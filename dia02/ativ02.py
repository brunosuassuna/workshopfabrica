nume = input("Digite um número")
antecessor = 0
sucessor = 0

try:
    sucessor = 1 + int(nume) 
    antecessor = int(nume)  - 1 
except ValueError:
    raise ValueError ("Digite um número valido")

print(f"O antecessor do número {nume} é {antecessor} e o sucessor {sucessor}")

print(type(nume))
print(type(antecessor))
print(type(sucessor))