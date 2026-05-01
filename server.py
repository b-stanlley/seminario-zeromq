import argparse
from pathlib import Path
import zmq


ARQUIVO_TEXTO = Path(__file__).with_name("arquivo_servidor.txt")
OPCAO_TEXTO = 1
OPCAO_ARQUIVO = 2
OPCAO_CALCULO = 3


def ler_argumentos():
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", type=str, required=True)
    parser.add_argument("--port", type=int, required=True)
    args = parser.parse_args()

    return args


class ServidorZeroMQ:
    def __init__(self, host:str, port:int):
        self.host = host
        self.port = port
        self.context = zmq.Context().instance()
        self.socket = self.context.socket(zmq.REP)
        self.endpoint = f"tcp://{self.host}:{self.port}"
        self.arquivo_texto = ARQUIVO_TEXTO

    def responder_texto(self, mensagem: str) -> str:
        if mensagem == "Hello":
            return "World"
        else:
            return "Mensagem desconhecida"

    def alterar_arquivo_texto(self, novo_texto: str) -> str:
        novo_texto = novo_texto

        if not novo_texto:
            return "[Erro] O texto enviado está vazio."

        with self.arquivo_texto.open("a", encoding="utf-8") as arquivo:
            arquivo.write(novo_texto + "\n")

        return f"Arquivo atualizado com sucesso em {self.arquivo_texto.name}."

    def calcular_funcoes(self, payload: str) -> str:
        try:
            partes = payload.split(",")
            funcao = partes[0].strip().lower()

            if funcao == "quadrado":
                x = float(partes[1].strip())
                resultado = x ** 2
                return f"quadrado({x}) = {resultado}"

            if funcao == "dobro":
                x = float(partes[1].strip())
                resultado = 2 * x
                return f"dobro({x}) = {resultado}"

            if funcao == "soma":
                a = float(partes[1].strip())
                b = float(partes[2].strip())
                resultado = a + b
                return f"soma({a}, {b}) = {resultado}"

            if funcao == "potencia":
                a = float(partes[1].strip())
                b = float(partes[2].strip())
                resultado = a ** b
                return f"potencia({a}, {b}) = {resultado}"

            if funcao == "raiz":
                x = float(partes[1].strip())
                resultado = x ** 0.5
                return f"raiz({x}) = {resultado}"

            return "[Erro] Funcao desconhecida. Use: quadrado, dobro, soma, potencia, raiz."

        except (IndexError, ValueError):
            return "[Erro] Formato invalido. Use: funcao,param1,param2,..."

    def processar_requisicao(self, mensagem: str) -> str:
        opcao_texto, payload = mensagem.split("|", 1)
        opcao = int(opcao_texto)
        
        match opcao:
            case 1:
                return self.responder_texto(payload)
            case 2:
                return self.alterar_arquivo_texto(payload)
            case 3:
                return self.calcular_funcoes(payload)
            case _:
                return "[Erro] Opcao desconhecida."
        
    def iniciar_servidor(self):
        try:
            self.socket.bind(self.endpoint)
            print(f"Servidor iniciado em {self.endpoint}")

            while True:
                mensagem = self.socket.recv_string()
                resposta = self.processar_requisicao(mensagem)
                self.socket.send_string(resposta)
        
        except zmq.error.ZMQError as erro:
            if "Address already in use" in str(erro):
                print(f"[Erro] A porta {self.port} já está em uso. Escolha outra porta.")
            else:
                print(f"[Erro ZeroMQ] {erro}")

        except KeyboardInterrupt:
            print("\n[Servidor] encerrado")
            
        finally:
            self.socket.close(0)


def main():
    argumentos = ler_argumentos()
    servidor = ServidorZeroMQ(argumentos.host, argumentos.port)
    servidor.iniciar_servidor()


if __name__ == "__main__":
    main()