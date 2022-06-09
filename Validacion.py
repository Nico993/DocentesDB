import string

ABC = list(string.ascii_uppercase)
ABC.append("Ñ")
ABC.append(" ")

class Validacion():

    def VerificarString(self,input):
        band = False
        if len(input) == 0:
            band = True
        else:
            for i in input:
                if(i.upper() not in ABC):
                    band = True
                    break
        return band

    def VerificarDocente(self,nombre,localidad,telefono):
        band1 = False
        band2 = False
        band = self.VerificarString(nombre)
        if(len(localidad) == 0):
            band1 = True
        try:
            telefono = int(telefono)
        except ValueError:
            band2 = True
        if(band == False and band1 == False and band2 == False):
            return True
        else:
            return False

    def VerificarMateria(self,nombre,carrera,docente):
        band1 = False
        band = self.VerificarString(nombre)
        if(len(carrera) == 0 or len(docente) == 0):
            band1 = True
        if(band == False and band1 == False):
            return True
        else:
            return False

    def VerificarLocalidad(self,id,nombre):
        band1 = False
        try:
            id = int(id)
        except ValueError:
            band1 = True
        band = self.VerificarString(nombre)
        if(band == False and band1 == False):
            return True
        else:
            return False

