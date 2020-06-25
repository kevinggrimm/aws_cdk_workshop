#!/usr/bin/env python3

from aws_cdk import core

from cdworkshop.cdworkshop_stack import CdworkshopStack


app = core.App()
CdworkshopStack(app, "cdworkshop", env={'region': 'us-west-2'})

app.synth()
