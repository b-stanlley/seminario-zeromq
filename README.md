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

O cliente exibe um menu com três operações:

- resposta a uma mensagem de texto;
- alteração de um arquivo texto no servidor;
- cálculo de funções matemáticas.

Para sair, escolha:

```text
0
```

## Operações disponíveis

### 1. Resposta a mensagem de texto
- Digite qualquer mensagem e o servidor responde.

### 2. Alterar arquivo texto
- Grava uma linha no arquivo [arquivo_servidor.txt](arquivo_servidor.txt).

### 3. Cálculo de funções
Funções disponíveis:
- `quadrado,x` → x²
- `dobro,x` → 2*x
- `soma,a,b` → a+b
- `potencia,a,b` → a^b
- `raiz,x` → √x

Exemplo:
```
Digite a funcao e parametros (ex: quadrado,5): quadrado,5
Resposta do servidor: quadrado(5.0) = 25.0
```

## Observações

- Se a porta estiver em uso, troque para outra, como `5560`.
- O servidor responde com `World` quando recebe `Hello`.
