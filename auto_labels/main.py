"""Generate labels from two commit refs."""


def main(ref1: str, ref2: str) -> int:
    """Generate labels from two commit refs.

    Args:
        ref1 (str): commit ref
        ref2 (str): commit ref

    Returns:
        int: return code
    """
    print(f"{ref1} -> {ref2}")
    return 0
