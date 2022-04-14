"""Generate some labels from the files names."""
from functools import partial

from auto_labels.interfaces import ScrappersResults, GitScrapper
from auto_labels.generators.regex import RegexGenerator


# pylint: disable=too-few-public-methods
class FileScrapper(GitScrapper):
    """Get all files."""

    def __call__(self, ref1: str, ref2: str) -> ScrappersResults:
        """Collect all the data from ref1 to ref2, return them as a list."""
        # TODO
        return ["a"]


FromFile = partial(RegexGenerator, scrapper=FileScrapper())
