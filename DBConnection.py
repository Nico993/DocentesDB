import pyodbc
import pandas as pd

class DataBase():
    def __init__(self):
        self.conn = pyodbc.connect("Driver={SQL Server};"
                        "Server=DESKTOP-V0UAET1;"
                        "Database=TpFinal1;"
                        "Trusted_Connection=yes;")

        self.cursor = self.conn.cursor()


    def InsertCarrera(self,nombre:str):
        self.cursor.execute(f"insert into Carrera (Nombre) values ('{nombre}')")
        self.cursor.commit()
        print("Fila en carrera insertada")

    def InsertLocalidad(self,id:int,nombre:str):
        self.cursor.execute(f"insert into Localidad values ({id},'{nombre}')")
        self.cursor.commit()
        print("Fila en localidad insertada")

    def InsertDocente(self,nombre,domicilio,localidad,telefono):
        df = self.SelectLocalidad()
        id = df[df["Nombre"]==localidad].index.values
        IdLocalidad = df.loc[id,"Id"]
        self.cursor.execute(f"insert into Docente(Nombre,Domicilio,IdLocalidad,Telefono) values ('{nombre}','{domicilio}',{int(IdLocalidad)},{telefono})")
        self.cursor.commit()
        print("Fila en Docente insertada")

    def InsertMateria(self,nombre,carrera,docente):
        dfCarrera = self.SelectCarrera()
        dfDocente = self.SelectDocente()
        IdCarrera = dfCarrera[dfCarrera["Nombre"] == carrera].index.values
        IdCarrera = dfCarrera.loc[IdCarrera,"Id"]
        IdDocente = dfDocente[dfDocente["Nombre"] == docente].index.values
        IdDocente = dfDocente.loc[IdDocente,"Id"]
        self.cursor.execute(f"insert into Materia(Nombre,IdCarrera,IdDocente) values ('{nombre}',{int(IdCarrera)},{int(IdDocente)})")
        self.cursor.commit()
        print("Fila en Materia creada")

    def SelectCarrera(self):
        df = pd.read_sql_query("select * from Carrera",self.conn)
        return df
        
    def SelectLocalidad(self):
        df = pd.read_sql_query("select * from Localidad",self.conn)
        return df

    def SelectDocente(self):
        df = pd.read_sql_query("select * from Docente",self.conn)
        return df
    
    def SelectMateria(self):
        df = pd.read_sql_query("select * from Materia",self.conn)
        return df
    
    def ActualizarDocente(self,id,nombre,domicilio,localidad,telefono):
        df = self.SelectLocalidad()
        idLocalidad = df[df["Nombre"]==localidad].index.values
        IdLocalidad = df.loc[idLocalidad,"Id"]
        self.cursor.execute(f"update Docente set Nombre = '{nombre}', Domicilio = '{domicilio}', Idlocalidad = {int(IdLocalidad)}, Telefono = {int(telefono)} where Id = {int(id)}")
        self.cursor.commit()
        print("Fila Docente Actualizada")
    
    def EliminarDocente(self,id):
        self.cursor.execute(f"delete from Docente where id = {int(id)}")
        self.cursor.commit()
        print("Fila Docente Eliminada")

    def ActualizarMateria(self,id,nombre,carrera,docente):
        dfCarrera = self.SelectCarrera()
        dfDocente = self.SelectDocente()
        IdCarrera = dfCarrera[dfCarrera["Nombre"] == carrera].index.values
        IdCarrera = dfCarrera.loc[IdCarrera,"Id"]
        IdDocente = dfDocente[dfDocente["Nombre"] == docente].index.values
        IdDocente = dfDocente.loc[IdDocente,"Id"]
        self.cursor.execute(f"update Materia set Nombre = '{nombre}', IdCarrera = {int(IdCarrera)}, IdDocente = {int(IdDocente)} where Id = {int(id)}")
        self.cursor.commit()
        print("Fila Materia Actualizada")
    
    def EliminarMateria(self,id):
        self.cursor.execute(f"delete from Materia where id = {int(id)}")
        self.cursor.commit()
        print("Fila Materia Eliminada")



    def Consulta_a(self):
        df = pd.read_sql_query("select  materia.id as idmateria, materia.nombre as nombreMateria, carrera.id as idCarrera, carrera.nombre as nombreCarrera, docente.id as idDocente, docente.nombre as nombreDocente from materia inner join carrera on materia.idcarrera = carrera.id inner join docente on materia.iddocente = docente.id order by carrera.id;",self.conn)
        return df
    
    def Consulta_b(self):
        df = pd.read_sql_query("select  materia.id as idmateria, materia.nombre as nombreMateria, carrera.id as idCarrera, carrera.nombre as nombreCarrera, docente.id as idDocente, docente.nombre as nombreDocente from materia inner join carrera on materia.idcarrera = carrera.id inner join docente on materia.iddocente = docente.id order by docente.id,materia.id;",self.conn)
        return df
    
    def Consulta_c(self):
        df = pd.read_sql_query("select count(materia.id) as cantidad, carrera.nombre  from materia inner join carrera on materia.idcarrera = carrera.id group by carrera.nombre;",self.conn)
        return df

    def Consulta_d(self):
        df = pd.read_sql_query("select count(materia.id) as cantidad, docente.nombre from materia inner join docente on materia.iddocente = docente.id group by docente.nombre;",self.conn)
        return df

    def Consulta_e(self):
        df = pd.read_sql_query("select materia.nombre as 'nombre materia', docente.nombre as 'nombre docente', localidad.nombre as 'nombre localidad', docente.telefono from materia inner join docente on materia.iddocente = docente.id inner join localidad on docente.idlocalidad = localidad.id order by materia.nombre;",self.conn)
        return df

    def Consulta_f(self):
        df = pd.read_sql_query("select localidad.nombre as 'nombre localidad' from localidad left join docente on localidad.id = docente.idlocalidad where docente.idlocalidad is null;",self.conn)
        return df

    def Consulta_g(self):
        df = pd.read_sql_query("select docente.nombre, localidad.id from docente inner join localidad on docente.idlocalidad = localidad.id where localidad.id = 2400 union select docente.nombre, localidad.id from docente inner join localidad on docente.idlocalidad = localidad.id where localidad.id = 5000;",self.conn)
        return df

    def CloseConnection(self):
        self.cursor.close()
        self.conn.close()