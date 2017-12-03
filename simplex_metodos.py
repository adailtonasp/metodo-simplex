# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 21:58:41 2017

@author: Adailton Palhano
"""

"""
O programa vai trabalhar com o problema na forma padrao
ele vai receber uma matriz do tipo Ax = b e tabem a função objetivo
uma variavel definira se o problema sera de maximizacao ou minimizacao
"""

class simplex:
    
    tipoFunc = 0 #variavel que define se a funcao obejtico é max(1) ou min(0)
    matriz = [] #define a matriz
    quantVar = 0 #define a quantidade de variaveis xn do problema
    quantEqua = 0 #define a quantidade de equacoes
    variaveisBasicas = {}
    variaveisNaoBasicas = {}
    valorFuncObj = 0 
    
    def setMatriz (self,m,t):
        self.matriz = m #atribuição a matriz da classe
        self.tipoFunc = t #atribuição do tipo da matriz
        self.quantVar = len(self.matriz[0]) - 1 #definição da quantidade de variaveis
        self.quantEqua = len(self.matriz) - 1 #definicao da quantidade de equacoes
    
    def calc_min (self):
        
        varDict = {} #dicionario auxiliar para decidir qual variavel ira sair da base
        flagIlimitado = 0 #flag que identifica que os coeficientes da matriz na coluna da variavel candidata são negativos,ou seja, a solução é ilimitada
        flagVB = 0 #identifica que nãa há mais variaveis para entrar na base 
        aux = 0 #é utilizado para forca o pivor o valor 1
        
        
        while 1 : #loop necessario para fazer o pivoteamento das variaveis que saem e entram na base 
            for x in range(0,self.quantVar): #for para "andar" na função objetivo da ppl
                if(self.matriz[self.quantEqua][x] < 0): #verificação se o custo relativo de cada variavel da função objetivo é < 0,ou seja,se a variavel é candidata ou não
                    for y in range(0,self.quantEqua): #apos encontrar o indice da coluna é necessario fazer uma verificação em cada linha nessa coluna 
                         if(self.matriz[y][x] > 0): #necessario nessa verificação observar os elemento positivos diferentes de 0
                             varDict[float(self.matriz[y][self.quantVar]/self.matriz[y][x])] = y #então fazemos a divisão do termo independente dessa linha pelo coeficiente da coluna onde há variavel candidata - o "x" do for + externo guarda essa informação
                             #para saber qual linha tera o menor resultado da divisão utilizaremos um dicionario para guardar isso: [resultado da divisão] = linha(restrição) onde foi feita da divisão dos elementos
                    if(len(varDict)==0): #caso não haja nenhuma elemento nesse dicionario, todos os coeficientes daquela variavel são negativos ou = a 0
                        print("solução Ilimitada") #dessa forma a solução é ilimitada
                        flagIlimitado = 1 #<- necessario para sair do loopwhile
                        break;
                    aux = min(varDict.keys()) #nesse ponto aux tera o menor resultado das divisões feitas anteriomente
                    y = varDict[aux] #nesse ponto obtemos o indice da linha onde faremos o pivoteamento
                    #agora ja possuimos os dois indices
                    # x = indice das colunas
                    # y = indice das linhas
                    varDict.clear() #o dicionario deve ser limpo para ser utilizada na proxima interação caso necessario
                    
                    ###
                    #essa parte foi adicionada para forçar que o elemento base do pivoteamento seja sempre 1
                    if(self.matriz[y][x]!=1 ):
                        aux = self.matriz[y][x]
                        for a in range (0,self.quantVar+1):
                            self.matriz[y][a] = float(self.matriz[y][a]/aux)
                    ###
                    
                    #agora faremos o pivoteamento
                    for z in range(0,self.quantEqua+1): #iremos "caminhar" pelas linhas do tableau para realizar transformações
                        if(z==y): #como a linha do elemento base para pivoteamento não muda iremos pular na sua vez
                            continue
                        multiplicador =  float(self.matriz[z][x] * (-1) / self.matriz[y][x]) #aqui iremos calcular o multiplicador do pivoteamento
                        for a in range (0,self.quantVar + 1):
                            self.matriz[z][a] += multiplicador * self.matriz[y][a] #aqui iremos atualizar cada linha do tabeau
                    break #terminada a atualização deve se checkar se ainda há variaveis para entrar na base
                elif(x == self.quantVar-1): #se não foi encontrada nenhum candidato até a ultima variavel verificada uma solução otima deve ter sido encontrada
                    print("Não há candidatos para entrar nas variaveis básicas")
                    flagVB = 1
                    break
            if(flagIlimitado): #se for ilimitada deve-se sair do loopwhile
                break
            if(flagVB): #se não tiver mais candidatos deve-se sair do loopwhile
                self.set_var()
                break
            
    #Transformar o problema de maximização em um de minimização
    #todas as outras operações são as mesmas do metodo de minimização            
    def calc_max(self):
        varDict = {}
        flagIlimitado = 0
        flagVB = 0
        #para reaproveitar o metodo de minimização iremos inverter a função objetivo do tableau de maximização 
        for x in range(0,self.quantVar):
            self.matriz[self.quantEqua][x] *= (-1)
            
        while 1 : #loop necessario para fazer o pivoteamento das variaveis que saem e entram na base 
            for x in range(0,self.quantVar): #for para "andar" na função objetivo da ppl
                if(self.matriz[self.quantEqua][x] < 0): #verificação se o custo relativo de cada variavel da função objetivo é < 0,ou seja,se a variavel é candidata ou não
                    for y in range(0,self.quantEqua): #apos encontrar o indice da coluna é necessario fazer uma verificação em cada linha nessa coluna 
                         if(self.matriz[y][x] > 0): #necessario nessa verificação observar os elemento positivos diferentes de 0
                             varDict[float(self.matriz[y][self.quantVar]/self.matriz[y][x])] = y #então fazemos a divisão do termo independente dessa linha pelo coeficiente da coluna onde há variavel candidata - o "x" do for + externo guarda essa informação
                             #para saber qual linha tera o menor resultado da divisão utilizaremos um dicionario para guardar isso: [resultado da divisão] = linha(restrição) onde foi feita da divisão dos elementos
                    if(len(varDict)==0): #caso não haja nenhuma elemento nesse dicionario, todos os coeficientes daquela variavel são negativos ou = a 0
                        print("solução Ilimitada") #dessa forma a solução é ilimitada
                        flagIlimitado = 1 #<- necessario para sair do loopwhile
                        break;
                    aux = min(varDict.keys()) #nesse ponto aux tera o menor resultado das divisões feitas anteriomente
                    y = varDict[aux] #nesse ponto obtemos o indice da linha onde faremos o pivoteamento
                    #agora ja possuimos os dois indices
                    # x = indice das colunas
                    # y = indice das linhas
                    varDict.clear() #o dicionario deve ser limpo para ser utilizada na proxima interação caso necessario
                    
                    ###
                    #essa parte foi adicionada para forçar que o elemento base do pivoteamento seja sempre 1
                    if(self.matriz[y][x]!=1 ):
                        aux = self.matriz[y][x]
                        for a in range (0,self.quantVar+1):
                            self.matriz[y][a] = float(self.matriz[y][a]/aux)
                    ###
                    
                    #agora faremos o pivoteamento
                    for z in range(0,self.quantEqua+1): #iremos "caminhar" pelas linhas do tableau para realizar transformações
                        if(z==y): #como a linha do elemento base para pivoteamento não muda iremos pular na sua vez
                            continue
                        multiplicador =  float(self.matriz[z][x] * (-1) / self.matriz[y][x]) #aqui iremos calcular o multiplicador do pivoteamento
                        for a in range (0,self.quantVar + 1):
                            self.matriz[z][a] += multiplicador * self.matriz[y][a] #aqui iremos atualizar cada linha do tabeau
                    break #terminada a atualização deve se checkar se ainda há variaveis para entrar na base
                elif(x == self.quantVar-1): #se não foi encontrada nenhum candidato até a ultima variavel verificada uma solução otima deve ter sido encontrada
                    print("Não há candidatos para entrar nas variaveis básicas")
                    flagVB = 1
                    break
            if(flagIlimitado): #se for ilimitada deve-se sair do loopwhile
                break
            if(flagVB): #se não tiver mais candidatos deve-se sair do loopwhile
                self.set_var()
                break
        #como invertemos a função objetivo devemos atualizar seu valor já que é um problema de maximização
        self.matriz[self.quantEqua][self.quantVar] *= (-1)
    
    def set_var(self):
        for x in range(0,self.quantVar):
            if(self.matriz[self.quantEqua][x] == 0):
                for y in range(0,self.quantEqua):
                    if(self.matriz[y][x]==1):
                        self.variaveisBasicas[x+1]=self.matriz[y][self.quantVar]
                        break
            else:
                self.variaveisNaoBasicas[x+1] = 0
                
        self.valorFuncObj = self.matriz[self.quantEqua][self.quantVar] * (-1)
