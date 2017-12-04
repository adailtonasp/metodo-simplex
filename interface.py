from tkinter import *
import simplex as sim
class Application:
    def __init__(self, master=None):
        #Variáveis 
        self.textFO = "Função Objetivo"
        self.textRes = "Restrinções: \n"
        self.textRestrincao = ""
        self.numeroVariaveis = 0
        self.numeroVariaveisRes = 0
        self.funcaoObjetiva = list()  #lista que fica os coeficientes da função objetivo
        #self.listaRestrincoes = list()
        self.restrincaoL = [] #matriz das restrições
        self.aux = [] #adicionado para fazer uma matriz das restrições
        ######################################################

        self.fontePadrao = ("Arial", "10")
        
        #titulo
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()
        self.titulo = Label(self.primeiroContainer, text="SIMPLEX RESOLUTOR '-'")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        #subtitulo
        self.segundoConteiner = Frame(master)
        self.segundoConteiner["padx"] = 10
        self.segundoConteiner.pack()
        self.titulo = Label(self.segundoConteiner, text="Insira as variáveis da função objetivo", font=self.fontePadrao)
        self.titulo.pack()

        #Mostra a função objetiva
        self.terceiroConteiner = Frame(master)
        self.terceiroConteiner["padx"] = 10
        self.terceiroConteiner.pack()
        self.mensagem = Label(self.terceiroConteiner, text="", font=self.fontePadrao)
        self.mensagem.pack()

        #adicionar uma nova variável na função objetiva
        self.variavelObjetivaConteiner = Frame(master)
        self.variavelObjetivaConteiner["padx"] = 20
        self.variavelObjetivaConteiner.pack()
        #Entrada de dados: variavel da função objetivo
        self.variavelObjetiva = Entry(self.variavelObjetivaConteiner)
        self.variavelObjetiva["width"] = 5
        self.variavelObjetiva["font"] = self.fontePadrao
        self.variavelObjetiva.pack(side=LEFT)
        #Label: X
        self.variavelObjetivaLabel = Label(self.variavelObjetivaConteiner,text="X" + str(self.numeroVariaveis + 1), font=("Arial", "11", "bold"))
        self.variavelObjetivaLabel["padx"] = 2
        self.variavelObjetivaLabel.pack(side=LEFT)
        #Botão: add
        self.add = Button(self.variavelObjetivaConteiner)
        self.add["text"] = "Add"
        self.add["command"] = self.addVariavelObjetiva
        self.add["padx"] = 20
        self.add.pack(side=RIGHT)
       
        #Adicionar as restrinções
        self.restrincaoConteiner = Frame(master)
        self.restrincaoConteiner["pady"] = 20
        self.restrincaoConteiner.pack()
        #Label: Insira restrinções
        self.restrincaoLabel = Label(self.restrincaoConteiner, text="Insira as restrinções: ")
        self.restrincaoLabel["font"] = ("Arial", "10", "bold")
        self.restrincaoLabel.pack()
        #Label: restrinção
        self.restrincaoLabel1 = Label(self.restrincaoConteiner)
        self.restrincaoLabel1["font"] = ("Arial", "10", "bold")
        self.restrincaoLabel1.pack()
        #Entrada de dados: vairiaveis
        self.restrincao = Entry(self.restrincaoConteiner)
        self.restrincao["width"] = 7
        self.restrincao["font"] = self.fontePadrao
        self.restrincao.pack(side = LEFT)
        #Label: X
        self.restrincaoLabel2 = Label(self.restrincaoConteiner,text="X1" , font=("Arial", "11", "bold"))
        self.restrincaoLabel2["padx"] = 2
        self.restrincaoLabel2.pack(side=LEFT)
        #Botão: add
        self.add = Button(self.restrincaoConteiner, text = "Add")
        self.add["command"] = self.addRestrincoes
        self.add["padx"] = 20
        self.add.pack(side=LEFT)
        #Separador: <
        self.separador = Label(self.restrincaoConteiner, text = "<=", font = ("Arial", "10", "bold"), padx = 5)
        self.separador.pack(side = LEFT)
        #b
        self.b = Entry(self.restrincaoConteiner, width = 5)
        self.b.pack(side = LEFT)
        #Botão: inserir
        self.Inserir = Button(self.restrincaoConteiner, text = "Inserir")
        self.Inserir["command"] = self.addRestrincoesb
        self.Inserir["padx"] = 20
        self.Inserir.pack(side=LEFT)
        #Botão Proxima Restrição
        self.Proxima = Button(self.restrincaoConteiner,text = "Proxima")
        self.Proxima["command"] = self.proxima_restrição
        self.Proxima["padx"] = 20
        self.Proxima.pack(side=RIGHT)
        #mostra as funções
        self.viewConteiner = Frame(master)
        self.viewConteiner["pady"] = 20
        self.viewConteiner.pack()
        self.view = Label(self.viewConteiner, text = "Função Objetivo: ")
        self.view.pack()
        self.view2 = Label(self.viewConteiner, text = "Restrinções: \n")
        self.view2.pack()


    def addVariavelObjetiva(self):
        """Adiciona variáveis a função objetivo"""
                
        try:
            xi = int(self.variavelObjetiva.get())
            self.funcaoObjetiva.append(xi)
            self.numeroVariaveis += 1
            if xi < 0:
                self.textFO += str(xi)+ "X" + str(self.numeroVariaveis) + " "
            else:
                self.textFO += "+" + str(xi) + "X" + str(self.numeroVariaveis) + " "
            self.variavelObjetivaLabel["text"] = "X" + str(self.numeroVariaveis + 1)
        except Exception:
            raise
        self.view["text"] = (self.textFO)
        self.variavelObjetiva.delete(0, 999)
        print(self.funcaoObjetiva)

    def addRestrincoes(self):
        """Adicionar as restrinções"""
        try:
            xi = int(self.restrincao.get())
            self.aux.append(xi)
            print(self.aux)
            self.numeroVariaveisRes += 1
            self.restrincaoLabel2["text"] = "X" + str(self.numeroVariaveisRes + 1)
            if xi < 0:
                self.textRestrincao += str(xi)+ "X" + str(self.numeroVariaveisRes) + " "
            else:
                self.textRestrincao += "+" + str(xi) + "X" + str(self.numeroVariaveisRes) + " "
        except Exception:
            raise
        self.restrincaoLabel1["text"] = self.textRestrincao
        self.restrincao.delete(0, 999)
    
    def addRestrincoesb(self):
        """Adicionar as restrinções"""
        try:
            xi = int(self.b.get())
            self.aux.append(xi)
            print(self.aux)
            #self.numeroVariaveisRes += 1
            #self.restrincaoLabel2["text"] = "X" + str(self.numeroVariaveisRes + 1)
            self.textRestrincao += "=" + str(xi)
        except Exception:
            raise
        self.restrincaoLabel1["text"] = self.textRestrincao
        self.restrincao.delete(0, 999)    
        
    def proxima_restrição(self):
        print(self.aux)
        print(self.restrincaoL)
        self.restrincaoL.append([])
        self.restrincaoL[len(self.restrincaoL)-1].extend(self.aux)
        self.aux.clear()
        self.textRestrincao += "\n"
        self.numeroVariaveisRes = 0
    def geraTextRes(self, listaR):
        text = ""
        
        for y in range(0, len(listaR) - 2):
            n = listaR[y]
            if n < 0:       
                text += str(n) + "X" + str(y+1) + " "
            else:
                text += "+" +str(n) + "X" + str(y+1) + " "
        text += " < " + str(listaR[-1]) + "\n"
        self.textRes += text

    def simplexAction(self):
        sim.forma_padrao(self.funcaoObjetiva,self.restrincaoL)
        
    ######################    
root = Tk()
root.geometry('800x600')
Application(root)
root.mainloop()
