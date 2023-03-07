import boto3
client = boto3.client(
    'dynamodb',
    aws_access_key_id='AKIAXMCJPEKIKJYX6TVS',
    aws_secret_access_key='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',
    )
dynamodb = boto3.resource(
    'dynamodb',
    aws_access_key_id='AKIAXMCJPEKIKJYX6TVS',
    aws_secret_access_key='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',
    )
ddb_exceptions = client.exceptions


