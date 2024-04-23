# create_fake_data
### Criando dados fake com a biblioteca Faker do Python

Essa biblioteca gera dados fake e conseguimos popular bases para realizarmos trabalhos diversos.

| Pasta  | Descrição                                     |
|--------|-----------------------------------------------|
| lambda | Gerar dados via AWS Lambda                    |
| local  | Gerar dados localmente                        |
| package | Lib necessária para criar o AWS Lambda Layer  |

Instalar a lib utilizando pip:
```bash
pip install Faker
```

- Local: <br> 
    Para gerar os dados localmente será necessário ter instalado awscli e configurado as secrets da AWS.
  ```bash
  pip install awscli
  ```
- Lambda: <br>
    Para gerar os dados via Lambda será necessário primeiro criar a Layer (package) e depois executar a Lambda.
    O zip está na pasta package, basta fazer o upload do zip diretamente ou adicionar no bucket e fazer o apontamento.

#### Links
Lib Faker - https://faker.readthedocs.io/en/master/index.html <br>
Criando lambda layer - https://www.linkedin.com/pulse/add-external-python-libraries-aws-lambda-using-layers-gabe-olokun/
