from db import DEVS
from fuzzy import calula_aptidao

input_complexidade = int(input("insira a complexidade: "))
input_linguagens = input("insira as linguagens: ")
input_linguagens = input_linguagens.split(",")
print("complexidade: " + str(input_complexidade))
print("linguagens: " + str(input_linguagens))

aptidao_linguagens = []
# Criar base de aptidao de linguagens
for linguagem in input_linguagens:
    aptidao_linguagens.append(
        {
            "nome": linguagem,
            "devs_aptidao": [],
        }
    )

for dev in DEVS:
    # buscar a linguagem
    for linguagen in dev["linguagens"]:
        if linguagen["nome"] in (input_linguagens):
            ##
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
print(aptidao_linguagens)
