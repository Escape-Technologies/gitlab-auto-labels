"""Generate some labels from the files names."""
from typing import Set
from auto_labels.gitmanager import Git
from auto_labels.interfaces import ScrappersResults, GitScrapper
from auto_labels.generators.regex import RegexGenerator, RegexConfig


class FileScrapper(GitScrapper):
    """Get all files."""

    def __call__(self, ref1: str, ref2: str) -> ScrappersResults:
        """Collect all the data from ref1 to ref2, return them as a list."""
        commits = Git().commits_list_from_refs(ref1, ref2)
        all_files: Set[str] = set(
            str(k)
            for commit in commits
            for k in commit.stats.files.keys()
        )
        return list(all_files)

class FromFiles(RegexGenerator):
    """Generate some labels from the commits names."""

    def __init__(self, config: RegexConfig):
        super().__init__(config, FileScrapper())
