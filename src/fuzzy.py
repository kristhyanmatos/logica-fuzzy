import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
from matplotlib import pyplot as pl

# Cria as variáveis do problema
comida = ctrl.Antecedent(np.arange(0, 11, 1), "comida")
servico = ctrl.Antecedent(np.arange(0, 11, 1), "servico")
gorjeta = ctrl.Consequent(np.arange(0, 26, 1), "gorjeta")

# Cria automaticamente o mapeamento entre valores nítidos e difusos
# usando uma função de pertinência padrão (triângulo)
comida.automf(names=["péssima", "comível", "deliciosa"])


# Cria as funções de pertinência usando tipos variados
servico["ruim"] = fuzz.trimf(servico.universe, [0, 0, 5])
servico["aceitável"] = fuzz.gaussmf(servico.universe, 5, 2)
servico["excelente"] = fuzz.gaussmf(servico.universe, 10, 3)

gorjeta["baixa"] = fuzz.trimf(gorjeta.universe, [0, 0, 13])
gorjeta["média"] = fuzz.trapmf(gorjeta.universe, [0, 13, 15, 25])
gorjeta["alta"] = fuzz.trimf(gorjeta.universe, [15, 25, 25])

## comida.view()
## servico.view()
## gorjeta.view()

rule1 = ctrl.Rule(servico["excelente"] | comida["deliciosa"], gorjeta["alta"])
rule2 = ctrl.Rule(servico["aceitável"], gorjeta["média"])
rule3 = ctrl.Rule(servico["ruim"] & comida["péssima"], gorjeta["baixa"])

gorjeta_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
gorjeta_simulador = ctrl.ControlSystemSimulation(gorjeta_ctrl)


def aptidao(
    tempo_carreira,
    complexidade,
    projetos_realizados,
):
    # Entrando com alguns valores para qualidade da comida e do serviço
    gorjeta_simulador.input["comida"] = tempo_carreira
    gorjeta_simulador.input["servico"] = tempo_carreira

    # Computando o resultado
    gorjeta_simulador.compute()
    print(gorjeta_simulador.output["gorjeta"])
    return gorjeta_simulador.output["gorjeta"]

    ## comida.view(sim=gorjeta_simulador)
    ## servico.view(sim=gorjeta_simulador)
    ## gorjeta.view(sim=gorjeta_simulador)
    ##
    ## pl.show()
