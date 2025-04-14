#Código criado por:
#Antonio Augusto Nunes de Souza

#Iteração do Método da Bissecção
def bissecao(a:float,b:float,funcao,precisao:float,valor_exato:float,x_anterior:float,k=0,parada=False):
    assert funcao(a) * funcao(b) < 0 and a < b
    x = (a+b)/2
    e = abs(valor_exato-x)
    #O processo de parada não pode depender da raíz
    if funcao(x)==0 or abs(b-a) < precisao*max(1,x_anterior):
        parada = True
    return {'k':k,'a':a,'b':b,'x':x,'f(x)':funcao(x),'e':e,'parada':parada}

#Função para formatar o topo da tabela do arquivo de texto de saída
def write_top_bissecao(file):
    file.write(f'| k |'+' '*6+'a'+' '*5+'|'+' '*5+'b'+' '*6+'|'+' '*4+'x_k'+' '*5+'|'+' '*4+'f(x)'+' '*3+'|'+' '*4+'e_k'+' '*3+'|\n')
    file.write('='*68+'\n')

#função para escrever cada iteração no arquivo de texto de saída
def write_data_bissecao(file,k,a,b,x,f_x,e):
    #arrendondar para 8 casas decimais
    a,b,x,f_x,e = round(a,8),round(b,8),round(x,8),round(f_x,8),round(e,8)
    file.write(f'|{k:03}|'+f'{a:=12.9f}|'+f'{b:=12.9f}|'+f'{x:=12.9f}|'+f'{f_x:=11.8f}|'+f'{e:=11.8f}|\n')

#Aplica o método iterativo e gera o arquivo de saída
def metodo_bissecao(a:float,b:float,funcao,precisao:float,valor_exato:float,n_raiz:int):
    k=0
    x_anterior = 0
    file = open(rf'bisseccao\bissecao_saida{n_raiz}.txt','w')
    write_top_bissecao(file)
    while True:
        data = bissecao(a,b,funcao,precisao,valor_exato,x_anterior,k)
        write_data_bissecao(file,data['k'],data['a'],data['b'],data['x'],data['f(x)'],data['e'])
        x_anterior = data['x']
        if data['parada']:
            break
        else:
            k+=1
            if funcao(data['a'])*funcao(data['x'])<0:
                b = data['x']
            else:
                a = data['x']
    file.close()
