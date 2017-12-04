from tkinter import *
from simplex import Simplex
from simplex_metodos import simplex_meth

class Application:
    def __init__(self, master=None):
        # Variáveis
        self.textFO = "Função Objetivo"
        self.textRes = "Restrições: \n"
        self.textRestrincao = ""
        self.numeroVariaveis = 0
        self.numeroVariaveisRes = 0
        self.funcaoObjetiva = list()  # lista que fica os coeficientes da função objetivo
        # self.listaRestrincoes = list()
        self.restrincaoL = []  # matriz das restrições
        self.aux = []  # adicionado para fazer uma matriz das restrições
        self.aux2 = [0]
        ######################################################

        self.fontePadrao = ("Arial", "10")

        # titulo
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()
        self.titulo = Label(self.primeiroContainer, text="SIMPLEX RESOLUTOR '-'")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        # subtitulo
        self.segundoConteiner = Frame(master)
        self.segundoConteiner["padx"] = 10
        self.segundoConteiner.pack()
        self.titulo = Label(self.segundoConteiner, text="Insira as variáveis da função objetivo", font=self.fontePadrao)
        self.titulo.pack()

        # Mostra a função objetiva
        self.terceiroConteiner = Frame(master)
        self.terceiroConteiner["padx"] = 10
        self.terceiroConteiner.pack()
        self.mensagem = Label(self.terceiroConteiner, text="", font=self.fontePadrao)
        self.mensagem.pack()

        # adicionar uma nova variável na função objetiva
        self.variavelObjetivaConteiner = Frame(master)
        self.variavelObjetivaConteiner["padx"] = 20
        self.variavelObjetivaConteiner.pack()
        self.tipo = IntVar()
        Radiobutton(self.variavelObjetivaConteiner, text="MIN", padx=20, variable=self.tipo, value=1).pack(anchor=W, side=LEFT)
        Radiobutton(self.variavelObjetivaConteiner, text="MAX", padx=20, variable=self.tipo, value=2).pack(anchor=W, side=LEFT)
        # Entrada de dados: variavel da função objetivo
        self.variavelObjetiva = Entry(self.variavelObjetivaConteiner)
        self.variavelObjetiva["width"] = 5
        self.variavelObjetiva["font"] = self.fontePadrao
        self.variavelObjetiva.pack(side=LEFT)
        # Label: X
        self.variavelObjetivaLabel = Label(self.variavelObjetivaConteiner, text="X" + str(self.numeroVariaveis + 1),
                                           font=("Arial", "11", "bold"))
        self.variavelObjetivaLabel["padx"] = 2
        self.variavelObjetivaLabel.pack(side=LEFT)
        # Botão: add
        self.add = Button(self.variavelObjetivaConteiner)
        self.add["text"] = "Add"
        self.add["command"] = self.addVariavelObjetiva
        self.add["padx"] = 20
        self.add.pack(side=RIGHT)

        # Adicionar as restrinções
        self.restrincaoConteiner = Frame(master)
        self.restrincaoConteiner["pady"] = 20
        self.restrincaoConteiner.pack()
        # Label: Insira restrinções
        self.restrincaoLabel = Label(self.restrincaoConteiner, text="Insira as restrinções: ")
        self.restrincaoLabel["font"] = ("Arial", "10", "bold")
        self.restrincaoLabel.pack()
        # Label: restrinção
        self.restrincaoLabel1 = Label(self.restrincaoConteiner)
        self.restrincaoLabel1["font"] = ("Arial", "10", "bold")
        self.restrincaoLabel1.pack()
        # Entrada de dados: vairiaveis
        self.restrincao = Entry(self.restrincaoConteiner)
        self.restrincao["width"] = 7
        self.restrincao["font"] = self.fontePadrao
        self.restrincao.pack(side=LEFT)
        # Label: X
        self.restrincaoLabel2 = Label(self.restrincaoConteiner, text="X1", font=("Arial", "11", "bold"))
        self.restrincaoLabel2["padx"] = 2
        self.restrincaoLabel2.pack(side=LEFT)
        # Botão: add
        self.add = Button(self.restrincaoConteiner, text="Add")
        self.add["command"] = self.addRestrincoes
        self.add["padx"] = 20
        self.add.pack(side=LEFT)
        # Separador: <
        self.separador = Label(self.restrincaoConteiner, text="<=", font=("Arial", "10", "bold"), padx=5)
        self.separador.pack(side=LEFT)
        # b
        self.b = Entry(self.restrincaoConteiner, width=5)
        self.b.pack(side=LEFT)
        # Botão: inserir
        self.Inserir = Button(self.restrincaoConteiner, text="Inserir")
        self.Inserir["command"] = self.addRestrincoesb
        self.Inserir["padx"] = 20
        self.Inserir.pack(side=LEFT)
        # Botão Proxima Restrição
        self.Proxima = Button(self.restrincaoConteiner, text="Proxima")
        self.Proxima["command"] = self.proxima_restrição
        self.Proxima["padx"] = 20
        self.Proxima.pack(side=RIGHT)
        # mostra as funções
        self.viewConteiner = Frame(master)
        self.viewConteiner["pady"] = 20
        self.viewConteiner.pack()
        self.view = Label(self.viewConteiner, text="Função Objetivo: ")
        self.view.pack()
        self.view2 = Label(self.viewConteiner, text="Restrinções: \n")
        self.view2.pack()

        self.solucaoConteiner = Frame(master)
        self.solucaoConteiner["padx"] = 20
        self.solucaoConteiner.pack()
        # Botão: solucao
        self.add = Button(self.solucaoConteiner)
        self.add["text"] = "Solucao"
        self.add["command"] = self.solucao_simplex
        self.add["padx"] = 20
        self.add.pack(side=RIGHT)

        self.resetaConteiner = Frame(master)
        self.resetaConteiner["padx"] = 20
        self.resetaConteiner.pack()
        # Botão: resetar
        self.add = Button(self.resetaConteiner)
        self.add["text"] = "Resetar"
        self.add["command"] = self.resetar
        self.add["padx"] = 20
        self.add.pack(side=RIGHT)

        self.showConteiner = Frame(master)
        self.showConteiner["padx"] = 40
        self.showConteiner.pack()
        self.show = Scrollbar(self.showConteiner)
        self.t = Text(self.showConteiner,height=10, width=200)
        self.show.pack(side=RIGHT, fill=Y)
        self.t.pack(side=LEFT, fill=Y)
        self.show.config(command=self.t.yview)
        self.t.config(yscrollcommand=self.show.set)


        # Botão: show

    def solucao_simplex(self):
        s= Simplex()
        s2 = simplex_meth() #<-
        self.restrincaoL.append(self.aux2)
        s.forma_padrao(self.funcaoObjetiva,self.restrincaoL)
        s2.setMatriz(s.tableau,self.tipo)
        quote = ""
        print("Solução Básica Inicial")
        if(self.tipo.get()==1): #Min
            s2.calc_min()
        if(self.tipo.get()==2): #Max
            s2.calc_max()
        #############
        print(self.tipo.get())
        print(s2.matriz)
        print(s2.valorFuncObj)
        print(s2.variaveisBasicas)
        print(s2.variaveisNaoBasicas)
        #############
        if(s2.flagIlimitado):
            quote += "A Solução não foi possível pois ela é ilimitada\n"
        else:
            quote += "Valor da função objetivo = "
            quote += str(s2.valorFuncObj) + "\n"
            quote += "Variaveis básicas = "
            quote += str(s2.variaveisBasicas) + "\n"
            quote += "Variaveis não básicas = "
            quote += str(s2.variaveisNaoBasicas) + "\n"
        self.t.insert(END,quote)            
        #############
        """
        quote+="Solução Básica Inicial:"+"\n"+str(s.solve)+"\n"
        while not (s.is_otima()):
            variavelEntra = s.quem_entra()
            print("Variável que entra")
            print(variavelEntra)
            quote += "Variável que entra:" + "\n"+str(variavelEntra)+"\n"
            variavelSai = s.quem_sai(variavelEntra)
            print("Variável que sai")
            print(variavelSai)
            quote += "Variável que sai:" +"\n"+ str(variavelSai) + "\n"
            s.new_solution(sai=variavelSai, entra=variavelEntra)
            print("Novo Tableau")
            quote += "Novo Tableau:"+"\n"
            for i in s.tableau:
                quote += str(i)+"\n"
            print(s.tableau)
        self.t.insert(END, quote)
        """


    def resetar(self):
        self.textFO = "Função Objetivo"
        self.textRes = "Restrições: \n"
        self.textRestrincao = ""
        self.numeroVariaveis = 0
        self.numeroVariaveisRes = 0
        self.funcaoObjetiva = list()  # lista que fica os coeficientes da função objetivo
        # self.listaRestrincoes = list()
        self.restrincaoL = []  # matriz das restrições
        self.aux = []
        self.mensagem["text"] =""
        self.variavelObjetivaLabel["text"] = "X" + str(self.numeroVariaveis + 1)
        self.restrincaoLabel2["text"]="X1"
        self.restrincaoLabel1["text"]=""





    def addVariavelObjetiva(self):
        """Adiciona variáveis a função objetivo"""

        try:
            xi = int(self.variavelObjetiva.get())
            self.funcaoObjetiva.append(xi)
            self.aux2.append(">=")
            self.numeroVariaveis += 1
            if xi < 0:
                self.textFO += str(xi) + "X" + str(self.numeroVariaveis) + " "
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
                self.textRestrincao += str(xi) + "X" + str(self.numeroVariaveisRes) + " "
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
            print("Aqui", self.aux)
            # self.numeroVariaveisRes += 1
            # self.restrincaoLabel2["text"] = "X" + str(self.numeroVariaveisRes + 1)
            self.textRestrincao += "=" + str(xi)
        except Exception:
            raise
        self.restrincaoLabel1["text"] = self.textRestrincao
        self.restrincao.delete(0, 999)

    def proxima_restrição(self):
        self.aux.insert(0, "<=")
        print(self.aux)
        print("Menimo", self.restrincaoL)
        self.restrincaoL.append(self.aux)
        print("Mais olha só", self.restrincaoL)
        #self.restrincaoL[len(self.restrincaoL) - 1].extend(self.aux)
        self.aux= list()
        self.textRestrincao += "\n"
        self.numeroVariaveisRes = 0
        self.view2["text"]=self.textRestrincao

    def geraTextRes(self, listaR):
        text = ""

        for y in range(0, len(listaR) - 2):
            n = listaR[y]
            if n < 0:
                text += str(n) + "X" + str(y + 1) + " "
            else:
                text += "+" + str(n) + "X" + str(y + 1) + " "
        text += " < " + str(listaR[-1]) + "\n"
        self.textRes += text

    def simplexAction(self):
        Simplex().forma_padrao(self.funcaoObjetiva, self.restrincaoL)

        ######################


root = Tk()
root.geometry('800x600')
Application(root)
root.mainloop()