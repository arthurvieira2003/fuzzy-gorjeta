# Sistema de Cálculo de Gorjeta com Lógica Fuzzy

Este projeto implementa um sistema de cálculo de gorjeta utilizando lógica fuzzy. O sistema leva em consideração três fatores para determinar o percentual de gorjeta recomendado: qualidade da refeição, qualidade do serviço e tempo de atendimento.

## Como funciona

O sistema utiliza a biblioteca scikit-fuzzy para implementar a lógica fuzzy. Ele define três variáveis de entrada (antecedentes) e uma variável de saída (consequente):

1. Qualidade da refeição (0-10)
2. Qualidade do serviço (0-10)
3. Tempo de atendimento (0-10, onde 0 é muito rápido e 10 é muito demorado)
4. Gorjeta (0-25%)

Cada variável é dividida em conjuntos fuzzy, e um conjunto de regras é definido para determinar o percentual de gorjeta com base nas entradas.

## Requisitos

Para executar este projeto, você precisará das seguintes bibliotecas Python:

- scikit-fuzzy
- numpy
- matplotlib
- pandas

Você pode instalar estas dependências usando pip:

```bash
pip install -r requirements.txt
```

## Como usar

1. Clone este repositório para sua máquina local.
2. Instale as dependências conforme mencionado acima.
3. Execute o arquivo `app.py`:

```bash
python app.py
```

4. O programa solicitará que você insira valores para:

   - Qualidade da refeição (0-10)
   - Qualidade do serviço (0-10)
   - Tempo de atendimento (0-10, onde 0 é muito rápido e 10 é muito demorado)

5. Após inserir os valores, o programa calculará e exibirá o percentual de gorjeta recomendado.

## Estrutura do código

O código principal está no arquivo `app.py`. Ele define as variáveis fuzzy, as regras e a função para calcular a gorjeta. As principais partes do código são:

1. Definição das variáveis antecedentes e consequente (linhas 5-9)
2. Definição dos conjuntos fuzzy para cada variável (linhas 11-24)
3. Definição das regras fuzzy (linhas 27-31)
4. Criação do sistema de controle e simulação (linhas 33-34)
5. Função para calcular a gorjeta (linhas 36-45)
6. Código principal para interação com o usuário (linhas 47-53)
