
from PyQt5 import QtCore, QtGui, QtWidgets

class IForm(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 720)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMaximumSize(QtCore.QSize(500, 300))

        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(560, 160, 91, 161))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        font = QtGui.QFont()
        font.setPointSize(12)
        
        font = QtGui.QFont()
        font.setPointSize(12)
        self.buttonSelect = QtWidgets.QPushButton(Form)
        self.buttonSelect.setGeometry(QtCore.QRect(400, 260, 89, 23))
        self.buttonSelect.setObjectName("buttonSelect")
    
    
        self.textNumeroElemento = QtWidgets.QLineEdit(Form)#K
        self.textNumeroElemento.setObjectName("textNumeroElemento")
        self.textNumeroElemento.setGeometry(QtCore.QRect(100, 40, 50, 20))


        self.textR1 = QtWidgets.QLineEdit(Form)#erro volum
        self.textR1.setObjectName("textR1")
        self.textR1.setGeometry(QtCore.QRect(100, 80, 50, 20))

        self.textR2 = QtWidgets.QLineEdit(Form)#erri peso
        self.textR2.setObjectName("textR2")
        self.textR2.setGeometry(QtCore.QRect(100, 120, 50, 20))
###################################################################

        self.numeroElemento = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.numeroElemento.setFont(font)
        self.numeroElemento.setObjectName("numeroElemento")
        self.numeroElemento.setGeometry(QtCore.QRect(10, 0, 120, 90))

        self.restriccionPeso = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.restriccionPeso.setFont(font)
        self.restriccionPeso.setObjectName("restriccionPeso")
        self.restriccionPeso.setGeometry(QtCore.QRect(10, 0, 110, 180))

        self.restriccionVolumen = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.restriccionVolumen.setFont(font)
        self.restriccionVolumen.setObjectName("restriccionVolumen")
        self.restriccionVolumen.setGeometry(QtCore.QRect(10, 0, 110, 265))

        self.peso_min = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.peso_min.setFont(font)
        self.peso_min.setObjectName("peso_min")
        self.peso_min.setGeometry(QtCore.QRect(20, 0, 110, 338))

        self.peso_max = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.peso_max.setFont(font)
        self.peso_max.setObjectName("peso_max")
        self.peso_max.setGeometry(QtCore.QRect(20, 0, 80, 423))

        self.codP = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.codP.setFont(font)
        self.codP.setObjectName("codP")
        self.codP.setGeometry(QtCore.QRect(200, 0, 110, 338))

        self.volumen_min = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.volumen_min.setFont(font)
        self.volumen_min.setObjectName("volumen_min")
        self.volumen_min.setGeometry(QtCore.QRect(1, 0, 95, 500 ))

        self.volumen_max = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.volumen_max.setFont(font)
        self.volumen_max.setObjectName("volumen_max")
        self.volumen_max.setGeometry(QtCore.QRect(200, 0, 120, 90 ))
        
        self.ganancia_min = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ganancia_min.setFont(font)
        self.ganancia_min.setObjectName("ganancia_min")
        self.ganancia_min.setGeometry(QtCore.QRect(200, 0, 110, 180))

        self.ganancia_max = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ganancia_max.setFont(font)
        self.ganancia_max.setObjectName("ganancia_max")
        self.ganancia_max.setGeometry(QtCore.QRect(200, 0, 110, 265))

        self.option1 = QtWidgets.QCheckBox(Form)
        self.option1.setGeometry(QtCore.QRect(230, 40, 163, 17))
        self.option1.setObjectName("option1")

        self.option2 = QtWidgets.QCheckBox(Form)
        self.option2.setGeometry(QtCore.QRect(230, 40, 163, 100))
        self.option2.setObjectName("option2")

        self.option3 = QtWidgets.QCheckBox(Form)
        self.option3.setGeometry(QtCore.QRect(230, 40, 163, 183))
        self.option3.setObjectName("option3")

        self.option4 = QtWidgets.QCheckBox(Form)
        self.option4.setGeometry(QtCore.QRect(230, 40, 150, 266))
        self.option4.setObjectName("option4")

        self.option5 = QtWidgets.QCheckBox(Form)
        self.option5.setGeometry(QtCore.QRect(20, 40, 163, 313))
        self.option5.setObjectName("option5")

        self.option6 = QtWidgets.QCheckBox(Form)
        self.option6.setGeometry(QtCore.QRect(120, 40, 163, 313))
        self.option6.setObjectName("option6")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Geneticos"))
        self.buttonSelect.setText(_translate("Form", "Ejecutar"))
        self.restriccionPeso.setText(_translate("Form", "Peso \n(KG): "))
        self.numeroElemento.setText(_translate("Form", "Altura \n(CM): "))
        self.restriccionVolumen.setText(_translate("Form", "Edad:  "))
        self.option1.setText(_translate('Form','Poco o ningun ejercicio.'))
        self.option2.setText(_translate('Form','Ejercicio ligero. \n(1-3 días a la semana)'))
        self.option3.setText(_translate('Form','Ejercicio Moderado. \n(3-5 días a la semana)'))
        self.option4.setText(_translate('Form','Ejercicio intenso. \n(6-7 días a la semana)'))
        self.option5.setText(_translate('Form','Hombre'))
        self.option6.setText(_translate('Form','Mujer'))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QFormDialog()
    ui = IForm()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

