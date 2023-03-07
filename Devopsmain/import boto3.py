import boto3

ACCESS_KEY = 'AKIAXMCJPEKIKJYX6TVS'
SECRET_KEY = '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'

s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)

