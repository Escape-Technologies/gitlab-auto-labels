"""Test the config."""
import os
import pytest

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


@pytest.mark.parametrize("folder, result", [
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


@pytest.mark.parametrize("folder, result", [
    ("all", [FromCommits, FromFiles, FromBranch]),
    ("branch", [FromBranch]),
    ("commits", [FromCommits]),
    ("files", [FromFiles]),
])
def test_file_config(folder: str, result: list) -> None:
    """Test the base config."""
    # must works even if the local config file is not the right one
    cd_to_config("files")
    fp = os.path.join(path_to_config(folder), ".auto_labels.json")
    config = ConfigGenerator(fp)
    assert set(map(type, config.config)) == set(result)

@pytest.mark.parametrize("folder, result", [
    ("all", [FromCommits, FromFiles, FromBranch]),
    ("branch", [FromBranch]),
    ("commits", [FromCommits]),
    ("files", [FromFiles]),
])
def test_env_config(folder: str, result: list) -> None:
    """Test the base config."""
    # must works even if the local config file is not the right one
    cd_to_config("files")
    fp = os.path.join(path_to_config(folder), ".auto_labels.json")
    x = os.environ.get("AUTO_LABELS_CONFIG_PATH")
    os.environ["AUTO_LABELS_CONFIG_PATH"] = fp
    config = ConfigGenerator()
    assert set(map(type, config.config)) == set(result)
    if x:
        os.environ["AUTO_LABELS_CONFIG_PATH"] = x
