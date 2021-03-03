import mysql.connector

class Libro:
    def abrir (self):
        conexion = mysql.connector.connect(host="localhost",
                                           user="root",
                                           passwd="",
                                           database="libreria")
        return conexion
    
    def insert (self, datos):
        cone = self.abrir()
        cursor = cone.cursor()          
        sql = "INSERT INTO clientes(Documento, Nombre, Apellido, Direccion, Ciudad, Codigo_Postal) VALUES (%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql, datos)      
        cone.commit()                  
        cone.close()

    def insert_ord (self, datos):
        try:
            cone = self.abrir()
            cursor = cone.cursor()
            sql = "INSERT INTO ordenes(Documento, Id_libro) VALUES (%s,%s)"
            cursor.execute(sql, datos)
            print(cursor)
            cone.commit()
            cone.close()
            return True

        except Exception as ex:
            print(ex)
            return False

    def retrieve_all(self):
        cone = self.abrir()
        cursor = cone.cursor()      
        sql = "SELECT Id_libro,Titulo,Nom_Autor,Categoria,Precio FROM libros"
        cursor.execute(sql)         
        cone.close()                
        return cursor.fetchall()

    def retrieve_all_ordenes(self):
        cone = self.abrir()
        cursor = cone.cursor()      
        sql = "SELECT Id_orden,clientes.Documento,Nombre,Apellido,Titulo,Nom_Autor,Precio,Fecha_Orden  FROM ordenes,clientes,libros WHERE ordenes.Documento = clientes.Documento AND ordenes.Id_libro = libros.Id_libro"
        cursor.execute(sql)         
        cone.close()                
        return cursor.fetchall()    