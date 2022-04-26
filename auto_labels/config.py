"""Generate LabelsGenerators from the config file."""
from typing import List, Dict, Optional
import json
from os import getenv

from auto_labels.interfaces import LabelsGenerator, Label
from auto_labels.generators.from_commits import FromCommits
from auto_labels.generators.from_files import FromFiles
from auto_labels.generators.from_branch import FromBranch

DEFAULT_CONFIG_PATH: str = ".auto_labels.json"
CONFIG_MAPPING = {
    "commits": FromCommits,
    "files": FromFiles,
    "branch": FromBranch,
}


class ConfigGenerator:
    """Generate the config."""

    _config: Dict[str, Dict[str, Label]]

    def __init__(self, config_path: Optional[str] = None):
        """Init with the config."""
        self._config = self.load_config(config_path)

    @property
    def config(self) -> List[LabelsGenerator]:
        """Get the config."""
        lst: List[LabelsGenerator] = []
        for key, config in self._config.items():
            lst.append(CONFIG_MAPPING[key](config))
        return lst

    def load_config(self, config_path: Optional[str]):
        """Load a config and set it as the file."""
        if config_path:
            return self._load_config(config_path)
        elif (config_path := getenv('AUTO_LABELS_CONFIG_PATH')):
            return self._load_config(config_path)
        else:
            return self._load_config(DEFAULT_CONFIG_PATH)

    def _load_config(self, config_path: str):
        """Load a config from the given file."""
        with open(config_path, 'r', encoding='utf-8') as config_file:
            return json.load(config_file)
