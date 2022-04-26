"""Generate some labels from the commits names."""
from auto_labels.gitmanager import Git
from auto_labels.interfaces import ScrappersResults, GitScrapper
from auto_labels.generators.regex import RegexGenerator, RegexConfig


class CommitsScrapper(GitScrapper):
    """Get all commits."""

    def __call__(self, ref1: str, ref2: str) -> ScrappersResults:
        """Collect all the data from ref1 to ref2, return them as a list."""
        commits = Git().commits_list_from_refs(ref1, ref2)
        return [str(com.message) for com in commits]


class FromCommits(RegexGenerator):
    """Generate some labels from the commits names."""

    def __init__(self, config: RegexConfig):
        super().__init__(config, CommitsScrapper())
