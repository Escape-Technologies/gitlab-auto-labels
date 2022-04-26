"""Print to console for debugging."""
from typing import Set

from auto_labels.interfaces import Label, Sender

class ConsoleSender(Sender):

    """Print to console for debugging."""

    def send_labels(self, labels: Set[Label]) -> None:
        for label in labels:
            print(label)
