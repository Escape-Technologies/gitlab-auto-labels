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
        self.base_url = getenv("CI_API_V4_URL")
        self.merge_request_project_id = getenv("CI_MERGE_REQUEST_PROJECT_ID")
        self.merge_request_iid = getenv("CI_MERGE_REQUEST_IID")
        self.merge_request_labels = getenv("CI_MERGE_REQUEST_LABELS")
        self.token = getenv("CI_JOB_TOKEN")

    @property
    def url(self) -> str:
        """Return the URL."""
        return f"{self.base_url}/projects/{self.merge_request_project_id}/merge_requests/{self.merge_request_iid}"

    def send_labels(self, labels: Set[Label]) -> None:
        if self.merge_request_labels:
            labels.update(set(self.merge_request_labels.split(",")))
        labels_str = ",".join(labels)
        req = requests.put(self.url, headers={"PRIVATE-TOKEN": self.token}, data={"labels": labels_str})
        if not req.ok:
            print(req.text, req.status_code)
