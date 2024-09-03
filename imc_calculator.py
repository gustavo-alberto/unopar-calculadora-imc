# Calculadora de IMC para o projeto de atividade prática da disciplina de linguagem de programação.
# O IMC é calculado dividindo o peso (em kg) pela altura ao quadrado (em metros)
# de acordo com a seguinte fórmula: IMC = peso / (altura x altura).
# O resultado de IMC é dado em kg/m2.
# Depois de obter o resultado de IMC, deve-se interpretar o valor utilizando a seguinte tabela:
#  _____________________________________ 
# |      IMC       |    Classificação   |
# |----------------|--------------------|
# | Menor que 18,5 | Magreza            |
# | 18,5 a 24,9    | Normal             |
# | 25 a 29,9      | Sobrepeso          |
# | 30 a 34,9      | Obesidade grau I   |
# | 35 a 39,9      | Obesidade grau II  |
# | Maior que 40   | Obesidade grau III |

def main():
    """Função principal. 
    Solicita ao usuário seu peso e altura e retorna uma mensagem com as informação calculadas
    """

    print("############################")
    print("#### Calculadora de IMC ####")
    print("############################")

    peso = parse_value("Digite seu peso em kg (Ex: 70.5): ")
    altura = parse_value("Digite sua altura em metros (Ex: 1.69): ")

    imc = calculate_imc(peso, altura)
    classification = classify_imc(imc)

    print(f'Seu IMC é de {imc}. Sua classificação é: {classification}')


def parse_value(prompt: str) -> float:
    """Solicita ao usuário um valor até que seja fornecido um valor válido.

    Parâmetros:
        prompt(str): mensagem a ser exibida para o usuário.
    
    Retorna:
        parsed_value(float): valor convertido.
    """
    while True:
        value = input(prompt)
        try:
            parsed_value = float(value)
            return parsed_value
        except ValueError:
            print('Entrada inválida. Por favor, insira um número válido.')

def calculate_imc(peso: float, altura: float) -> float:
    """Retorna o valor do IMC.

    Parâmetros:
        peso(float): peso do usuário em kg
        altura(int): altura do usuário em metros

    Retorna:
        imc(float): valor do IMC calculado
    """
    return round(peso / (altura * altura), 2)

def classify_imc(imc: float) -> str:
    """ Retorna a classificação do IMC informado

    Parâmetros:
        imc(float): imc calculado
    
    Retorna:
        classification(str): Classificação do IMC calculado
    """
    if imc < 18.5:
        return 'Magreza'
    elif imc > 18.5 and imc < 24.9:
        return 'Normal'
    elif imc > 25 and imc < 29.9:
        return 'Sobrepeso'
    elif imc > 30 and imc < 34.9:
        return 'Obesidade grau I'
    elif imc > 35 and imc < 39.9:
        return 'Obesidade grau II'
    elif imc > 40:
        return 'Obesidade grau III'

if __name__ == "__main__":
    # Executa a função principal
    main()