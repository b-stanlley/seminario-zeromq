# Seminário ZeroMQ - Servidor Node.js

Servidor ZeroMQ implementado em Node.js usando o padrão Request/Reply.

## Dependências

Instale as dependências via npm:

```bash
npm install
```

## Como executar

```bash
node ServerNode/server.js
```

O servidor Node.js escuta na porta `5555` e implementa o padrão ZeroMQ Reply/Request.

## Operações suportadas

### 1. Echo de texto
- Recebe uma mensagem e responde
- Exemplo: `Hello` → `World`

### 2. Operações com arquivo
- Escreve linhas em `arquivo_servidor.txt`

### 3. Cálculo de funções
Funções matemáticas disponíveis:
- `quadrado,x` → x²
- `dobro,x` → 2*x
- `raiz,x` → √x

## Observações

- Porta padrão: `5555` (pode ser alterada no código)
- O servidor responde com `World` quando recebe `Hello`
- Compatible com clientes ZeroMQ em qualquer linguagem
