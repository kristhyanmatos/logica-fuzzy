from db import DEVS
from utils import busca_chave
from fuzzy import calula_aptidao

input_complexidade = int(input("insira a complexidade: "))
input_linguagens = input("insira as linguagens: ")
input_linguagens = input_linguagens.split(",")

aptidao_linguagens = []
for linguagem in input_linguagens:
    aptidao_linguagens.append(
        {
            "nome": linguagem,
            "devs_aptidao": [],
        }
    )

for dev in DEVS:
    for linguagen in dev["linguagens"]:
        if linguagen["nome"] in (input_linguagens):
            for index, aptidao_linguagem in enumerate(aptidao_linguagens):
                if aptidao_linguagem["nome"] == linguagen["nome"]:
                    aptidao_linguagens[index]["devs_aptidao"].append(
                        {
                            "nome": dev["nome"],
                            "aptidao": calula_aptidao(
                                dev["tempo_carreira"],
                                input_complexidade,
                                linguagen["projetos_realizados"],
                            ),
                        }
                    )

for linguagem in aptidao_linguagens:
    linguagem["devs_aptidao"].sort(key=busca_chave)

print(aptidao_linguagens)
