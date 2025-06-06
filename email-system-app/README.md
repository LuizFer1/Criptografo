# Email System Application

Este projeto é um sistema de e-mails que permite enviar e receber mensagens com criptografia. A aplicação é estruturada em vários módulos, cada um responsável por uma parte específica do sistema.

## Estrutura do Projeto

```
email-system-app
├── src
│   ├── app.py               # Ponto de entrada da aplicação
│   ├── email_client.py      # Classe para enviar e receber e-mails
│   ├── encryption.py        # Funções para criptografar e descriptografar mensagens
│   ├── utils.py             # Funções utilitárias
│   └── types
│       └── __init__.py      # Tipos e interfaces utilizados no projeto
├── requirements.txt         # Dependências do projeto
└── README.md                # Documentação do projeto
```

## Instalação

Para instalar as dependências do projeto, execute o seguinte comando:

```
pip install -r requirements.txt
```

## Uso

Para iniciar a aplicação, execute o arquivo `app.py`:

```
python src/app.py
```

## Arquitetura

- **app.py**: Inicializa o sistema de e-mails e gerencia o fluxo de envio e recebimento de mensagens.
- **email_client.py**: Contém a classe `EmailClient` com métodos para enviar e receber e-mails, utilizando criptografia.
- **encryption.py**: Define funções para criptografar e descriptografar mensagens.
- **utils.py**: Contém funções utilitárias, como validação de endereços de e-mail.
- **types/__init__.py**: Define tipos e interfaces para padronizar a estrutura dos dados.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.