# Seminário ZeroMQ

Projeto com comunicação cliente/servidor utilizando ZeroMQ.

Agora o projeto possui **implementações de servidor Node.js**:

*  Python
*  Node.js

---

##  Dependências

### Python

Instale via:

```bash
pip install -r requirements.txt
```

### Node.js

Entre na pasta do servidor Node:

```bash
cd server-node
npm install
```

---

##  Como criar e usar o venv (Python)

### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

---

##  Como executar

Abra dois terminais.

---


### Terminal 1
##  Servidor Node.js

```bash
cd server-node
node server.js
```

---

##  Cliente (Python)

### Terminal 2

```bash
python client.py --host 127.0.0.1 --port 5555
```

---

##  Comunicação

Utiliza o padrão:

* REQ/REP (cliente-servidor)

---

##  Operações disponíveis

### 1. Resposta a mensagem de texto

* Digite a mensagem 'Hello' e o servidor responde 'Hello World'.

### 2. Alterar arquivo texto

* Grava uma linha no arquivo [arquivo_servidor.txt](arquivo_servidor.txt).

### 3. Cálculo de funções

Funções disponíveis:

* `quadrado,x` → x²
* `dobro,x` → 2*x
* `soma,a,b` → a+b
* `potencia,a,b` → a^b
* `raiz,x` → √x

Exemplo:

```
Digite a funcao e parametros (ex: quadrado,5): quadrado,5
Resposta do servidor: quadrado(5.0) = 25.0
```

---

##  Observações

* Se a porta estiver em uso, troque para outra (ex: `5560`)
* O servidor responde com `World` quando recebe `Hello`

---

##  Estrutura do projeto

```
/server-node      → servidor em Node.js
/client.py        → cliente
```
