"""Some basic interfaces to keep the programe upgradable."""
from abc import ABC, abstractmethod
from typing import List

Label = str
ScrappersResults = List[str]


# pylint: disable=too-few-public-methods
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
    def generate_labels(self, data: ScrappersResults) -> List[Label]:
        """Generate labels from a scrapping result."""

    def __call__(self, ref1: str, ref2: str) -> List[Label]:
        """Generate labels."""
        return self.generate_labels(self.scrapper(ref1, ref2))
