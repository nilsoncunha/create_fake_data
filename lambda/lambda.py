import json
import boto3
from faker import Faker

fake = Faker('pt-BR')
s3 = boto3.client('s3')


def lambda_handler(event, context):
    # TODO implement
    data = []
    file = 'landing/sample.json'
    bucket = 'SEU_REPOSITORIO'

    try:
        # TODO: write code...
        for index in range(20):
            info = {
                "id": fake.uuid4(),
                "nome": fake.name(),
                "cidade": fake.city(),
                "estado": fake.country(),
                "email": fake.email(),
                "telefone": fake.phone_number(),
            }
            data.append(info)

        create_json = json.dumps(data, separators=(',', ':'), ensure_ascii=False)
        s3.put_object(Body=create_json, Bucket=bucket, Key=file)

        return {
            'statusCode': 200,
            'body': 'File uploaded successfully.'
        }
    except Exception:
        raise Exception

