"""Utilities for working with colours."""


def is_dark_colour(colour: str) -> bool:
    """Returns True if `colour` (as hex string) is dark, False if it's light."""

    rgb = tuple(int(colour[i : i + 2], 16) for i in range(1, 7, 2))
    return sum(rgb) / 3 < 127.5
