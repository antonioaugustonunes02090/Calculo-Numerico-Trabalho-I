#Código criado por:
#Antonio Augusto Nunes de Souza

#Iteração do Método de Newton
def newton(x_k:float, funcao, derivada, precisao:float,valor_exato:float,k=0,parada=False):
    assert derivada(x_k)!=0
    x = x_k - funcao(x_k)/derivada(x_k)
    #O processo de parada não pode depender da raíz
    if funcao(x) == 0 or abs(x-x_k) < precisao*max(1,x_k):
        parada = True
    return {'k':k,'x_k':x_k,'f(x_k)':funcao(x_k),"f'(x_k)":derivada(x_k),'e':abs(valor_exato-x_k),'parada':parada} if k==0 else {'k':k,'x_k':x,'f(x_k)':funcao(x),"f'(x_k)":derivada(x),'e':abs(valor_exato-x),'parada':parada}

#Função para formatar o topo da tabela do arquivo de texto de saída
def write_top_newton(file):
    file.write(f'| k |'+' '*4+'x_k'+' '*5+'|'+' '*4+'f(x_k)'+' '*3+'|'+' '*3+"f'(x_k)"+' '*3+'|'+' '*4+'e_k'+' '*4+'|\n')
    file.write('='*58+'\n')

#função para escrever cada iteração no arquivo de texto de saída
def write_data_newton(file,k,x,fx,f_x,e):
    #arrendondar para 8 casas decimais
    x,fx,f_x,e = round(x,8),round(fx,8),round(f_x,8),round(e,8)
    file.write(f'|{k:03}|'+f'{x:=12.9f}|'+f'{fx:=13.8f}|'+f'{f_x:=13.8f}|'+f'{e:.9f}|\n')

#Aplica o método iterativo linear e gera o arquivo de saída
def metodo_newton(x_k:float,funcao,derivada,precisao:float,valor_exato:float,n_raiz:int):
    k=0
    file = open(f'newton_saida{n_raiz}.txt','w')
    write_top_newton(file)
    while True:
        data = newton(x_k,funcao,derivada,precisao,valor_exato,k)
        write_data_newton(file,data['k'],data['x_k'],data['f(x_k)'],data["f'(x_k)"],data['e'])
        if data['parada']:
            break
        else:
            k+=1
            x_k = data['x_k']
    file.close()
