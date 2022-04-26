"""Some basic interfaces to keep the programe upgradable."""
from abc import ABC, abstractmethod
from typing import List, Set, Dict

Label = str
ScrappersResults = List[str]
RegexConfig = Dict[str, Label]


class GitScrapper(ABC):
    """Get some raw data from the git repo."""

    @abstractmethod
    def __call__(self, ref1: str, ref2: str) -> ScrappersResults:
        """Collect all the data from ref1 to ref2, return them as a list."""


class LabelsGenerator(ABC):
    """Generate labels from a scrapping result."""

    def __init__(self, scrapper: GitScrapper):
        """Init the generator."""
        self.scrapper = scrapper

    @abstractmethod
    def generate_labels(self, data: ScrappersResults) -> Set[Label]:
        """Generate labels from a scrapping result."""

    def __call__(self, ref1: str, ref2: str) -> Set[Label]:
        """Generate labels."""
        return self.generate_labels(self.scrapper(ref1, ref2))


class Sender(ABC):
    """Send labels to the output."""

    def __init__(self):
        """Setup the class."""

    @abstractmethod
    def send_labels(self, labels: Set[Label]) -> None:
        """Send labels to the output."""
