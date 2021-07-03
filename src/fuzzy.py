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
tempo_carreira["junior"] = fuzz.gaussmf(tempo_carreira.universe, 2, 1.5)
tempo_carreira["pleno"] = fuzz.gaussmf(tempo_carreira.universe, 7, 1.5)
tempo_carreira["senior"] = fuzz.gaussmf(tempo_carreira.universe, 20, 5)

projetos_realizados["junior"] = fuzz.trimf(projetos_realizados.universe, [0, 0, 2])
projetos_realizados["pleno"] = fuzz.trapmf(projetos_realizados.universe, [2, 4, 9, 10])
projetos_realizados["senior"] = fuzz.trimf(projetos_realizados.universe, [6, 15, 90])


complexidade["baixa"] = fuzz.trimf(complexidade.universe, [0, 0, 3])
complexidade["média"] = fuzz.trapmf(complexidade.universe, [1, 3, 6, 8])
complexidade["alta"] = fuzz.trimf(complexidade.universe, [6, 9, 16])

aptidao.automf(names=["Júnior", "Pleno", "Sênior"])

tempo_carreira.view()
projetos_realizados.view()
complexidade.view()
aptidao.view()
pl.show()

# rule1 = ctrl.Rule(servico["excelente"] | comida["deliciosa"], aptidao["alta"])
# rule2 = ctrl.Rule(servico["aceitável"], aptidao["média"])
# rule3 = ctrl.Rule(servico["ruim"] & comida["péssima"], aptidao["baixa"])

# aptidao = ctrl.ControlSystem([rule1, rule2, rule3])
# aptidao = ctrl.ControlSystemSimulation(aptidao)


## def calula_aptidao(
##     tempo_carreira,
##     complexidade,
##     projetos_realizados,
## ):
##     # Entrando com alguns valores para qualidade da comida e do serviço
##     aptidao.input["comida"] = tempo_carreira
##     aptidao.input["servico"] = tempo_carreira
##
##     # Computando o resultado
##     aptidao.compute()
##     print(aptidao.output["aptidao"])
##     return aptidao.output["aptidao"]
##
##     ## comida.view(sim=aptidao)
##     ## servico.view(sim=aptidao)
##     ## aptidao.view(sim=aptidao)
##     ##
##     ## pl.show()
