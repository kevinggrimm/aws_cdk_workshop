from aws_cdk import (
    core,
    aws_lambda as _lambda,
    aws_apigateway as apigw,
)

from cdk_dynamo_table_viewer import TableViewer
from hitcounter import HitCounter

class CdworkshopStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        my_lambda = _lambda.Function(
            self, 'HelloHandler',
            runtime=_lambda.Runtime.PYTHON_3_7, # Runtime environment
            code=_lambda.Code.from_asset('lambda'), # Loaded from Lambda dir
            handler='hello.handler', # Name of file, function
        )

        hello_with_counter = HitCounter(
            self, 'HelloHitCounter',
            downstream=my_lambda,
        )

        apigw.LambdaRestApi(
            self, 'Endpoint',
            handler=hello_with_counter.handler,
        )

        TableViewer(
            self, 'ViewHitCounter',
            title='Hello Hits',
            table=hello_with_counter.table,
            sort_by='-hits'
        )