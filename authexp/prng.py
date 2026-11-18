"""Deterministic pseudo-random numbers (SplitMix64), independent of Python's `random` module,
so generated images and watermark patterns are identical across Python versions."""

import hashlib

MASK64 = (1 << 64) - 1


def seed_from_text(text: str) -> int:
    """Derive a 64-bit seed from a text label."""
    return int.from_bytes(hashlib.sha256(text.encode("utf-8")).digest()[:8], "big")


class SplitMix64:
    def __init__(self, seed: int):
        self.state = seed & MASK64

    def next_u64(self) -> int:
        self.state = (self.state + 0x9E3779B97F4A7C15) & MASK64
        z = self.state
        z = ((z ^ (z >> 30)) * 0xBF58476D1CE4E5B9) & MASK64
        z = ((z ^ (z >> 27)) * 0x94D049BB133111EB) & MASK64
        return z ^ (z >> 31)

    def uniform(self) -> float:
        """Float in [0, 1)."""
        return (self.next_u64() >> 11) * (1.0 / (1 << 53))

    def randint(self, lo: int, hi: int) -> int:
        """Integer in [lo, hi] (inclusive)."""
        return lo + int(self.uniform() * (hi - lo + 1))
