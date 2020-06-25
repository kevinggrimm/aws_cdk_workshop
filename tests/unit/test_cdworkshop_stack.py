import json
import pytest

from aws_cdk import core
from cdworkshop.cdworkshop_stack import CdworkshopStack


def get_template():
    app = core.App()
    CdworkshopStack(app, "cdworkshop")
    return json.dumps(app.synth().get_stack("cdworkshop").template)


def test_sqs_queue_created():
    assert("AWS::SQS::Queue" in get_template())


def test_sns_topic_created():
    assert("AWS::SNS::Topic" in get_template())
