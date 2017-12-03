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
    #self.objFunc = [] #variavel que define a funcao objetivo do problema
    matriz = [] #define a matriz
    quantVar = 0 #define a quantidade de variaveis xn do problema
    quantEqua = 0 #define a quantidade de equacoes
    #self.terInd = [] #matriz que define os termos independentes
    variaveisBasicas = {}
    variaveisNaoBasicas = {}
    
    def setMatriz (self,m,t):
        self.matriz = m
        self.tipoFunc = t
        self.quantVar = len(self.matriz[0]) - 1 
        self.quantEqua = len(self.matriz) - 1
        #self.objFunc = self.matriz[len(self.matriz)-1]
        
        #self.variaveisBasicas = self.quantVar -self.quantEqua
    
    """
    #retira os termos independentes da matriz e coloca na lista 'terInd'    
    def corrigeMatriz (self):
        for n in self.matriz:
            self.terInd.append(n.pop)
    """        
    """
    realiza o teste de otimalidade para funcao de minimizacao
    ira ser escolhido sempre o primerio Custo relativo < 0 sera escolhido
    """
    def calc_min (self):
        
        varDict = {}
        flagIlimitado = 0
        flagVB = 0
        
        while 1 :
            for x in range(0,self.quantVar):
                if(self.matriz[self.quantEqua][x] < 0):
                    for y in range(0,self.quantEqua):
                         if(self.matriz[y][x] > 0):
                             varDict[float(self.matriz[y][self.quantVar]/self.matriz[y][x])] = y
                    if(len(varDict)==0):
                        print("solução Ilimitada")
                        flagIlimitado = 1
                        break;
                    aux = min(varDict.keys())
                    y = varDict[aux]
                    varDict.clear()
                    for z in range(0,self.quantEqua+1):
                        if(z==y):
                            continue
                        multiplicador =  float(self.matriz[z][x] * (-1) / self.matriz[y][x])
                        for a in range (0,self.quantVar + 1):
                            self.matriz[z][a] += multiplicador * self.matriz[y][a] #+ self.matriz[z][a]
                            
                    break
                elif(x == self.quantVar-1):
                    print("Não há candidatos para entrar nas variaveis básicas")
                    flagVB = 1
                    break
            if(flagIlimitado):
                break
            if(flagVB):
                self.set_var()
                break
            
    #Transformar o problema de maximização em um de minimização            
    def calc_max(self):
        varDict = {}
        flagIlimitado = 0
        flagVB = 0
        
        for x in range(0,self.quantVar):
            self.matriz[self.quantEqua][x] *= (-1)
            
        while 1 :
            for x in range(0,self.quantVar):
                if(self.matriz[self.quantEqua][x] < 0):
                    for y in range(0,self.quantEqua):
                         if(self.matriz[y][x] > 0):
                             varDict[float(self.matriz[y][self.quantVar]/self.matriz[y][x])] = y
                    if(len(varDict)==0):
                        print("solução Ilimitada")
                        flagIlimitado = 1
                        break;
                    aux = min(varDict.keys())
                    y = varDict[aux]
                    varDict.clear()
                    for z in range(0,self.quantEqua+1):
                        if(z==y):
                            continue
                        multiplicador =  float(self.matriz[z][x] * (-1) / self.matriz[y][x])
                        for a in range (0,self.quantVar + 1):
                            self.matriz[z][a] += multiplicador * self.matriz[y][a] #+ self.matriz[z][a]
                            
                    break
                elif(x == self.quantVar-1):
                    print("Não há candidatos para entrar nas variaveis básicas")
                    flagVB = 1
                    break
            if(flagIlimitado):
                break
            if(flagVB):
                self.set_var()
                break
    
        self.matriz[self.quantEqua][self.quantVar] *= (-1)
    
    def set_var(self):
        for x in range(0,self.quantVar):
            if(self.matriz[self.quantEqua][x] == 0):
                for y in range(0,self.quantEqua):
                    if(y==1):
                        self.variaveisBasicas[x+1]=self.matriz[y][self.quantVar]
                        break
            else:
                self.variaveisNaoBasicas[x+1] = 0
            
            
            
                
            
                    
                
            
            
            
            
            
        
                     
                
