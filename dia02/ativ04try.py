velocidade = input("Qual velocidade que estava o veiculo?")
velocidade_em_int = 0
try:    
    velocidade_em_int = float(velocidade)
except ValueError:
    raise ValueError ("Digite a velocidade em numeros.")
if velocidade_em_int > 80:
    print("Você ultrapassou a velocidade permitida de 80km/h.")
    print("Sua multa é de: ", (velocidade_em_int - 80) * 7,"R$")
else:
    print("Pode continuar, você não foi multado")