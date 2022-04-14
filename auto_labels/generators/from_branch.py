"""Generate some labels from the branch name."""
from functools import partial

from auto_labels.interfaces import ScrappersResults, GitScrapper
from auto_labels.generators.regex import RegexGenerator


# pylint: disable=too-few-public-methods
class BranchScrapper(GitScrapper):
    """Get all commits."""

    def __call__(self, ref1: str, ref2: str) -> ScrappersResults:
        """Collect all the data from ref1 to ref2, return them as a list."""
        # TODO
        return ["a"]


FromBranch = partial(RegexGenerator, scrapper=BranchScrapper())
