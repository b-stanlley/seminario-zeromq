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

    def enviar_requisicao(self, requisicao: str) -> None:
        try:
            self.socket.send_string(requisicao)
            resposta = self.socket.recv_string()
            print(f"Resposta do servidor: {resposta}")
        except zmq.error.ZMQError as erro:
            print(f"[Erro ZeroMQ] {erro}")

    def encerrar(self) -> None:
        self.socket.close(0)


def mostrar_menu() -> None:
    print("\n=== Menu do cliente ===")
    print("1 - Resposta a uma mensagem de texto")
    print("2 - Alterar um arquivo texto no servidor")
    print("0 - Sair")


def main() -> None:
    argumentos = ler_argumentos()
    cliente = ClienteZeroMQ(argumentos.host, argumentos.port)

    try:
        cliente.conectar_servidor()

        while True:
            mostrar_menu()
            opcao = input("Escolha uma opcao: ")

            try:
                opcao_num = int(opcao)
            except ValueError:
                print("Opcao invalida.")
                continue

            match opcao_num:
                case 0:
                    break
                case 1:
                    mensagem = input("Digite a mensagem: ")

                    if mensagem:
                        cliente.enviar_requisicao(f"{opcao}|{mensagem}")
                case 2:
                    texto = input("Digite o texto para gravar no arquivo do servidor: ")

                    if texto:
                        cliente.enviar_requisicao(f"{opcao}|{texto}")
                case _:
                    print("Opcao invalida.")

    except KeyboardInterrupt:
        print("\n[Conexão encerrada]")
    finally:
        cliente.encerrar()


if __name__ == "__main__":
    main()