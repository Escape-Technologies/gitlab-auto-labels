"""Generate LabelsGenerators from the config file."""
from typing import List, Dict, Optional
import json
from os import getenv

from auto_labels.interfaces import LabelsGenerator, Label
from auto_labels.generators.from_commits import FromCommits
from auto_labels.generators.from_files import FromFiles
from auto_labels.generators.from_branch import FromBranch

config_mapping = {
    "commits": FromCommits,
    "files": FromFiles,
    "branch": FromBranch,
}


class ConfigGenerator:
    """Generate the config."""

    _config: Dict[str, Dict[str, Label]]
    default_config_path: str = ".auto_labels.json"

    def __init__(self, config_path: Optional[str]):
        """Init with the config."""
        if config_path:
            self.load_config_from_file(config_path)
        elif (config_path := getenv('AUTO_LABELS_CONFIG_PATH')):
            self.load_config_from_file(config_path)
        else:
            self.load_config_from_file(self.default_config_path)
        self._config = {}

    @property
    def config(self) -> List[LabelsGenerator]:
        """Get the config."""
        lst: List[LabelsGenerator] = []
        for key, config in self._config.items():
            lst.append(config_mapping[key](config))
        return lst

    def load_config_from_file(self, config_path):
        """Load a config and set it as the file."""
        with open(config_path, 'r', encoding='utf-8') as config_file:
            self._config = json.load(config_file)
