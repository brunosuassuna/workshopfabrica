from abc import ABC, abstractmethod

class IAnimal:

    @abstractmethod
    def falar(self):
        """Defina na classe filha"""

    @abstractmethod
    def andar (self):
        """Defina na classe filha"""

class Cachorro(IAnimal):
    def falar(self):
        print("AuAu")

    def andar(self):
        print("Ando com 4 patas")

class Pessoa: 
    
    def __init__(self, nome: str, idade: int):
        self._nome = nome
        self.idade = idade
        self.humano = True

    def fala_pessoa(self):
        print("falando")

pingo = Cachorro()
pingo.falar()
pingo.andar()










