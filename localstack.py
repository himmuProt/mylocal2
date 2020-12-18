import localstack_client.session

session = localstack_client.session.Session()
sqs = session.client('sqs')
assert sqs.list_queues() is not None

import localstack_client.session
import pytest


@pytest.fixture(autouse=True)
def boto3_localstack_patch(monkeypatch):
    session_ls = localstack_client.session.Session()
    monkeypatch.setattr(boto3, "client", session_ls.client)
    monkeypatch.setattr(boto3, "resource", session_ls.resource)
sqs = boto3.client('sqs')
assert sqs.list_queues() is not None