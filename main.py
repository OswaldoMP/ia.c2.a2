from view.window_ui import *
from view.window_ui import IForm
from Dieta import Dieta
class Main(QtWidgets.QMainWindow,IForm):

    def __init__(self,*args,**kwargs):
        QtWidgets.QMainWindow.__init__(self,*args,**kwargs)
        self.setupUi(self)
        self.buttonSelect.clicked.connect(self.initial)


    def initial(self):
        EJERCICIO = -1
        SEXO = 2
        ALTURA = int(self.textNumeroElemento.text())
        print(ALTURA,"ALTURA")
        PESO = int(self.textR1.text())
        print(PESO,"PESO")
        EDAD = int(self.textR2.text())
        print(EDAD,"EDAD")
        if self.option1.isChecked():
            EJERCICIO = 0
        elif self.option2.isChecked():
            EJERCICIO = 3
        elif self.option3.isChecked():
            EJERCICIO = 5
        elif self.option4.isChecked():
            EJERCICIO = 7
        if self.option5.isChecked():
            SEXO = 1
            
        print(EJERCICIO,SEXO)
        
        # pesoMin = int(self.textPesoMin.text())
        # # print(self.textTMax.text(),"tmax")
        # pesoMax = int(self.textPesoMax.text())
        # # print(self.text0.text(),"t0")
        # volumenMin = int(self.textVolumenMin.text())
        # volumenMax = int(self.textVolumenMax.text())
        # gananciaMin = int(self.textGananciaMin.text())
        # ganancianMax = int(self.textGananciaMax.text())
        # porcentaje = int(self.textCondicion.text())
        # print(self.textcodP.text(),"cond")
        #cruza = 1
        # geneticos = Geneticos(k,n_max,m,t_max,t_inicial,porcentaje,cruza)
        # geneticos.start()
        # miKp = KnapsackTest(numeroElemento,15,R2,R1,porcentaje,pesoMin,pesoMax,volumenMin,volumenMax,gananciaMin,ganancianMax)
        miDieta = Dieta(PESO,ALTURA,EDAD,EJERCICIO,SEXO)
        miDieta.main()
        

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = Main()
    window.show()
    app.exec_() 



















