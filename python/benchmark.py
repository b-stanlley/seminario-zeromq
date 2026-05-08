import argparse
import zmq
import time


def ler_argumentos():
    parser = argparse.ArgumentParser(description="Benchmark ZeroMQ")
    parser.add_argument("--host", type=str, default="localhost")
    parser.add_argument("--port", type=int, default=5555)
    parser.add_argument("--requisicoes", type=int, default=10)
    parser.add_argument("--opcao", type=int, default=1)
    parser.add_argument("--payload", type=str, default="teste")
    
    return parser.parse_args()


def main():
    args = ler_argumentos()
    
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect(f"tcp://{args.host}:{args.port}")
    
    print(f"Conectado a {args.host}:{args.port}\n")
    
    for i in range(1, args.requisicoes + 1):
        mensagem = f"{args.opcao}|{args.payload}"
        
        inicio = time.perf_counter()
        socket.send_string(mensagem)
        resposta = socket.recv_string()
        fim = time.perf_counter()
        
        tempo_ms = (fim - inicio) * 1000
        print(f"Requisição {i}: {tempo_ms:.2f}ms")
    
    socket.close(0)
    context.term()


if __name__ == "__main__":
    main()
