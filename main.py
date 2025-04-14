from polinomio import Polinômio
from newton import metodo_newton
from bisseccao import metodo_bissecao
from secantes import metodo_secantes
#Função de interesse
#f(x) = 3x⁵-7x⁴-3x³+7x²-6x+14
funcao = Polinômio((14,-6,7,-3,-7,3))
#Intervalos de interesse I₁ = [-2,-1] e I₂ = [1,2]
#como f(-2)*f(-1) < 0 e f(1)*f(2)<0, pelo teorema do valor intermediário, existem x₁ ∈ I₁ e x₂ ∈ I₂ tais que f(x₁)=f(x₂)=0
#Raizes de f(x)=0: -√2, √2 e 7/3
SQRT2 = 2**(1/2) #Constante √2
#Derivada de f(x): f'(x) = 15x⁴-28x³-9x²+14x-6
derivada = funcao.derivada()
#Precisão definida a priori por ε = 10ˉ⁶
precisao = 10**-6


#Aplica o Método de Newton no intervalo I₁ = [-2,-1], primeira aproximação x₀ = -1.5
metodo_newton(-2,funcao.f,derivada.f,precisao,-SQRT2,1)
#Aplica o Método de Newton no intervalo I₂ = [1,2], primeira aproximação x₀ = 1.5
metodo_newton(1,funcao.f,derivada.f,precisao,SQRT2,2)

#Aplica o Método das Secantes no intervalo I₁ = [-2,-1]
metodo_secantes((-2,-1),funcao.f,precisao,-SQRT2,2)
#Aplica o Método das Secantes no intervalo I₂ = [1,2]
metodo_secantes((1,2),funcao.f,precisao,SQRT2,1)

#Aplica o Método da Bissecção no intervalo I₁ = [-2,-1]
metodo_bissecao(-2,-1,funcao.f,precisao,-SQRT2,1)
#Aplica o Método da Bissecção no intervalo I₂ = [1,2]
metodo_bissecao(1,2,funcao.f,precisao,SQRT2,2)
