import boto3
import json

client = boto3.client(
    service_name="bedrock-runtime",
    region_name="us-east-1",
    verify=False
)

prompt = "Explain Amazon Bedrock features"

body = {
    "prompt": prompt,
    "max_gen_len": 300,
    "temperature": 0.5,
    "top_p": 0.9
}

response = client.invoke_model(
    modelId="meta.llama3-8b-instruct-v1:0",
    body=json.dumps(body)
)

response_body = json.loads(response["body"].read())

print(response_body)