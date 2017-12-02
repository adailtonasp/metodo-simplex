#File name: simplex.py
#Autor: Luis Carlos <luiscarlos.sf@outlook.com>
 #import numpy as np
"""
    O método Simplex compreende os seguintes passos:
    0 - Colocar o PPL na forma padrão
    1 - Achar uma solução viável básica inicial
    2 - Verificar se a solução atual é ótima, se for PARE
        Caso contrário, vá para o passo 3
    3 - Determinar a variável não básica que deve entrar na base
    4 - Determinar a variável básica que deve sair da base
    5 - Achar a nova solução viável básica e voltar ao passo 2

"""
def cria_matriz(m , n):

    restricoes = list()
    for i in range(m):
        restricoes.append([0]*n)
    return restricoes

"""
    funcao_objetivo : [x1, x2, x3, ...]
    restricoes : [["<= ou >= ou = ",x1, x2, x3, ..., b1],["<= ou >= ou = ", x1, x2, x3, ..., b2], ...]
"""
def forma_padrao(funcao_objetivo, restricoes):

    m = len(restricoes)
    for i in range(len(funcao_objetivo)):
        #Variável sem restrição de sinal
        if restricoes[m-1][i+1] == "free":
            funcao_objetivo[i]=(1* funcao_objetivo[i], -1* funcao_objetivo[i])
            for j in range(m):
                restricoes[j][i+1]=(1* restricoes[j][i+1], -1* restricoes[j][i+1])
            restricoes[j][i + 1] = (">=",">=")
        #Variável com restrição negativa
        elif restricoes[m-1][i+1] == "<=":
            funcao_objetivo[i] = -1 * funcao_objetivo[i]
            for j in range(m):
                restricoes[i][j]= -1 * funcao_objetivo[i]


    for i in range(m-1):
        n = len(restricoes[i])-2
        #Menor ou igual
        if restricoes[i][0] == "<=":
            restricoes[i][0] = "=";
            restricoes[i].insert(n+1, 1)
            for k in range(m-1):
                if k != i:
                    restricoes[k].insert(n+1, 0)
        #Maior ou igual
        elif restricoes[i][0] == ">=":
            restricoes[i][0] = "=";
            restricoes[i].insert(n+1, -1)
            for k in range(m-1):
                if k != i:
                    restricoes[k].insert(n+1, 0)
        #Lado Direito negativo
        print(restricoes[i][len(restricoes[i])-1])
        if restricoes[i][len(restricoes[i])-1] < 0:
            for j in range(1,len(restricoes[i])):
                #CORRIGE ERRO PARA TUPLAR
                restricoes[i][j] *= -1;
                print("After", restricoes[i][j])


if __name__=="__main__":
    funcao_objetivo = [1,1,1,7]
    restricoes = [[">=",3,1,0,1,20], ["=",1,5,-1,0,-8],[">=",2,3,4,5,31], [0, ">=", "free", ">=",">="]]

    #Exibindo o PPL na forma padrão
    forma_padrao(funcao_objetivo, restricoes)
    funcao= "MAX Z = "
    for i in range(len(funcao_objetivo)):
        if i+1 == len(funcao_objetivo):
            funcao += str(funcao_objetivo[i]) + 'X' + str(i + 1)
        else:
            funcao += str(funcao_objetivo[i])+'X'+ str(i+1)+" + "
    print(funcao)
    print("Restrições: ")
    for i in range(len(restricoes)-1):
        string = ""
        for j in range(1,len(restricoes[i])):
                if j + 1 == len(restricoes[i]):
                    string += str(restricoes[i][j])
                elif j + 2 == len(restricoes[i]):
                    string += str(restricoes[i][j]) + 'X' + str(j)+ " ="
                else:
                    string += str(restricoes[i][j])+'X'+ str(j)+ "  +"
        print(string)


