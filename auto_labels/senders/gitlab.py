"""Use Gitlab API"""
from typing import Set
from os import getenv

import requests

from auto_labels.interfaces import Label, Sender

class GitlabSender(Sender):

    """Use Gitlab API"""

    def __init__(self):
        """Setup the class."""
        super().__init__()
        self.url = getenv("GITLAB_URL")

    def send_labels(self, labels: Set[Label]) -> None:
        labels_str = ",".join(labels)
        requests.post(self.url, data={"labels": labels_str})
