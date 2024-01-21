import json
import boto3
from faker import Faker

fake = Faker('pt-BR')
s3 = boto3.client('s3')


def generate_data(qtd_data: int):
    data = []
    file = 'landing/fake_data.json'
    bucket = 'SEU_REPOSITORIO'

    try:
        for _ in range(qtd_data):
            info = {
                "id": fake.uuid4(),
                "nome": fake.name(),
                "cidade": fake.city(),
                "estado": fake.country(),
                "email": fake.email(),
                "telefone": fake.phone_number(),
            }
            data.append(info)

        # Criando json
        create_json = json.dumps(data, separators=(',', ':'), ensure_ascii=False)
        # Fazendo upload do arquivo json no bucket
        s3.put_object(Body=create_json, Bucket=bucket, Key=file)

        print('Arquivo gerado com sucesso!')
    except Exception:
        raise Exception


if __name__ == '__main__':
    generate_data(20)
