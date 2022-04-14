"""Generate some labels from the commits names."""
from functools import partial

from auto_labels.interfaces import ScrappersResults, GitScrapper
from auto_labels.generators.regex import RegexGenerator


# pylint: disable=too-few-public-methods
class CommitsScrapper(GitScrapper):
    """Get all commits."""

    def __call__(self, ref1: str, ref2: str) -> ScrappersResults:
        """Collect all the data from ref1 to ref2, return them as a list."""
        # TODO
        return ["a"]


FromCommits = partial(RegexGenerator, scrapper=CommitsScrapper())
