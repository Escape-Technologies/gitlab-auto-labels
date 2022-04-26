"""Test the config."""
import pytest
import os

from auto_labels.config import ConfigGenerator
from auto_labels.generators.from_commits import FromCommits
from auto_labels.generators.from_files import FromFiles
from auto_labels.generators.from_branch import FromBranch


def path_to_config(config_folder: str) -> str:
    """Return the absolute path to the ./config/{config_folder}"""
    here = os.path.abspath(os.path.join(__file__, os.pardir))
    config = os.path.join(here, "configs")
    target = os.path.join(config, config_folder)
    return target


def cd_to_config(config_folder: str) -> None:
    """Change directory to the ./config/{config_folder}"""
    os.chdir(path_to_config(config_folder))


@pytest.mark.parametrize('folder, result', [
    ("all", [FromCommits, FromFiles, FromBranch]),
    ("branch", [FromBranch]),
    ("commits", [FromCommits]),
    ("files", [FromFiles]),
])
def test_base_config(folder: str, result: list) -> None:
    """Test the base config."""
    cd_to_config(folder)
    config = ConfigGenerator()
    assert set(map(type, config.config)) == set(result)
