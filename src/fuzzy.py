import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
from matplotlib import pyplot as pl

# Cria as variáveis do problema
tempo_carreira = ctrl.Antecedent(np.arange(0, 51, 1), "tempo_carreira")
projetos_realizados = ctrl.Antecedent(np.arange(0, 91, 1), "projetos_realizados")
complexidade = ctrl.Antecedent(np.arange(0, 10, 1), "complexidade")
aptidao = ctrl.Consequent(np.arange(0, 11, 1), "aptidao")


# Cria as funções de pertinência
tempo_carreira["Júnior"] = fuzz.gaussmf(tempo_carreira.universe, 2, 1.5)
tempo_carreira["Pleno"] = fuzz.gaussmf(tempo_carreira.universe, 7, 1.5)
tempo_carreira["Sênior"] = fuzz.gaussmf(tempo_carreira.universe, 20, 5)

projetos_realizados["Júnior"] = fuzz.trimf(projetos_realizados.universe, [0, 0, 2])
projetos_realizados["Pleno"] = fuzz.trapmf(projetos_realizados.universe, [2, 4, 9, 10])
projetos_realizados["Sênior"] = fuzz.trimf(projetos_realizados.universe, [6, 15, 90])


complexidade["Júnior"] = fuzz.trimf(complexidade.universe, [0, 0, 3])
complexidade["Pleno"] = fuzz.trapmf(complexidade.universe, [1, 3, 6, 8])
complexidade["Sênior"] = fuzz.trimf(complexidade.universe, [6, 9, 16])

aptidao.automf(names=["Júnior", "Pleno", "Sênior"])

# tempo_carreira.view()
# projetos_realizados.view()
# complexidade.view()
# aptidao.view()
# pl.show()

# Regras
regra1 = ctrl.Rule(
    tempo_carreira["Júnior"] & projetos_realizados["Júnior"] & complexidade["Júnior"],
    aptidao["Pleno"],
)
regra2 = ctrl.Rule(
    tempo_carreira["Júnior"] & projetos_realizados["Júnior"] & complexidade["Pleno"],
    aptidao["Júnior"],
)
regra3 = ctrl.Rule(
    tempo_carreira["Júnior"] & projetos_realizados["Júnior"] & complexidade["Sênior"],
    aptidao["Júnior"],
)
regra4 = ctrl.Rule(
    tempo_carreira["Júnior"] & projetos_realizados["Pleno"] & complexidade["Júnior"],
    aptidao["Sênior"],
)
regra5 = ctrl.Rule(
    tempo_carreira["Júnior"] & projetos_realizados["Pleno"] & complexidade["Pleno"],
    aptidao["Pleno"],
)
regra6 = ctrl.Rule(
    tempo_carreira["Júnior"] & projetos_realizados["Pleno"] & complexidade["Sênior"],
    aptidao["Pleno"],
)
regra7 = ctrl.Rule(
    tempo_carreira["Júnior"] & projetos_realizados["Sênior"] & complexidade["Júnior"],
    aptidao["Sênior"],
)
regra8 = ctrl.Rule(
    tempo_carreira["Júnior"] & projetos_realizados["Sênior"] & complexidade["Pleno"],
    aptidao["Sênior"],
)
regra9 = ctrl.Rule(
    tempo_carreira["Júnior"] & projetos_realizados["Sênior"] & complexidade["Sênior"],
    aptidao["Pleno"],
)
regra10 = ctrl.Rule(
    tempo_carreira["Pleno"] & projetos_realizados["Júnior"] & complexidade["Júnior"],
    aptidao["Pleno"],
)
regra11 = ctrl.Rule(
    tempo_carreira["Pleno"] & projetos_realizados["Júnior"] & complexidade["Pleno"],
    aptidao["Júnior"],
)
regra12 = ctrl.Rule(
    tempo_carreira["Pleno"] & projetos_realizados["Júnior"] & complexidade["Sênior"],
    aptidao["Júnior"],
)
regra13 = ctrl.Rule(
    tempo_carreira["Pleno"] & projetos_realizados["Pleno"] & complexidade["Júnior"],
    aptidao["Sênior"],
)
regra14 = ctrl.Rule(
    tempo_carreira["Pleno"] & projetos_realizados["Pleno"] & complexidade["Pleno"],
    aptidao["Pleno"],
)
regra15 = ctrl.Rule(
    tempo_carreira["Pleno"] & projetos_realizados["Pleno"] & complexidade["Sênior"],
    aptidao["Pleno"],
)
regra16 = ctrl.Rule(
    tempo_carreira["Pleno"] & projetos_realizados["Sênior"] & complexidade["Júnior"],
    aptidao["Sênior"],
)
regra17 = ctrl.Rule(
    tempo_carreira["Pleno"] & projetos_realizados["Sênior"] & complexidade["Pleno"],
    aptidao["Sênior"],
)
regra18 = ctrl.Rule(
    tempo_carreira["Pleno"] & projetos_realizados["Sênior"] & complexidade["Sênior"],
    aptidao["Pleno"],
)
regra19 = ctrl.Rule(
    tempo_carreira["Sênior"] & projetos_realizados["Júnior"] & complexidade["Júnior"],
    aptidao["Pleno"],
)
regra20 = ctrl.Rule(
    tempo_carreira["Sênior"] & projetos_realizados["Júnior"] & complexidade["Pleno"],
    aptidao["Júnior"],
)
regra21 = ctrl.Rule(
    tempo_carreira["Sênior"] & projetos_realizados["Júnior"] & complexidade["Sênior"],
    aptidao["Júnior"],
)
regra22 = ctrl.Rule(
    tempo_carreira["Sênior"] & projetos_realizados["Pleno"] & complexidade["Júnior"],
    aptidao["Pleno"],
)
regra23 = ctrl.Rule(
    tempo_carreira["Sênior"] & projetos_realizados["Pleno"] & complexidade["Pleno"],
    aptidao["Pleno"],
)
regra24 = ctrl.Rule(
    tempo_carreira["Sênior"] & projetos_realizados["Pleno"] & complexidade["Sênior"],
    aptidao["Pleno"],
)
regra25 = ctrl.Rule(
    tempo_carreira["Sênior"] & projetos_realizados["Sênior"] & complexidade["Júnior"],
    aptidao["Sênior"],
)
regra26 = ctrl.Rule(
    tempo_carreira["Sênior"] & projetos_realizados["Sênior"] & complexidade["Pleno"],
    aptidao["Sênior"],
)
regra27 = ctrl.Rule(
    tempo_carreira["Sênior"] & projetos_realizados["Sênior"] & complexidade["Sênior"],
    aptidao["Sênior"],
)
regra28 = ctrl.Rule(
    projetos_realizados["Júnior"] | tempo_carreira["Júnior"],
    aptidao["Júnior"],
)
regra29 = ctrl.Rule(
    projetos_realizados["Pleno"] | tempo_carreira["Pleno"],
    aptidao["Pleno"],
)
regra30 = ctrl.Rule(
    projetos_realizados["Sênior"] | tempo_carreira["Sênior"],
    aptidao["Sênior"],
)
regra31 = ctrl.Rule(
    projetos_realizados["Júnior"] & complexidade["Júnior"],
    aptidao["Júnior"],
)
regra32 = ctrl.Rule(
    projetos_realizados["Pleno"] & complexidade["Pleno"],
    aptidao["Pleno"],
)
regra33 = ctrl.Rule(
    projetos_realizados["Sênior"] & complexidade["Sênior"],
    aptidao["Sênior"],
)

aptidao_regras = ctrl.ControlSystem(
    [
        regra1,
        regra2,
        regra3,
        regra4,
        regra5,
        regra6,
        regra7,
        regra8,
        regra9,
        regra10,
        regra11,
        regra12,
        regra13,
        regra14,
        regra15,
        regra16,
        regra17,
        regra18,
        regra19,
        regra20,
        regra21,
        regra22,
        regra23,
        regra24,
        regra25,
        regra26,
        regra27,
        regra28,
        regra29,
        regra30,
        regra31,
        regra32,
        regra33,
    ]
)
aptidao_simulatior = ctrl.ControlSystemSimulation(aptidao_regras)


def calula_aptidao(
    tempo_carreira_input,
    complexidade_input,
    projetos_realizados_input,
):
    # Inserindo valores
    aptidao_simulatior.input["tempo_carreira"] = tempo_carreira_input
    aptidao_simulatior.input["complexidade"] = complexidade_input
    aptidao_simulatior.input["projetos_realizados"] = projetos_realizados_input

    # Computando o resultado
    aptidao_simulatior.compute()
    print(aptidao_simulatior.output["aptidao"])
    # aptidao.view(sim=aptidao_simulatior)
    # pl.show()
    return aptidao_simulatior.output["aptidao"]
