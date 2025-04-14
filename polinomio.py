#Código criado por:
#Antonio Augusto Nunes de Souza N°USP 15440698

#Implementação da classe Polinomio
class Polinômio:
    def __init__(self,termos:tuple):
        '''Coloque os termos em ordem crescente, isto é, começa do termo de grau 0.'''
        self.termos = termos
        self.grau = len(termos) - 1
    def f(self,x:float):
        '''Retorna o valor do polinomio no ponto x'''
        fx = 0
        for i in reversed(range(self.grau+1)):
            xn = self.termos[i]*x**i
            fx += xn
        return float(fx)
    def derivada(self):
        '''Retorna um Polinomio novo, o qual é derivada deste.'''
        termos_novos = []
        for n in range(1,self.grau+1):
            termos_novos.append(n*self.termos[n])
        termos_tupla = tuple(termos_novos)
        return Polinômio(termos_tupla)


