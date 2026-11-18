"""Minimal PNG and PPM reading/writing with the standard library only.

PNG support: 8- or 16-bit, colour types 0 (grey), 2 (RGB), 3 (palette), 4 (grey+alpha) and
6 (RGBA), non-interlaced. Text chunks (tEXt) and other ancillary chunks are exposed so the
experiment can see which metadata survives conversions.
"""

import hashlib
import struct
import zlib

PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
# Private, ancillary, safe-to-copy chunk name used by the toy provenance manifest.
MANIFEST_CHUNK = b"prVn"


class Image:
    """An 8-bit RGB image stored as a flat bytearray (row-major, 3 bytes per pixel)."""

    __slots__ = ("width", "height", "rgb")

    def __init__(self, width: int, height: int, rgb):
        if len(rgb) != width * height * 3:
            raise ValueError("pixel buffer size does not match dimensions")
        self.width = width
        self.height = height
        self.rgb = bytearray(rgb)

    def copy(self) -> "Image":
        return Image(self.width, self.height, bytearray(self.rgb))

    def pixel_digest(self) -> str:
        """SHA-256 over dimensions and decoded pixels (what the toy manifest binds to)."""
        h = hashlib.sha256()
        h.update(b"RGB8")
        h.update(struct.pack(">II", self.width, self.height))
        h.update(bytes(self.rgb))
        return h.hexdigest()


def _chunk(ctype: bytes, data: bytes) -> bytes:
    crc = zlib.crc32(ctype + data) & 0xFFFFFFFF
    return struct.pack(">I", len(data)) + ctype + data + struct.pack(">I", crc)


def encode_png(img: Image, text=None, extra_chunks=None) -> bytes:
    stride = img.width * 3
    raw = bytearray()
    for y in range(img.height):
        raw.append(0)  # filter type 0 (None)
        raw += img.rgb[y * stride:(y + 1) * stride]
    ihdr = struct.pack(">IIBBBBB", img.width, img.height, 8, 2, 0, 0, 0)
    out = bytearray(PNG_SIGNATURE)
    out += _chunk(b"IHDR", ihdr)
    for key, value in (text or {}).items():
        out += _chunk(b"tEXt", key.encode("latin-1") + b"\x00" + value.encode("latin-1"))
    for ctype, data in (extra_chunks or []):
        out += _chunk(ctype, data)
    out += _chunk(b"IDAT", zlib.compress(bytes(raw), 9))
    out += _chunk(b"IEND", b"")
    return bytes(out)


def write_png(path, img: Image, text=None, extra_chunks=None) -> None:
    with open(path, "wb") as f:
        f.write(encode_png(img, text=text, extra_chunks=extra_chunks))


def _paeth(a: int, b: int, c: int) -> int:
    p = a + b - c
    pa, pb, pc = abs(p - a), abs(p - b), abs(p - c)
    if pa <= pb and pa <= pc:
        return a
    if pb <= pc:
        return b
    return c


def decode_png(data: bytes):
    """Return (Image, text_dict, other_chunks) where other_chunks is a list of (type, bytes)."""
    if data[:8] != PNG_SIGNATURE:
        raise ValueError("not a PNG file")
    pos = 8
    idat = bytearray()
    text = {}
    others = []
    palette = None
    width = height = bit_depth = colour_type = interlace = None
    while pos < len(data):
        (length,) = struct.unpack(">I", data[pos:pos + 4])
        ctype = data[pos + 4:pos + 8]
        cdata = data[pos + 8:pos + 8 + length]
        pos += 12 + length
        if ctype == b"IHDR":
            width, height, bit_depth, colour_type, _comp, _filt, interlace = struct.unpack(">IIBBBBB", cdata)
        elif ctype == b"IDAT":
            idat += cdata
        elif ctype == b"PLTE":
            palette = bytes(cdata)
        elif ctype == b"tEXt":
            key, _, value = bytes(cdata).partition(b"\x00")
            text[key.decode("latin-1")] = value.decode("latin-1")
        elif ctype == b"IEND":
            break
        else:
            others.append((bytes(ctype), bytes(cdata)))
    if interlace:
        raise ValueError("interlaced PNG not supported")
    if bit_depth not in (8, 16):
        raise ValueError("unsupported bit depth %r" % bit_depth)
    channels = {0: 1, 2: 3, 3: 1, 4: 2, 6: 4}[colour_type]
    sample_bytes = bit_depth // 8
    bpp = channels * sample_bytes
    stride = width * bpp
    raw = zlib.decompress(bytes(idat))
    prev = bytearray(stride)
    rows = []
    i = 0
    for _ in range(height):
        ftype = raw[i]
        line = bytearray(raw[i + 1:i + 1 + stride])
        i += 1 + stride
        if ftype == 1:
            for x in range(bpp, stride):
                line[x] = (line[x] + line[x - bpp]) & 0xFF
        elif ftype == 2:
            for x in range(stride):
                line[x] = (line[x] + prev[x]) & 0xFF
        elif ftype == 3:
            for x in range(stride):
                left = line[x - bpp] if x >= bpp else 0
                line[x] = (line[x] + ((left + prev[x]) >> 1)) & 0xFF
        elif ftype == 4:
            for x in range(stride):
                a = line[x - bpp] if x >= bpp else 0
                c = prev[x - bpp] if x >= bpp else 0
                line[x] = (line[x] + _paeth(a, prev[x], c)) & 0xFF
        elif ftype != 0:
            raise ValueError("bad PNG filter type %d" % ftype)
        rows.append(line)
        prev = line
    rgb = bytearray(width * height * 3)
    o = 0
    for line in rows:
        for x in range(width):
            base = x * bpp
            samples = [line[base + k * sample_bytes] for k in range(channels)]  # high byte if 16-bit
            if colour_type == 2 or colour_type == 6:
                r, g, b = samples[0], samples[1], samples[2]
            elif colour_type == 3:
                idx = samples[0] * 3
                r, g, b = palette[idx], palette[idx + 1], palette[idx + 2]
            else:  # grey or grey+alpha
                r = g = b = samples[0]
            rgb[o] = r
            rgb[o + 1] = g
            rgb[o + 2] = b
            o += 3
    return Image(width, height, rgb), text, others


def read_png(path):
    with open(path, "rb") as f:
        return decode_png(f.read())


def write_ppm(path, img: Image) -> None:
    with open(path, "wb") as f:
        f.write(b"P6\n%d %d\n255\n" % (img.width, img.height))
        f.write(bytes(img.rgb))


def read_ppm(path) -> Image:
    with open(path, "rb") as f:
        data = f.read()
    tokens = []
    pos = 0
    while len(tokens) < 4:
        while data[pos:pos + 1].isspace():
            pos += 1
        if data[pos:pos + 1] == b"#":
            while data[pos:pos + 1] not in (b"\n", b""):
                pos += 1
            continue
        start = pos
        while not data[pos:pos + 1].isspace():
            pos += 1
        tokens.append(data[start:pos])
    pos += 1  # single whitespace after maxval
    magic, w, h, maxval = tokens[0], int(tokens[1]), int(tokens[2]), int(tokens[3])
    if maxval != 255:
        raise ValueError("only 8-bit PPM/PGM supported")
    body = data[pos:]
    if magic == b"P6":
        return Image(w, h, body[: w * h * 3])
    if magic == b"P5":
        grey = body[: w * h]
        return Image(w, h, bytes(v for g in grey for v in (g, g, g)))
    raise ValueError("unsupported PNM type %r" % magic)
