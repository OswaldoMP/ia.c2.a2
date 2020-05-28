import numpy as np
import random
from  random import sample
import matplotlib.pyplot as plt
import pandas as pd


class Dieta:

    def __init__(self,PESO,ALTURA,EDAD,EJERCICIO,SEXO):
        self.PESO = PESO #DATO DE ENTRADA
        self.ALTURA = ALTURA #DATAO DE ENTRADA
        self.EDAD = EDAD # DATO DE ENTRADA
        self.EJERCICIO = EJERCICIO #DATO DE ENTRADA
        self.IMC = self.PESO / ((self.ALTURA/100)**2)
        self.TAMANO_POBLACION = 15 #DATO DE ENTRADA?
        self.POBLACION = []
        self.SEXO = SEXO # DATO ENTRADA
        self.TMB = None
        self.CARBOHIDRATOS_PORCENTAJE = None
        self.PROTEINAS_PORCENTAJE = None
        self.LIPIDOS_PORCENTAJE = None
        self.SOBRE_PESO = None
        self.APTITUD = None #VARIABLE DEL OBJETIVO FIT
        self.TOTAL_GANANCIA = 0
        self.PORCENTAJE = int((self.TAMANO_POBLACION*95)/100)
        self.FLAG = False
        self.LISTA_GRAFICAR = []
        pass

    def main(self):
        self.calcular()
        print('TMB => ',self.TMB)

        while True:
            print('TMB => ',self.TMB)
            print('IMC =>', self.IMC)
            self.createPoblacion()
            # print('iniico => ',self.POBLACION)
            valor = self.funcionAptitud(self.POBLACION)
            #ordenar poblacion por Aptitud
            self.POBLACION.sort(key=lambda  poblacion: poblacion[11], reverse=True)
            print('Poblacion Inital => ', self.POBLACION)
            print('fin__')
            if self.POBLACION[0][11] > 0:
                break
            else:
                self.POBLACION.clear()
        #--------------------------
        x = 0
        while self.FLAG != True:
            self.LISTA_GRAFICAR.clear()
            print()
            print('d__',self.POBLACION)
            self.funcionAptitud(self.POBLACION)
            # self.grafica(self.LISTA_GRAFICAR,x)
            INDIVIDUOS_PADRE = self.seleccion()
            # print()
            # print('PADRE => ',INDIVIDUOS_PADRE)
            # print()
            INDIVIDUOS_HIJOS = self.cruza(INDIVIDUOS_PADRE)
            # print()
            # print('HIJOS => ', INDIVIDUOS_HIJOS)
            # print()
            INDIVIDUOS_HIJOS_M = self.mutacion(INDIVIDUOS_HIJOS)
            # print()
            # print('HIJOS_MU => ', INDIVIDUOS_HIJOS_M)
            # print('==> GANANCIA => ', self.TOTAL_GANANCIA)
            # print()
            POBLACION_NEW = self.funcionAptitud(INDIVIDUOS_HIJOS_M)
            # print()
            # print('POBLACION_NEW => ',POBLACION_NEW)
            POBLACION_NEW.sort(key=lambda POBLACION_NEW: POBLACION_NEW[11], reverse=True)
            # print()
            self.update(POBLACION_NEW)
            self.grafica(self.LISTA_GRAFICAR,x)
            self.FLAG = self.condicionParo()
            x = x +1
            print('---------------------',x,'------------------------------')
        pass

    def grafica(self,listaValores,x):
        print(listaValores)
        listaValores.sort()
        plt.plot(listaValores, marker='x', linestyle=':', color='r', label = f'Dieta {x+1} kc = {listaValores[0]} ')
        # plt.plot(lista2, marker='*', linestyle='-', color='g', label = "Febrero")
        # plt.plot(lista3, marker='o', linestyle='--', color='r', label = "Marzo")
        plt.xlabel('Individuos')
        plt.ylabel('KiloCalorías')
        plt.title('Dieta')
        plt.legend(loc="upper left")
        plt.savefig(f'ImageGrafica-VALOR {x}')
        self.LISTA_GRAFICAR.clear()
        pass

    def condicionParo(self):
        print('Valor Maximo paro => ',self.POBLACION[0][11])
        mayorElemento = self.POBLACION[0][11]
        count = 0
        for i in range(len(self.POBLACION)):
            if self.POBLACION[i][11] == mayorElemento:
                count=count+1
        if count >= self.PORCENTAJE:
            return True
        return False
        pass

    def update(self,POBLACION_NEW):
        for i in range(len(self.POBLACION)):
            self.POBLACION[i] = POBLACION_NEW[i]
            self.LISTA_GRAFICAR.append(self.POBLACION[i][11])
            # self.POBLACION[i].pop()
        pass

    def funcionAptitud(self,POBLACION_NEW):
        #calcular la suma total
        #Suma total Carbohidratos
        self.TOTAL_GANANCIA = 0
        sumaTotalCarbohidratos = 0
        sumaTotalProteinas = 0
        sumaTotalLipidos = 0
        for i in range(len(POBLACION_NEW)):
            sumaTotalCarbohidratos = 0
            sumaTotalProteinas = 0
            sumaTotalLipidos = 0
            for j in range(5):
                sumaTotalCarbohidratos = sumaTotalCarbohidratos + POBLACION_NEW[i][j]
            #Llenar Protenínas
            for j in range(5,8):
                sumaTotalProteinas = sumaTotalProteinas + POBLACION_NEW[i][j]
            #Llenar lípidos
            for j in range(8,11):
                sumaTotalLipidos = sumaTotalLipidos + POBLACION_NEW[i][j]

            self.setAptitud(sumaTotalCarbohidratos,sumaTotalProteinas,sumaTotalLipidos)
            print('APTITUD ===>',self.APTITUD)
            #A cada individuo i se le asigna su valor de APTITUD
            POBLACION_NEW[i].extend([self.APTITUD])
        POBLACION_NEW = self.restricciones(POBLACION_NEW)
        for i in range(len(POBLACION_NEW)):
            self.TOTAL_GANANCIA = self.TOTAL_GANANCIA + POBLACION_NEW[i][11]
            # self.LISTA_GRAFICAR.append(POBLACION_NEW[i][11])
        return POBLACION_NEW

    def restricciones(self,POBLACION_NEW):
        if self.SOBRE_PESO == 1:
            print('Sobre Peso')
            for i in range(len(POBLACION_NEW)):
                if POBLACION_NEW[i][11] <= 2000:
                    pass
                else:
                    POBLACION_NEW[i][11] = 0
        elif self.SOBRE_PESO == -1:
            print('Peso Bajo')
            for i in range(len(POBLACION_NEW)):
                if  POBLACION_NEW[i][11] <= 2300:
                    pass
                else:
                    POBLACION_NEW[i][11] = 0
        else:
            print('Peso Normal')
            for i in range(len(POBLACION_NEW)):
                if  POBLACION_NEW[i][11] <= self.TMB:
                    pass
                else:
                    POBLACION_NEW[i][11] = 0
        return POBLACION_NEW

    # Calcular la aptitud de cada individuo i
    def setAptitud(self,sumaTotalCarbohidratos,sumaTotalProteinas,sumaTotalLipidos):
        self.APTITUD = 0
        # Calcular la aptitud de cada individuo i
        if sumaTotalCarbohidratos != self.CARBOHIDRATOS_PORCENTAJE:
            self.APTITUD = self.APTITUD + int(abs(sumaTotalCarbohidratos - self.CARBOHIDRATOS_PORCENTAJE))
        if sumaTotalProteinas != self.PROTEINAS_PORCENTAJE:
            self.APTITUD = self.APTITUD + int(abs(sumaTotalProteinas - self.PROTEINAS_PORCENTAJE))
        if sumaTotalLipidos != self.LIPIDOS_PORCENTAJE:
            self.APTITUD = self.APTITUD + int(abs(sumaTotalLipidos - self.LIPIDOS_PORCENTAJE))

    def seleccion(self):
        #metodo de la ruleta, para seleccionar los mejores
        ruleta = []
        aux = 0
        numeroAleatorio = []
        listaIndex = []
        #Obtener la probalidad
        for i in range(len(self.POBLACION)):
            numeroAleatorio.append(random.random())
            aux = self.POBLACION[i][11] / self.TOTAL_GANANCIA + aux
            ruleta.append(aux)
        # print(np.sum(listaProbalidad),'lis',ruleta)
        #Obtener los mejores
        for i in range(len(self.POBLACION)):
            aux = 0
            for j in range(len(self.POBLACION)):
                if numeroAleatorio[i] <= ruleta[j]:
                    listaIndex.append(self.POBLACION[j])
                    break
        return listaIndex

    #Cruza BI-PUNTUAL
    def cruza(self,INDIVIDUOS_PADRE):
        INDIVIDUOS_HIJOS = []
        for i in range(len(self.POBLACION)):
            for j in range(i+1,len(self.POBLACION)):
                posicionCruce =  random.sample(range(0,11),2)
                posicionCruce.sort()#ordenar indices de cruza
                hijo1 = list(INDIVIDUOS_PADRE[i][:posicionCruce[0]]) + list(INDIVIDUOS_PADRE[j][posicionCruce[0]:posicionCruce[1]]) + list(INDIVIDUOS_PADRE[i][posicionCruce[1]:11])
                hijo2 = list(INDIVIDUOS_PADRE[j][:posicionCruce[0]]) + list(INDIVIDUOS_PADRE[i][posicionCruce[0]:posicionCruce[1]]) + list(INDIVIDUOS_PADRE[j][posicionCruce[1]:11])
                INDIVIDUOS_HIJOS.append(hijo1)
                INDIVIDUOS_HIJOS.append(hijo2)
                posicionCruce.clear()
        return INDIVIDUOS_HIJOS
        pass

    def mutacion(self,INDIVIDUOS_HIJOS):
        for i in range(len(self.POBLACION)):
            numeroIntercambio = random.randint(0,(11//2))
            for j in range(11):
                posicion = random.sample(range(0,11),2)
                valorAux = INDIVIDUOS_HIJOS[i][posicion[0]]
                INDIVIDUOS_HIJOS[i][posicion[0]] = INDIVIDUOS_HIJOS[i][posicion[1]]
                INDIVIDUOS_HIJOS[i][posicion[1]] = valorAux
        return INDIVIDUOS_HIJOS

    #crear Poblacion
    def createPoblacion(self):
        for i in range(self.TAMANO_POBLACION):
            self.POBLACION.append(self.createIndividuos())

    def createIndividuos(self):
        #Llena los alelos del individuo i
        vectorCalorias = []
        #Llenar Carbohidratos
        for i in range(5):
            valor = int(random.uniform(0,self.CARBOHIDRATOS_PORCENTAJE))
            vectorCalorias.append(valor)
        #Llenar Protenínas
        for i in range(5,8):
            valor = int(random.uniform(0,self.PROTEINAS_PORCENTAJE))
            vectorCalorias.append(valor)
        #Llenar lípidos
        for i in range(8,11):
            valor = int(random.uniform(0,self.LIPIDOS_PORCENTAJE))
            vectorCalorias.append(valor)
        return vectorCalorias

    def calcular(self):
        #Calcular las calorías diarias
        # Masuculino if sexo = 1
        if self.SEXO == 1:
            self.TMB = 66.4 + (13.7 * self.PESO) + (5 * self.ALTURA) - (6.76 * self.EDAD)
        else:
            self.TMB = 655.1 + ( (9.6 * self.PESO) + (1.8 * self.ALTURA) - (4.7 * self.EDAD))
        # print(self.TMB,'TMB 1')
        #Obtener los porcentajes que requiere para la dieta, 50%, 30%, 20%
        self.CARBOHIDRATOS_PORCENTAJE = self.TMB * .50
        self.PROTEINAS_PORCENTAJE = self.TMB * .30
        self.LIPIDOS_PORCENTAJE = self.TMB * .20
        print(self.CARBOHIDRATOS_PORCENTAJE,self.PROTEINAS_PORCENTAJE,self.LIPIDOS_PORCENTAJE)

        self.SOBRE_PESO = self.calcularSobrePeso()
        self.calcularCaloriaActividad()
        pass

    def calcularSobrePeso(self):
        #sobre peso > 27, peso bajo < 18 y peso normal >18 y < 25
        print(self.IMC)
        if self.IMC < 18:
            sobrePeso = -1
            return sobrePeso
        elif self.IMC <= 25:
            sobrePeso = 0
            return sobrePeso
        else:
            sobrePeso = 1
            return sobrePeso

    def calcularCaloriaActividad(self):
        if self.EJERCICIO == 0:
            self.TMB = self.TMB * 1.2
        elif self.EJERCICIO == 3:
            self.TMB = self.TMB * 1.375
        elif self.EJERCICIO == 5:
            self.TMB = self.TMB * 1.55
        elif self.EJERCICIO == 7:
            self.TMB = self.TMB * 1.725



# if __name__ == "__main__":
#     miDieta = Dieta(70,170,21,2,1)
#     miDieta.main()
#     pass