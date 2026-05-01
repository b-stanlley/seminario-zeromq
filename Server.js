const zmq = require("zeromq");
const fs = require("fs");

const OPCAO_TEXTO = 1;
const OPCAO_ARQUIVO = 2;
const OPCAO_CALCULO = 3;

async function iniciarServidor() {
    const sock = new zmq.Reply();
    await sock.bind("tcp://*:5555");

    console.log("Servidor Node.js rodando na porta 5555...");

    for await (const [msg] of sock) {
        const mensagem = msg.toString();
        console.log("Recebido:", mensagem);

        const [opcaoStr, payload] = mensagem.split("|");
        const opcao = parseInt(opcaoStr);

        let resposta = "";

        switch (opcao) {

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

        if (funcao === "raiz") {
            const x = parseFloat(partes[1]);
            return `raiz(${x}) = ${Math.sqrt(x)}`;
        }

        if (funcao === "dobro") {
            const x = parseFloat(partes[1]);
            return `dobro(${x}) = ${2 * x}`;
        }

        return "[Erro] Funcao desconhecida";

    } catch {
        return "[Erro] Falha no cálculo";
    }
}

iniciarServidor();
