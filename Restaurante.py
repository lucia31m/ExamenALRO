import mysql.connector

conexion = mysql.connector.connect(
     host = "localhost",
     user = "root",
     password = "123456789",
     database = "Restaurante"
 )

cursor = conexion.cursor
print("Bienvenido al sistema de Restaurante")
while True:
     print("1.Agregar Plato al menú")
     print ("2.Eliminar Plato del menú")
     print("3.Mostrar nenú")
     print("4.Salir")

     opcion = input("Indique el numero de la opcion que desea: ")

     if opcion == "1":
            plato = input("ingrese el nombre del libro que desea agregar: ")
            if plato :
                sql = "INSERT INTO plato  (nombre) VALUES (%s)"
                valores = (plato,)
                cursor.execute(sql, valores)
                conexion.commit()
                print("Se agrego el Plato al Menú")
            else:
                print("No se puedo agregar al menú")
     elif opcion == " 2":
         plato = input("Indique que plato desea eliminar: ")
         sql = "DELETE *FROM Platos "
         valores = (plato,)
         cursor.execute(sql, valores)
         conexion.commit()
         if cursor.rowcount > 0:
            print ( " El plato a sido eliminado del menú")
     else:
         print("No se encontro este plato en el menú")
     elif opcion == "3":
         sql = "SELECT Plato FROM Restaurante "
               print("Menu de restaurante:")





