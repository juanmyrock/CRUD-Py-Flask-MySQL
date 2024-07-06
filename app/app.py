

from config import *

class crudpython:
    
    # Constructor de la clase
    def __init__(self, host, user, password, myapp_python):
        # Primero, establecemos una conexión sin especificar la base de datos
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password
        )
        self.cursor = self.conn.cursor()

        # Intentamos seleccionar la base de datos
        try:
            self.cursor.execute(f"USE {myapp_python}")
        except mysql.connector.Error as err:
            # Si la base de datos no existe, la creamos
            if err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
                self.cursor.execute(f"CREATE DATABASE {myapp_python}")
                self.conn.database = myapp_python
            else:
                raise err

        # Una vez que la base de datos está establecida, creamos las tablas si no existe
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS `familias` (
            `id_familia` int AUTO_INCREMENT PRIMARY KEY,
            `familia` varchar(255) NOT NULL)''')
        self.conn.commit()

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS `usuarios` (
            `id_usuario` int AUTO_INCREMENT PRIMARY KEY,
            `id_familia` int,
            `username` varchar(255) NOT NULL,
            `password` varchar(255) NOT NULL,
            `mail` varchar(255) NOT NULL,
            `nombre` varchar(255) NOT NULL,
            `apellido` varchar(255) NOT NULL,
            FOREIGN KEY (`id_familia`) REFERENCES `familias`(`id_familia`))''') 
        self.conn.commit()

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS `artistas` (
            `id_artista` int AUTO_INCREMENT PRIMARY KEY,
            `nombre` varchar(255) NOT NULL,
            `apellido` varchar(255) NOT NULL,
            `nacionalidad` varchar(255) NOT NULL,
            `genero` varchar(255) NOT NULL,
            `edad` int NOT NULL)''') 
        self.conn.commit()

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS `tickets` (
            `id_ticket` int AUTO_INCREMENT PRIMARY KEY,
            `id_usuario` int,
            `id_artista` int,
            `nombre` varchar(255) NOT NULL,
            `apellido` varchar(255) NOT NULL,
            `mail` varchar(255) NOT NULL,
            `cantidad` int NOT NULL,
            `categoria` varchar(255) NOT NULL,
            `files` LONGBLOB,
            FOREIGN KEY (`id_usuario`) REFERENCES `usuarios`(`id_usuario`),
            FOREIGN KEY (`id_artista`) REFERENCES `artistas`(`id_artista`))''')
        self.conn.commit()

        # Cerrar el cursor inicial y abrir uno nuevo con el parámetro dictionary=True
        self.cursor.close()
        self.cursor = self.conn.cursor(dictionary=True)

#----------------------------------------------------------------
# se hacen los insert

    def agregar_usuario (self, id_familia, username, password, mail, nombre, apellido ):
               
        sql = "INSERT INTO usuarios (id_familia, username, password, mail, nombre, apellido) VALUES (%s, %s, %s, %s, %s)"
        valores = (id_familia, username, password, mail, nombre, apellido)

        self.cursor.execute(sql, valores)        
        self.conn.commit()
        return self.cursor.lastrowid


    def agregar_artista(self, nombre, apellido, nacionalidad, genero, edad):

        sql = "INSERT INTO artistas (nombre, apellido, nacionalidad, genero, edad) VALUES (%s, %s, %s, %s, %s)"
        valores = (nombre, apellido, nacionalidad, genero, edad)

        self.cursor.execute(sql, valores)        
        self.conn.commit()
        return self.cursor.lastrowid

    def agregar_ticket (self, id_usuario, id_artista, nombre, apellido, mail, cantidad, categoria, files):

        sql = "INSERT INTO tickets (id_usuario, id_artista, nombre, apellido, mail, cantidad, categoria, files) VALUES (%s, %s, %s, %s, %s)"
        valores = (id_usuario, id_artista, nombre, apellido, mail, cantidad, categoria, files)

        self.cursor.execute(sql, valores)        
        self.conn.commit()
        return self.cursor.lastrowid


# No estoy muy segura de si se puede hacer esto acá jaja 
    def agregar_familia(self, familia):

        sql = "INSERT INTO familias (familia) VALUES ('admin')"
        valores = (familia)

        sql = "INSERT INTO familias (familia) VALUES ('usuario')"
        valores = (familia)

        self.cursor.execute(sql, valores)        
        self.conn.commit()
        return self.cursor.lastrowid
  
#----------------------------------------------------------------
# consultar tablas 

    def consultar_usuarios(self, id_usuario):
        self.cursor.execute(f"SELECT * FROM usuarios WHERE id_usuario = {id_usuario}")
        return self.cursor.fetchone()
    
    def consultar_artistas(self, id_artista):
        self.cursor.execute(f"SELECT * FROM usuarios WHERE id_artista = {id_artista}")
        return self.cursor.fetchone()

    def consultar_tickets(self, id_ticket):
        self.cursor.execute(f"SELECT * FROM usuarios WHERE id_ticket = {id_ticket}")
        return self.cursor.fetchone()
#----------------------------------------------------------------
# faltaria hacer el join pero aun no se bien si resolvi la creación de las tabla "familia" con exito
# Modificar registros 

    def modificar_usuarios(self, id_familia, id_usuario, username, nuevo_password, nuevo_nombre, nuevo_apellido, nuevo_email):
        sql = "UPDATE myapp_python SET usuarios = %s, nuevo_password = %s, nuevo_nombre = %s, nuevo_apellido = %s, nuevo_email = %s WHERE codigo = %s"
        valores = (nuevo_password, nuevo_nombre, nuevo_apellido, nuevo_email, id_familia, id_usuario, username)
        self.cursor.execute(sql, valores)
        self.conn.commit()
        return self.cursor.rowcount > 0
    
    def modificar_tickets(self, id_ticket, id_usuario, nuevo_artista, nueva_cantidad, nueva_categoria):
        sql = "UPDATE myapp_python SET tickets = %s, nuevo_artista = %s, nueva_cantidad = %s, nueva_categoria = %s, WHERE codigo = %s"
        valores = (id_ticket, id_usuario, nuevo_artista, nueva_cantidad, nueva_categoria)
        self.cursor.execute(sql, valores)
        self.conn.commit()
        return self.cursor.rowcount > 0

    def modificar_artistas(self, id_artista,  nuevo_nombre, nuevo_apellido, nueva_nacionalidad, nueva_edad, nuevo_genero ):
        sql = "UPDATE myapp_python SET artistas = %s, nombre = %s, apellido = %s, nacionalidad = %s, edad = %s, genero = %s WHERE codigo = %s"
        valores = (id_artista, nuevo_nombre, nuevo_apellido, nueva_nacionalidad, nueva_edad, nuevo_genero)
        self.cursor.execute(sql, valores)
        self.conn.commit()
        return self.cursor.rowcount > 0
#----------------------------------------------------------------
# mostrar tablas 

    def listar_usuarios(self):
        self.cursor.execute("SELECT * FROM usuarios")
        usuarios = self.cursor.fetchall()
        return usuarios
    
    def listar_tickes(self):
        self.cursor.execute("SELECT * FROM tickets")
        tickets = self.cursor.fetchall()
        return tickets

    def listar_artistas(self):
        self.cursor.execute("SELECT * FROM artistas")
        artistas = self.cursor.fetchall()
        return artistas
#----------------------------------------------------------------
#eliminar registros en las tablas 

def eliminar_usuario(self, id_usuario):
        # Eliminamos un producto de la tabla a partir de su código
        self.cursor.execute(f"DELETE FROM usuarios WHERE id_usuario = {id_usuario}")
        self.conn.commit()
        return self.cursor.rowcount > 0

def eliminar_ticket(self, id_ticket):
        # Eliminamos un producto de la tabla a partir de su código
        self.cursor.execute(f"DELETE FROM tickets WHERE id_usuario = {id_ticket}")
        self.conn.commit()
        return self.cursor.rowcount > 0

def eliminar_artista(self, id_artista):
        # Eliminamos un producto de la tabla a partir de su código
        self.cursor.execute(f"DELETE FROM artistas WHERE id_artista = {id_artista}")
        self.conn.commit()
        return self.cursor.rowcount > 0

#----------------------------------------------------------------