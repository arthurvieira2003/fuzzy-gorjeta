import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

qualidade_refeicao = ctrl.Antecedent(np.arange(0, 11, 1), 'qualidade_refeicao')
qualidade_servico = ctrl.Antecedent(np.arange(0, 11, 1), 'qualidade_servico')
tempo_atendimento = ctrl.Antecedent(np.arange(0, 11, 1), 'tempo_atendimento')

gorjeta = ctrl.Consequent(np.arange(0, 26, 1), 'gorjeta')

qualidade_refeicao['insossa'] = fuzz.trimf(qualidade_refeicao.universe, [0, 0, 5])
qualidade_refeicao['regular'] = fuzz.trimf(qualidade_refeicao.universe, [0, 5, 10])
qualidade_refeicao['saborosa'] = fuzz.trimf(qualidade_refeicao.universe, [5, 10, 10])

qualidade_servico['ruim'] = fuzz.trimf(qualidade_servico.universe, [0, 0, 5])
qualidade_servico['regular'] = fuzz.trimf(qualidade_servico.universe, [0, 5, 10])
qualidade_servico['excelente'] = fuzz.trimf(qualidade_servico.universe, [5, 10, 10])

tempo_atendimento['rapido'] = fuzz.trimf(tempo_atendimento.universe, [0, 0, 5])
tempo_atendimento['medio'] = fuzz.trimf(tempo_atendimento.universe, [0, 5, 10])
tempo_atendimento['demorado'] = fuzz.trimf(tempo_atendimento.universe, [5, 10, 10])

gorjeta['baixa'] = fuzz.trimf(gorjeta.universe, [0, 0, 13])
gorjeta['media'] = fuzz.trimf(gorjeta.universe, [0, 13, 25])
gorjeta['alta'] = fuzz.trimf(gorjeta.universe, [13, 25, 25])

regra1 = ctrl.Rule(qualidade_refeicao['insossa'] | qualidade_servico['ruim'] | tempo_atendimento['demorado'], gorjeta['baixa'])
regra2 = ctrl.Rule(qualidade_refeicao['saborosa'] & qualidade_servico['excelente'] & tempo_atendimento['rapido'], gorjeta['alta'])
regra3 = ctrl.Rule(qualidade_refeicao['regular'] | qualidade_servico['regular'] | tempo_atendimento['medio'], gorjeta['media'])
regra4 = ctrl.Rule(qualidade_refeicao['saborosa'] & qualidade_servico['excelente'] & ~tempo_atendimento['rapido'], gorjeta['media'])
regra5 = ctrl.Rule(qualidade_refeicao['saborosa'] | qualidade_servico['excelente'] | tempo_atendimento['rapido'], gorjeta['alta'])

sistema_gorjeta = ctrl.ControlSystem([regra1, regra2, regra3, regra4, regra5])
simulacao = ctrl.ControlSystemSimulation(sistema_gorjeta)

def calcular_gorjeta(qualidade_refeicao, qualidade_servico, tempo_atendimento):
    simulacao.input['qualidade_refeicao'] = qualidade_refeicao
    simulacao.input['qualidade_servico'] = qualidade_servico
    simulacao.input['tempo_atendimento'] = tempo_atendimento
    try:
        simulacao.compute()
        return simulacao.output['gorjeta']
    except:
        print("Erro ao calcular a gorjeta. Usando valor padrão.")
        return 15

if __name__ == "__main__":
    qualidade_refeicao = float(input("Qualidade da refeição (0-10): "))
    qualidade_servico = float(input("Qualidade do serviço (0-10): "))
    tempo_atendimento = float(input("Tempo de atendimento (0-10, onde 0 é muito rápido e 10 é muito demorado): "))

    gorjeta = calcular_gorjeta(qualidade_refeicao, qualidade_servico, tempo_atendimento)
    print(f"Percentual de gorjeta recomendado: {gorjeta:.2f}%")