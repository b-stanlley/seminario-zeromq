const zmq = require("zeromq");
const fs = require("fs");

const OPCAO_SAIR = 0;
const OPCAO_TEXTO = 1;
const OPCAO_ARQUIVO = 2;
const OPCAO_CALCULO = 3;

function lerArgumentos() {
    const args = process.argv.slice(2);
    let host = "*";
    let port = 5555;

    for (let i = 0; i < args.length; i++) {
        if (args[i] === "--host" && i + 1 < args.length) {
            host = args[i + 1];
            i++;
        } else if (args[i] === "--port" && i + 1 < args.length) {
            port = parseInt(args[i + 1]);
            i++;
        }
    }

    return { host, port };
}

async function iniciarServidor(host, port) {
    const sock = new zmq.Reply();
    const endpoint = `tcp://${host}:${port}`;
    await sock.bind(endpoint);

    console.log(`Servidor Node.js rodando em ${endpoint}...`);

    for await (const [msg] of sock) {
        const mensagem = msg.toString();
        console.log("Recebido:", mensagem);

        const [opcaoStr, payload] = mensagem.split("|");
        const opcao = parseInt(opcaoStr);

        let resposta = "";

        switch (opcao) {

            case OPCAO_SAIR:
                resposta = "Servidor encerrando...";
                await sock.send(resposta);
                console.log("Encerrando servidor...");
                await sock.close();
                process.exit(0);
                break;

            case OPCAO_TEXTO:
                if (payload === "Hello") {
                    resposta = "World";
                } else {
                    resposta = "Mensagem desconhecida";
                }
                break;

            case OPCAO_ARQUIVO:
                fs.appendFileSync("arquivo_servidor.txt", payload + "\n");
                resposta = "Arquivo atualizado com sucesso.";
                break;

            case OPCAO_CALCULO:
                resposta = calcular(payload);
                break;

            default:
                resposta = "[Erro] Opcao invalida";
        }

        await sock.send(resposta);
    }
}

function calcular(payload) {
    try {
        const partes = payload.split(",");
        const funcao = partes[0];

        if (funcao === "quadrado") {
            const x = parseFloat(partes[1]);
            return `quadrado(${x}) = ${x * x}`;
        }

        else if (funcao === "raiz") {
            const x = parseFloat(partes[1]);
            return `raiz(${x}) = ${Math.sqrt(x)}`;
        }

        else if (funcao === "dobro") {
            const x = parseFloat(partes[1]);
            return `dobro(${x}) = ${2 * x}`;
        }

        else if (funcao === "soma") {
            const x = parseFloat(partes[1]);
            const y = parseFloat(partes[2]);
            return `soma(${x}, ${y}) = ${x + y}`;
        }

        else if (funcao === "potencia") {
            const x = parseFloat(partes[1]);
            const y = parseFloat(partes[2]);
            return `potencia(${x}, ${y}) = ${Math.pow(x, y)}`;
        }

        return "[Erro] Funcao desconhecida";

    } catch {
        return "[Erro] Falha no cálculo";
    }
}

const argumentos = lerArgumentos();
iniciarServidor(argumentos.host, argumentos.port);