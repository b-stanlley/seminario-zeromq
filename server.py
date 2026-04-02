import zmq
import argparse


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
        
    def iniciar_servidor(self):
        try:
            self.socket.bind(self.endpoint)
            print(f"Servidor iniciado em {self.endpoint}")

            while True:
                mensagem = self.socket.recv_string()

                if mensagem == "Hello":
                    resposta = "World"
                else:                    
                    resposta = "Mensagem desconhecida"

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