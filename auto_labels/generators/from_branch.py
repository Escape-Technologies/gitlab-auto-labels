"""Generate some labels from the branch name."""
from auto_labels.gitmanager import Git
from auto_labels.interfaces import ScrappersResults, GitScrapper
from auto_labels.generators.regex import RegexGenerator, RegexConfig


class BranchScrapper(GitScrapper):
    """Get all commits."""

    def __call__(self, ref1: str, ref2: str) -> ScrappersResults:
        """Collect all the data from ref1 to ref2, return them as a list."""
        return [Git().branch_name(ref2)]


class FromBranch(RegexGenerator):
    """Generate some labels from the commits names."""

    def __init__(self, config: RegexConfig):
        super().__init__(config, BranchScrapper())
