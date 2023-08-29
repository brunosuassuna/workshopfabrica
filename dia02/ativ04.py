velocidade = float(input("Qual é a velocidade do veiculo?"))
if velocidade > 80:
    print ("Você passou do limite de velocidade permitido, que é de 80km!")
    print("Sua multa é de:" ,(velocidade - 80) * 7, "R$")
else:
    print("Você está dentro do limite de velocidade!")