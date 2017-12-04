#File name: simplex.py
#Author: Luis Carlos <luiscarlos.sf@outlook.com>

import sys
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
class Simplex():

    def __init__(self):
        self.tableau = list()
        self.quantVar = 0
        self.quantRest = 0
        self.tipo = 0
        self.solve = list()

    """
        A função forma_padrao inicializa o self.tableau com a PPL, passada 
        por parâmetro, na forma padrão.  
        Formato dos parâmetros:
        funcao_objetivo : [x1, x2, x3, ...]
        restricoes : [["<= ou >= ou = ",x1, x2, x3, ..., b1],["<= ou >= ou = ", x1, x2, x3, ..., b2], ..., [0, ">=", ">=",">=", ...]]
    """
    def forma_padrao(self,funcao_objetivo, restricoes):

        m = len(restricoes)
        contVarAdd=0
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
                self.solve.append(n+1)
            #Maior ou igual
            elif restricoes[i][0] == ">=":
                restricoes[i][0] = "=";
                restricoes[i].insert(n+1, 1)
                for k in range(m-1):
                    if k != i:
                        restricoes[k].insert(n+1, 0)
            #Lado Direito negativo
            print(restricoes[i][len(restricoes[i])-1])
            if restricoes[i][len(restricoes[i])-1] < 0:
                for j in range(1,len(restricoes[i])):
                    #CORRIGE ERRO PARA TUPLAR
                    restricoes[i][j] *= -1;

        self.quantVar = len(restricoes[1][1:])
        self.quantRest = len(restricoes) - 1
        self.tableau_inicial(funcao_objetivo, restricoes)

    """
        Transfere os valores das duas matrizes passadas por parâmetro em self.tableau
        Formato dos parâmetros:
        funcao_objetivo : [x1, x2, x3, ...]
        restricoes : [["<= ou >= ou = ",x1, x2, x3, ..., b1],["<= ou >= ou = ", x1, x2, x3, ..., b2], ..., [0, ">=", ">=",">=", ...]]
        
    """
    def tableau_inicial(self, funcao_objetivo, restricoes):

        for i in range(self.quantRest):
            self.tableau.append(restricoes[i][1:])
        self.tableau.append(funcao_objetivo)
        aux = len(self.tableau)-1
        for i in range( len(funcao_objetivo), len(self.tableau[0])):
            self.tableau[aux].append(0)
    """
         Determina a variável que sai na base
         Retorna o índice da coluna da varíavel no Tableau
    """
    def quem_entra(self):
        variavelEntra = min(self.tableau[self.quantRest])
        return self.tableau[self.quantRest].index(variavelEntra)

        """
            Determina a variável que sai na base
            Retorna o índice da linha da varivável no Tableau
        """
    def quem_sai(self, variavel_entra):
        razao=list()
        for i in range(self.quantRest):
            if self.tableau[i][variavel_entra] != 0:
                aux = self.tableau[i][self.quantVar-1]/self.tableau[i][variavel_entra]
                if aux>=0:
                    razao.append(aux)
                else:
                    razao.append(sys.maxsize)
            else:
                razao.append(sys.maxsize)
        return razao.index(min(razao))

    """
        Verifica se a Solução atual é ótima
        Retorna True se sim, caso contrário False
    """
    def is_otima(self):
        for custo in self.tableau[self.quantRest]:
            if custo < 0:
                return False
        return True

    """
        Determina a nova solução
    """
    def new_solution(self, sai, entra):

        #Deixando igual a 1 na coluna
        lista = list()
        aux1 = self.tableau[sai][entra]
        for i in range(self.quantVar):
            self.tableau[sai][i] = self.tableau[sai][i]/aux1
            lista.append(self.tableau[sai][i])

        #Zerando a coluna
        aux= dict()
        for i in range(self.quantRest+1):
            if i != sai:
                    aux[i]=(-1)*(self.tableau[i][entra]/self.tableau[sai][entra])

        for i in range(self.quantRest+1):
            for j in range(self.quantVar):
                if i != sai:
                    self.tableau[i][j] = aux[i] * lista[j] + self.tableau[i][j]
        self.solve
