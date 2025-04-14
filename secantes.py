#Código criado por:
#Antonio Augusto Nunes de Souza N°USP 15440698  

#Iteração do Método das Secantes
def secantes(x_1:float, x_0:float, funcao, precisao:float,valor_exato:float,k=0,parada=False):
    x = (x_0*funcao(x_1)-x_1*funcao(x_0))/(funcao(x_1)-funcao(x_0))
    #O processo de parada não pode depender da raíz
    if funcao(x) == 0 or abs(x-x_1) < precisao*max(1,x_1):
        parada = True
    return {'k':k,'x_1':x, 'x_0':x_1, 'f(x_1)':funcao(x),'e':abs(valor_exato-x),'parada':parada}

#Função para formatar o topo da tabela do arquivo de texto de saída
def write_top_secantes(file,x_0,x_1,funcao,valor_exato):
    file.write(f'| k |'+' '*4+'x_k'+' '*5+'|'+' '*4+'f(x_k)'+' '*3+'|'+' '*4+'e_k'+' '*3+'|\n')
    file.write('='*43+'\n')
    #Escrever as duas aproximações iniciais
    file.write(f'|000|'+f'{x_0:=12.9f}|'+f'{funcao(x_0):=13.8f}|'+f'{abs(valor_exato-x_0):.8f}|\n')
    file.write(f'|001|'+f'{x_1:=12.9f}|'+f'{funcao(x_1):=13.8f}|'+f'{abs(valor_exato-x_1):.8f}|\n')

#função para escrever cada iteração no arquivo de texto de saída
def write_data_secantes(file,k,x,fx,e):
    #arrendondar para 8 casas decimais
    x,fx,e = round(x,8),round(fx,8),round(e,8)
    file.write(f'|{k:03}|'+f'{x:=12.9f}|'+f'{fx:=13.8f}|'+f'{e:.8f}|\n')

#Aplica o método iterativo e gera o arquivo de saída
def metodo_secantes(xs:tuple,funcao,precisao:float,valor_exato:float,n_raiz:int):
    k=2
    file = open(rf'secantes\secantes_saida{n_raiz}.txt','w')
    write_top_secantes(file,xs[0],xs[1],funcao,valor_exato)
    while True:
        data = secantes(xs[1],xs[0],funcao,precisao,valor_exato,k)
        write_data_secantes(file,data['k'],data['x_1'],data['f(x_1)'],data['e'])
        if data['parada']:
            break
        else:
            k+=1
            xs = (data['x_0'],data['x_1'])
        if k==100:
            break
    file.close()



