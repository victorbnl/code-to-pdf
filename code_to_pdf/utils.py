"""Utility functions."""


def is_dark_color(color: str) -> bool:
    """Returns True if `color` (as hex string) is dark, False if it's light."""

    rgb = tuple(int(color[i : i + 2], 16) for i in range(1, 7, 2))
    return sum(rgb) / 3 < 127.5
