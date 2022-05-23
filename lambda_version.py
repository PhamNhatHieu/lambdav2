import boto3

lambda_client =  boto3.client('lambda')

response = lambda_client.publish_version(
    FunctionName='helloWorldLambda'
)

print(response)