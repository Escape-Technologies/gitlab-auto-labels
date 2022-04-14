"""Generate labels from two commit refs."""
from auto_labels.config import ConfigGenerator
from auto_labels.worker import Worker


def main(ref1: str, ref2: str, config_file: str = None) -> int:
    """Generate labels from two commit refs.

    Args:
        ref1 (str): commit ref
        ref2 (str): commit ref

    Returns:
        int: return code
    """
    config = ConfigGenerator(config_file)
    worker = Worker(config.config)
    worker(ref1, ref2)
    return 0
