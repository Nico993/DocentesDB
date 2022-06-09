import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog
from PyQt5.uic import loadUi
from DBConnection import *
from Validacion import *
from SetItems import *

db = DataBase()
validador = Validacion()
gestor = Gestor()

class Menu(QMainWindow):
    def __init__(self):
        super(Menu,self).__init__()
        loadUi("Menu.ui",self)
        self.BtnDocente.clicked.connect(self.DocenteFunction)
        self.BtnCarrera.clicked.connect(self.CarreraFunction)
        self.BtnMateria.clicked.connect(self.MateriaFunction)
        self.BtnLocalidad.clicked.connect(self.LocalidadFunction)
        self.BtnConsultas.clicked.connect(self.ConsultasFunction)


    def DocenteFunction(self):
        docente = Docente()
        widget.addWidget(docente)
        widget.setFixedWidth(900)
        widget.setFixedHeight(600)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def CarreraFunction(self):
        carrera = Carrera()
        widget.addWidget(carrera)
        widget.setFixedWidth(600)
        widget.setFixedHeight(600)
        widget.setCurrentIndex(widget.currentIndex() + 1)
    
    def MateriaFunction(self):
        materia = Materia()
        widget.addWidget(materia)
        widget.setFixedWidth(800)
        widget.setFixedHeight(600)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def LocalidadFunction(self):
        localidad = Localidad()
        widget.addWidget(localidad)
        widget.setFixedWidth(600)
        widget.setFixedHeight(600)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def ConsultasFunction(self):
        consultas = Consultas()
        widget.addWidget(consultas)
        widget.setFixedWidth(600)
        widget.setFixedHeight(600)
        widget.setCurrentIndex(widget.currentIndex() + 1)





class Docente(QDialog):
    def __init__(self):
        super(Docente,self).__init__()
        loadUi("Docente.ui",self)
        self.labelError.hide()
        self.labelError_2.hide()
        self.labelError_3.hide()
        self.BtnVolver.clicked.connect(self.VolverFunction)
        self.BtnGuardar.clicked.connect(self.GuardarFunction)
        self.BtnActualizar.clicked.connect(self.ActualizarFunction)
        self.BtnRegistrar.clicked.connect(self.RegistrarFunction)
        self.BtnEliminar.clicked.connect(self.EliminarFunction)
        self.BtnActualizar_2.clicked.connect(self.Actualizar_2Function)
        self.BtnEliminar_2.clicked.connect(self.Eliminar_2Function)
        self.SetComboBoxLocalidad()
        self.ShowDocentes()
        self.stackedWidget.setCurrentIndex(0)

    def VolverFunction(self):
        menu = Menu()
        widget.addWidget(menu)
        widget.setFixedWidth(600)
        widget.setFixedHeight(600)
        widget.setCurrentIndex(widget.currentIndex() + 1)


    def SetComboBoxLocalidad(self):
        df = db.SelectLocalidad()
        gestor.SetComboBox(df,self.comboBoxLocalidad,1)

    def GuardarFunction(self):
        nombre = self.lineEditNombre.text()
        domicilio = self.lineEditDomicilio.text()
        localidad = self.comboBoxLocalidad.currentText()
        telefono = self.lineEditTelefono.text()
        band = validador.VerificarDocente(nombre,localidad,telefono)

        if(band):
            self.labelError.hide()
            db.InsertDocente(nombre,domicilio,localidad,telefono)
        else:
            self.labelError.show()
        self.lineEditNombre.clear()
        self.lineEditDomicilio.clear()
        self.lineEditTelefono.clear()
        self.comboBoxLocalidad.setCurrentIndex(-1)

    def ShowDocentes(self):
        df = db.SelectDocente()
        gestor.CreateTable(df,self.tableWidget)
        gestor.InsertTableItems(self.tableWidget,df)
    
    def ActualizarFunction(self):
        self.stackedWidget.setCurrentIndex(1)
        self.SetComboBoxActualizarLocalidad()
        self.SetComboBoxActualizarId()
    
    def RegistrarFunction(self):
        self.stackedWidget.setCurrentIndex(0)

    def EliminarFunction(self):
        self.stackedWidget.setCurrentIndex(2)
        self.SetComboBoxEliminarId()

    def SetComboBoxActualizarId(self):
        df = db.SelectDocente()
        gestor.SetComboBox(df,self.comboBoxActualizarId,0)

    def SetComboBoxActualizarLocalidad(self):
        df = db.SelectLocalidad()
        gestor.SetComboBox(df,self.comboBoxActualizarLocalidad,1)
    
    def SetComboBoxEliminarId(self):
        df = db.SelectDocente()
        gestor.SetComboBox(df,self.comboBoxEliminarId,0)

    def Actualizar_2Function(self):
        id = self.comboBoxActualizarId.currentText()
        nombre = self.lineEditNombre_2.text()
        domicilio = self.lineEditDomicilio_2.text()
        localidad = self.comboBoxActualizarLocalidad.currentText()
        telefono = self.lineEditTelefono_2.text()
        band = validador.VerificarDocente(nombre,localidad,telefono)
        if(band == True and len(id) != 0):
            self.labelError_2.hide()
            db.ActualizarDocente(id,nombre,domicilio,localidad,telefono)
        else:
            self.labelError_2.show() 
        self.lineEditNombre_2.clear()
        self.lineEditDomicilio_2.clear()
        self.lineEditTelefono_2.clear()
        self.comboBoxActualizarLocalidad.setCurrentIndex(-1)
        self.comboBoxActualizarId.setCurrentIndex(-1)
    
    def Eliminar_2Function(self):
        id = self.comboBoxEliminarId.currentText()
        if(len(id)!= 0):
            self.labelError_3.hide()
            db.EliminarDocente(id)
        else:
            self.labelError_3.show()
        self.comboBoxEliminarId.setCurrentIndex(-1)




class Materia(QDialog):
    def __init__(self):
        super(Materia,self).__init__()
        loadUi("Materia.ui",self)
        self.labelError.hide()
        self.labelError_2.hide()
        self.labelError_3.hide()
        self.BtnVolver.clicked.connect(self.VolverFunction)
        self.BtnGuardar.clicked.connect(self.GuardarFunction)
        self.BtnActualizar.clicked.connect(self.ActualizarFunction)
        self.BtnRegistrar.clicked.connect(self.RegistrarFunction)
        self.BtnEliminar.clicked.connect(self.EliminarFunction)
        self.BtnActualizar_2.clicked.connect(self.Actualizar_2Function)
        self.BtnEliminar_2.clicked.connect(self.Eliminar_2Function)
        self.SetComboBoxCarrera()
        self.SetComboBoxDocente()
        self.ShowMaterias()
        self.stackedWidget.setCurrentIndex(0)
    
    def VolverFunction(self):
        menu = Menu()
        widget.addWidget(menu)
        widget.setFixedWidth(600)
        widget.setFixedHeight(600)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def SetComboBoxCarrera(self):
        df = db.SelectCarrera()
        gestor.SetComboBox(df,self.comboBoxCarrera,1)

    def SetComboBoxDocente(self):
        df = db.SelectDocente()
        gestor.SetComboBox(df,self.comboBoxDocente,1)

    def GuardarFunction(self):
        nombre = self.lineEditNombre.text()
        carrera = self.comboBoxCarrera.currentText()
        docente = self.comboBoxDocente.currentText()
        band = validador.VerificarMateria(nombre,carrera,docente)
        if(band):
            self.labelError.hide() 
            db.InsertMateria(nombre,carrera,docente)
        else:
            self.labelError.show()
        self.lineEditNombre.clear()
        self.comboBoxCarrera.setCurrentIndex(-1)
        self.comboBoxDocente.setCurrentIndex(-1)

    def ShowMaterias(self):
        df = db.SelectMateria()
        gestor.CreateTable(df,self.tableWidget)
        gestor.InsertTableItems(self.tableWidget,df)
    
    def ActualizarFunction(self):
        self.stackedWidget.setCurrentIndex(1)
        self.SetComboBoxActualizarId()
        self.SetComboBoxActualizarCarrera()
        self.SetComboBoxActualizarDocente()
    def RegistrarFunction(self):
        self.stackedWidget.setCurrentIndex(0)
    def EliminarFunction(self):
        self.stackedWidget.setCurrentIndex(2)
        self.SetComboBoxEliminarId()

    def SetComboBoxActualizarId(self):
        df = db.SelectMateria()
        gestor.SetComboBox(df,self.comboBoxActualizarId,0)
    def SetComboBoxActualizarCarrera(self):
        df = db.SelectCarrera()
        gestor.SetComboBox(df,self.comboBoxActualizarCarrera,1)
    def SetComboBoxActualizarDocente(self):
        df = db.SelectDocente()
        gestor.SetComboBox(df,self.comboBoxActualizarDocente,1)
    def SetComboBoxEliminarId(self):
        df = db.SelectMateria()
        gestor.SetComboBox(df,self.comboBoxEliminarId,0)

    def Actualizar_2Function(self):
        id = self.comboBoxActualizarId.currentText()
        nombre = self.lineEditNombre_2.text()
        carrera = self.comboBoxActualizarCarrera.currentText()
        docente = self.comboBoxActualizarDocente.currentText()
        band = validador.VerificarMateria(nombre,carrera,docente)
        if(band == True and len(id) != 0):
            self.labelError_2.hide()
            db.ActualizarMateria(id,nombre,carrera,docente)
        else:
            self.labelError_2.show()
        self.comboBoxActualizarId.setCurrentIndex(-1)
        self.comboBoxActualizarCarrera.setCurrentIndex(-1)
        self.comboBoxActualizarDocente.setCurrentIndex(-1)
        self.lineEditNombre_2.clear()
    def Eliminar_2Function(self):
        id = self.comboBoxEliminarId.currentText()
        if(len(id)!= 0):
            self.labelError_3.hide()
            db.EliminarMateria(id)
        else:
            self.labelError_3.show()
        self.comboBoxEliminarId.setCurrentIndex(-1)



        



class Carrera(QDialog):
    def __init__(self):
        super(Carrera,self).__init__()
        loadUi("Carrera.ui",self)
        self.labelError.hide()
        self.BtnVolver.clicked.connect(self.VolverFunction)
        self.BtnGuardar.clicked.connect(self.GuardarFunction)
        self.showCarrera()
    
    def VolverFunction(self):
        menu = Menu()
        widget.addWidget(menu)
        widget.setFixedWidth(600)
        widget.setFixedHeight(600)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def GuardarFunction(self):
        nombre = self.lineEditNombre.text()
        band = validador.VerificarString(nombre)
        if(band == False):
            db.InsertCarrera(nombre)
            self.labelError.hide()
        else:
            self.labelError.show()
        self.lineEditNombre.clear()

    def showCarrera(self):
        df = db.SelectCarrera()
        gestor.CreateTable(df,self.tableWidget)
        gestor.InsertTableItems(self.tableWidget,df)


class Localidad(QDialog):
    def __init__(self):
        super(Localidad,self).__init__()
        loadUi("Localidad.ui",self)
        self.labelError.hide()
        self.BtnVolver.clicked.connect(self.VolverFunction)
        self.BtnGuardar.clicked.connect(self.GuardarFunction)
        self.ShowLocalidad()
        

    def GuardarFunction(self):
        id = self.lineEditCodigoPostal.text()
        nombre = self.lineEditNombre.text()
        band = validador.VerificarLocalidad(id,nombre)
        if(band):
            self.labelError.hide()  
            db.InsertLocalidad(int(id),nombre)
        else:
            self.labelError.show()
        self.lineEditNombre.clear()
        self.lineEditCodigoPostal.clear()


        
    def VolverFunction(self):
        menu = Menu()
        widget.addWidget(menu)
        widget.setFixedWidth(600)
        widget.setFixedHeight(600)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def ShowLocalidad(self):
        df = db.SelectLocalidad()
        gestor.CreateTable(df,self.tableWidget)
        gestor.InsertTableItems(self.tableWidget,df)

        
class Consultas(QDialog):
    def __init__(self):
        super(Consultas,self).__init__()
        loadUi("Consultas.ui",self)
        self.ConsultaA()
        self.BtnVolver.clicked.connect(self.VolverFunction)
        self.tabWidget.tabBarClicked.connect(self.tabBarFunction)

    
    def VolverFunction(self):
        menu = Menu()
        widget.addWidget(menu)
        widget.setFixedWidth(600)
        widget.setFixedHeight(600)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def tabBarFunction(self,index):
        if(index == 0):
            self.ConsultaA()
        elif(index == 1):
            self.ConsultaB()
        elif(index == 2):
            self.ConsultaC()
        elif(index == 3):
            self.ConsultaD()
        elif(index == 4):
            self.ConsultaE()
        elif(index == 5):
            self.ConsultaF()
        elif(index == 6):
            self.ConsultaG()

    def ConsultaA(self):
        df = db.Consulta_a()
        gestor.CreateTable(df,self.tableWidgetA)
        gestor.InsertTableItems(self.tableWidgetA,df)

    def ConsultaB(self):
        df = db.Consulta_b()
        gestor.CreateTable(df,self.tableWidgetB)
        gestor.InsertTableItems(self.tableWidgetB,df)

    def ConsultaC(self):
        df = db.Consulta_c()
        gestor.CreateTable(df,self.tableWidgetC)
        gestor.InsertTableItems(self.tableWidgetC,df)

    def ConsultaD(self):
        df = db.Consulta_d()
        gestor.CreateTable(df,self.tableWidgetD)
        gestor.InsertTableItems(self.tableWidgetD,df)

    def ConsultaE(self):
        df = db.Consulta_e()
        gestor.CreateTable(df,self.tableWidgetE)
        gestor.InsertTableItems(self.tableWidgetE,df)

    def ConsultaF(self):
        df = db.Consulta_f()
        gestor.CreateTable(df,self.tableWidgetF)
        gestor.InsertTableItems(self.tableWidgetF,df)

    def ConsultaG(self):
        df = db.Consulta_g()
        gestor.CreateTable(df,self.tableWidgetG)
        gestor.InsertTableItems(self.tableWidgetG,df)
    













app = QApplication(sys.argv)
MainWindow = Menu()
widget = QtWidgets.QStackedWidget()
widget.addWidget(MainWindow)
widget.setFixedWidth(600)
widget.setFixedHeight(600)
widget.show()
app.exec_()

db.CloseConnection()