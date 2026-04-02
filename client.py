import argparse
import zmq


def ler_argumentos():
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", type=str, required=True)
    parser.add_argument("--port", type=int, required=True)
    args = parser.parse_args()

    return args


class ClienteZeroMQ:
    def __init__(self, host:str, port:int):
        self.host = host
        self.port = port
        self.context = zmq.Context().instance()
        self.socket = self.context.socket(zmq.REQ)
        self.endpoint = f"tcp://{self.host}:{self.port}"

    def conectar_servidor(self) -> None:
        try:
            self.socket.connect(self.endpoint)
            print(f"Conectado ao servidor em {self.endpoint}")
        except zmq.error.ZMQError as erro:
            print(f"[Erro ZeroMQ] {erro}")
            raise

    def enviar_mensagem(self) -> None:
        try:
            self.socket.send_string(self.msg)
            resposta = self.socket.recv_string()
            print(f"Resposta do servidor: {resposta}")
        except zmq.error.ZMQError as erro:
            print(f"[Erro ZeroMQ] {erro}")

    def encerrar(self) -> None:
        self.socket.close(0)
        
        
def main() -> None:
    argumentos = ler_argumentos()
    cliente = ClienteZeroMQ(argumentos.host, argumentos.port)

    try:
        cliente.conectar_servidor()

        while True:
            cliente.msg = input("Digite a mensagem ou 'sair' para encerrar a conexao: ").strip()

            if cliente.msg.lower() == "sair":
                break

            if not cliente.msg:
                continue

            cliente.enviar_mensagem()

    except KeyboardInterrupt:
        print("\n[Conexão encerrada]")
    finally:
        cliente.encerrar()


if __name__ == "__main__":
    main()