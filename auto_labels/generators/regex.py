"""Generate labels from a regex match over the given data."""
from typing import Set
from functools import reduce
import re

from auto_labels.interfaces import GitScrapper, LabelsGenerator
from auto_labels.interfaces import Label, ScrappersResults, RegexConfig


class RegexGenerator(LabelsGenerator):
    """Return all the labels from the modified files."""

    def __init__(self, config: RegexConfig, scrapper: GitScrapper):
        """Init with the config."""
        self.config = config
        super().__init__(scrapper)

    def generate_labels(self, data: ScrappersResults) -> Set[Label]:
        """Generate labels from a scrapping result."""
        return reduce(lambda x, y: x.union(y), map(self.process_one, data), set())

    def process_one(self, data: str) -> Set[Label]:
        """Return the matching labels"""
        result = set()
        for regex, to_add in self.config.items():
            if re.search(regex, data):
                result.add(to_add)
        return result
