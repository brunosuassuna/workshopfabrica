idade = input("digite sua idade")
idade_em_int = 0
try:
    idade_em_int = int(idade)
except ValueError:
    raise ValueError("Digite a idade em numeros")


if idade_em_int >= 18:
    print("pode tirar a CNH")
else:
    print("Não pode tirar a CNH")