## Baseline: AWS Lambda com Serverless Framework

Este projeto consiste em uma função AWS Lambda simples que retorna uma mensagem "Hello, World!". Utilizamos o framework
Serverless para facilitar o deploy da aplicação. Para controle de dependências, usamos o Poetry. O projeto também inclui
um pipeline de CI/CD configurado com GitHub Actions para garantir a qualidade do código através de hooks do pre-commit,
testes unitários e relatórios de cobertura enviados para o SonarCloud.

## Estrutura do Projeto

```plaintext
.
├── .github
│   └── workflows
│       └── ci.yml
│       └── deploy.yml
│       └── publish.yml
├── .pre-commit-config.yaml
├── serverless.yml
├── pyproject.toml
├── README.md
├── handler.py
└── tests
    └── test_handler.py
```    

## Dependências

Este projeto utiliza o Poetry para gerenciamento de dependências. As dependências são definidas no arquivo
pyproject.toml.

## Instalação de Dependências

Para instalar as dependências do projeto, execute:

```
poetry install
```

## Deploy

O framework Serverless é utilizado para gerenciar o deploy da função AWS Lambda. A configuração do Serverless está no
arquivo serverless.yml.

### Comandos para Deploy

Para fazer o deploy da aplicação, execute:

```
serverless config credentials --provider aws --key <AWS Access key> --secret <AWS Secret key>
serverless deploy
```

## CI/CD

Utilizamos GitHub Actions para configurar o pipeline de CI/CD. O pipeline inclui:

- pre-commit hooks: Para garantir a qualidade do código.
- Testes unitários: Para verificar o funcionamento correto da aplicação.
- Cobertura de testes: Para garantir que todo o código está sendo testado, com relatórios enviados para o SonarCloud.

## CI

### Pre-commit

O pre-commit está definido no arquivo .pre-commit-config.yaml, execute:

```
 pre-commit run --all-files
```

### Testes

Os testes unitários estão localizados no diretório tests. Para verificar os testes, execute:

```
 python -m unittest
```

### Cobertura de testes

Para verificar combertura de testes, execute:

```
 coverage run -m unittest discover tests
 coverage report
```

## CD
Para realizar o deploy automático usando GitHub Actions, devemos configurar as seguintes variáveis de ambiente:

- AWS_REGION
- ROLE_TO_ASSUME

### Ambiente de Desenvolvimento
O deploy em desenvolvimento ocorrerá sempre que houver uma atualização na branch develop.

### Ambiente de Produção
O deploy em produção ocorrerá ao gerar uma nova release.

## Configuração do GitHub Actions

O pipeline de CI está definido no arquivo .github/workflows/ci.yml. Para configurá-lo, adicione os seguintes secrets no
seu repositório GitHub:

```
- SONAR_TOKEN
- GIT_TOKEN
```

O Sonar está definido no aquivo sonar-project.properties. Para configurá-lo, adicione os seguintes dados:

```
sonar.organization=OGANIZAÇÂO
sonar.projectKey=PROJETO
```