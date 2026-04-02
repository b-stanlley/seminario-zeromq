# Seminário ZeroMQ

Projeto simples com servidor e cliente usando ZeroMQ em Python.

## Dependências

Instale as dependências em [requirements.txt](requirements.txt):


## Como criar e usar o venv
### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Como executar

Abra dois terminais.

### Terminal 1: servidor

```bash
python server.py --host 127.0.0.1 --port 5555
```

### Terminal 2: cliente

```bash
python client.py --host 127.0.0.1 --port 5555
```

O cliente exibe um menu com duas operações:

- resposta a uma mensagem de texto;
- alteração de um arquivo texto no servidor.

Para sair, escolha:

```text
0
```

## Arquivo texto no servidor

O servidor grava as alterações em [arquivo_servidor.txt](arquivo_servidor.txt).

## Observações

- Se a porta estiver em uso, troque para outra, como `5560`.
- O servidor responde com `World` quando recebe `Hello`.
