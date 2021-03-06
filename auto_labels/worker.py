"""Generate labels from two commit refs."""
from typing import List, Set
from os import getenv

from auto_labels.interfaces import LabelsGenerator, Label, Sender
from auto_labels.senders.gitlab import GitlabSender
from auto_labels.senders.console import ConsoleSender

class Worker:
    """The general program."""

    def __init__(self, generators: List[LabelsGenerator]):
        """Setup the labels generator."""
        self.generators = generators

    def __call__(self, ref1: str, ref2: str) -> None:
        """Run all the code."""
        labels = self.generate_labels(ref1, ref2)
        self.send_labels(labels)

    def generate_labels(self, ref1: str, ref2: str) -> Set[Label]:
        """Generate labels from two commit refs."""
        labels: Set[Label] = set()
        for generator in self.generators:
            labels.update(generator(ref1, ref2))
        return labels

    def send_labels(self, labels: Set[Label]) -> None:
        """Send the labels to the output."""
        self.get_output().send_labels(labels)

    @staticmethod
    def get_output() -> Sender:
        """Return the output."""
        if getenv("CI_MERGE_REQUEST_IID"):
            return GitlabSender()
        return ConsoleSender()
