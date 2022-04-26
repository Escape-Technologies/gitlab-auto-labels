"""Get git data for the generators."""
from typing import List

from git import Repo
from git.objects.commit import Commit


class Git:

    """Get git data for the generators."""

    def __init__(self):
        """Setup the repo"""
        try:
            self.repo = Repo.init()
        except Exception as e:
            raise EnvironmentError("You seems not to be in a git repository.") from e

    @property
    def current_branch_name(self):
        """Return the current branch."""
        return self.repo.active_branch.name

    def commits_list_from_refs(self, ref1: str, ref2: str) -> List[Commit]:
        """Return the sublist of commit [ref1] to commit [ref2]."""
        return list(self.repo.iter_commits(f"{ref1}..{ref2}"))

    def branch_name(self, ref2: str) -> str:
        """Return the branch name."""
        commit = next(self.repo.iter_commits(ref2))
        return commit.name_rev.split(" ")[1]
