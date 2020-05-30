import os
import sys
import pymysql
#Universidad Mariano Galvez de Guatemala, extension Chimaltenango. 
#Programacion 1, Ingeniero Haroldo Turcios
#Programadores: 
# Kevin Gudiel Sequen Sal Carné: 1990-15-17463
# Jose ELias Jonathan Xia Zamora Carné: 1990-19-24815
# Jairo Vinicio Damian Pellecer Carné: 1990-17-16458
# Lester Oswaldo Martínez Morales Carné: 1990-19-7786
# Diego Antonio Martinez Yucute Carné: 1990-19-17123
# Yeison Arnoldo Cum Yaqui Carné: 1990-19-12072
#Fecha: 30 de mayo de 2020
#Lugar:Chimaltenango, Guatemala
#Este proyecto lo trabajamos en equipo.

#Boutique Fashion Python
#Programa permite el ingreso de prendas por medio de los proveedores
#Permite llevar el registro de todos los clientes 
#Permite facturar
#Podemos modificar y eliminar registros
#Todos los datos son almacenados en una base de datos en SQL

def Clientes(): #Creado por Kevin Gudiel Sequen Sal
	os.system("cls")
	print("--Agregar cliente--")
	print("")

	codigo = input("Digite el codigo del cliente: ")
	nombre = input("Digite el nombre del cliente: ")
	apellido = input("Digite el apellido del cliente: ")
	direccion = input("Digite la direcion: ")
	telefono = input("Digite numero de telefono: ")
	fecha = input("Digite la fecha: ")

	connection = pymysql.connect( #Conexion con mysql
		host="localhost",
		user="root",
		password="",
		db="Proyecto"
	)

	cursor = connection.cursor()
	
	sql = "INSERT INTO cliente (codigo, nombre, apellido, direccion, telefono, fecha) VALUES (%s, %s, %s, %s, %s, %s)" #Guardamos en la base de datos
	cursor.execute(sql,(codigo, nombre, apellido, direccion, telefono, fecha))
	connection.commit()

	print("[m] Volver al menu.")
	print("[s] Salir.")

	opcion = input("Digite una opcion: ")

	if opcion == "m":
		menu()
	elif opcion == "s":
		sys.exit()
		
def Encargado(): #Creado por Lester Oswaldo Martínez Morales 
	os.system("cls")
	print("--Encargado--")
	print("")

	codigo = input("Digite el codigo del encargado: ")
	nombre = input("Digite su nombre: ")
	apellido = input("Digite su apellido: ")
	direccion = input("Digite su direccion: ")
	telefono = input("Digite su telefono: ")
	correo = input("Digite su correo electronico: ")

	connection = pymysql.connect(
		host="localhost",
		user="root",
		password="",
		db="proyecto"
	)

	cursor = connection.cursor()
	
	sql = "INSERT INTO encargado (codigo, nombre, apellido, direccion, telefono, correo) VALUES (%s, %s, %s, %s, %s, %s)"
	cursor.execute(sql,(codigo, nombre, apellido, direccion, telefono, correo))
	connection.commit()

	print("[m] Volver al menu.")
	print("[s] Salir.")

	opcion = input("Digite una opcion: ")

	if opcion == "m":
		menu()
	elif opcion == "s":
		sys.exit()

def Producto(): #Creado por Arnoldo saber que mas 
	os.system("cls")
	print("--INGRESAR PRODUCTOS--")
	print("")

	codigo = input("Digite el codigo del producto: ")
	descripcion = input("descripcion del producto: ")
	precio = input("costo: ")
	observacion = input("alguna observacion: ")

	connection = pymysql.connect(
		host="localhost",
		user="root",
		password="",
		db="proyecto"
	)

	cursor = connection.cursor()
	
	sql = "INSERT INTO producto (codigo, descripcion, precio, observacion) VALUES (%s, %s, %s, %s)"
	cursor.execute(sql,(codigo,descripcion,precio,observacion))
	connection.commit()

	print("[m] Volver al menu.")
	print("[s] Salir.")

	opcion = input("Digite una opcion: ")

	if opcion == "m":
		menu()
	elif opcion == "s":
		sys.exit()

def proveedor(): #Creado por Jairo Vinicio Damian Pellecer
	os.system("cls")
	print("--PROVEEDORES--")
	print("")

	codigo = input("Digite el codigo del proveedor: ")
	nombre = input("Digite el nombre del proveedor: ")
	apellido = input("Digite el apellido del proveedor: ")
	direccion = input("Digite la direcion del proveedor: ")
	producto = input("Digite el producto: ")
	telefono = input("Digite su numero de telefono: ")
	observacion = input("Digite alguna observacion: ")

	connection = pymysql.connect(
		host="localhost",
		user="root",
		password="",
		db="proyecto"
	)

	cursor = connection.cursor()
	
	sql = "INSERT INTO proveedor (codigo, nombre, apellido, direccion, producto, telefono, observacion) VALUES (%s, %s, %s, %s, %s, %s, %s)"
	cursor.execute(sql,(codigo, nombre, apellido, direccion, producto, telefono, observacion))
	connection.commit()

	print("[m] Volver al menu.")
	print("[s] Salir.")

	opcion = input("Digite una opcion: ")

	if opcion == "m":
		menu()
	elif opcion == "s":
		sys.exit()

def mostrar_clientes(): #Creado por Jose Elias Xia Zamora
	os.system("cls")
	print("--LISTADO DE CLIENTES--")
	print("")

	connection = pymysql.connect(
		host="localhost",
		user="root",
		password="",
		db="proyecto"
	)

	cursor = connection.cursor()
	
	sql = "SELECT * FROM cliente  "
	cursor.execute(sql)
	#connection.commit()
	resultado = cursor.fetchall()

	for datos in resultado:
		print("|Codigo|  |Nombre|  |Apellido|  |Direccion|  |Telefono|  |Fecha|")
		print("_______________________________________________________________________")
		print(datos)
		print("")
	print("")
	print("[m] Volver al menu.")
	print("[s] Salir.")

	opcion = input("Digite una opcion: ")

	if opcion == "m":
		menu()
	elif opcion == "s":
		sys.exit()

def mostrar_encargado(): #Creado por Lester Oswaldo Martinez Morales
	os.system("cls")
	print("--ENCARGADOS DE BOUTIQUE--")
	print("")

	connection = pymysql.connect(
		host="localhost",
		user="root",
		password="",
		db="proyecto"
	)

	cursor = connection.cursor()
	
	sql = "SELECT * FROM encargado  "
	cursor.execute(sql)
	#connection.commit()
	resultado = cursor.fetchall()

	for datos in resultado:
		print("|Codigo|  |Nombre|  |Apellido|  |Direccion|  |Telefono|  |Correo|")
		print("_______________________________________________________________________")
		print(datos)
	print("")
	print("[m] Volver al menu.")
	print("[s] Salir.")

	opcion = input("Digite una opcion: ")

	if opcion == "m":
		menu()
	elif opcion == "s":
		sys.exit()

def mostrar_producto(): #Creado por Jose Elias Xia Zamora
	os.system("cls")
	print("--LISTADO DE PRODUCTOS--")
	print("")

	connection = pymysql.connect(
		host="localhost",
		user="root",
		password="",
		db="proyecto"
	)

	cursor = connection.cursor()
	
	sql = "SELECT * FROM producto  "
	cursor.execute(sql)
	#connection.commit()
	resultado = cursor.fetchall()

	for datos in resultado:
		print("|Codigo|  |Descripcion|  |Percio|  |Observacion| ")
		print("_________________________________________________")
		print(datos)
	print("")
	print("[m] Volver al menu.")
	print("[s] Salir.")
 
	opcion = input("Digite una opcion: ")

	if opcion == "m":
		menu()
	elif opcion == "s":
		sys.exit()

def mostrar_proveedor(): #Creado por Jario Vinicio Damian Pellecer
	os.system("cls")
	print("--PROVEEDORES REGISTRADOS--")
	print("")

	connection = pymysql.connect(
		host="localhost",
		user="root",
		password="",
		db="proyecto"
	)

	cursor = connection.cursor()
	
	sql = "SELECT * FROM proveedor  "
	cursor.execute(sql)
	#connection.commit()
	resultado = cursor.fetchall()

	for datos in resultado:
		print("|Codigo|  |Nombre|  |Apellido|  |Direccion|  |Producto|  |Fecha|  |Observacion|")
		print("_______________________________________________________________________________")
		print(datos)
	print("")
	print("[m] Volver al menu.")
	print("[s] Salir.")

	opcion = input("Digite una opcion: ")

	if opcion == "m":
		menu()
	elif opcion == "s":
		sys.exit()

def modificar_cliente(): #Creado por Kevin Gudiel Sequen Sal
	os.system("cls")
	print("--modificar cliente--")
	print("")

	codigo = input("Digite el codigo del cliente: ")
	nombre = input("Digite el nuevo nombre del cliente: ")
	apellido = input("Digite el nuevo apellido del cliente : ")
	direccion = input("Digite la nueva direccion del cliente : ")
	telefono = input("Digite el nuevo telefono del cliente: ")
	fecha = input("Digite la nueva fecha: ")

	connection = pymysql.connect(
		host="localhost",
		user="root",
		password="",
		db="proyecto"
	)

	cursor = connection.cursor()
	
	sql = "UPDATE cliente SET nombre = %s, apellido = %s, direccion = %s, telefono = %s, fecha = %s  WHERE codigo = %s"
	cursor.execute(sql,(nombre, apellido, direccion, telefono, fecha, codigo))
	resultado = cursor.fetchone()
	connection.commit()
	'''cursor.close()
	conexion.close()'''

	print("")
	print("[m] Volver al menu.")
	print("[s] Salir.")
 
	opcion = input("Digite una opcion: ")

	if opcion == "m":
		menu()
	elif opcion == "s":
		sys.exit()

def modificar_encargado():
	os.system("cls")
	print("--modificar encargado--")
	print("")

	codigo = input("Digite el codigo del encargado: ")
	nombre = input("Digite el nuevo nombre del encargado: ")
	apellido = input("Digite el nuevo apellido : ")
	direccion = input("Digite la nueva direccion : ")
	telefono = input("Digite el nuevo telefono: ")
	correo = input("Digite el nuevo correo : ")

	connection = pymysql.connect(
		host="localhost",
		user="root",
		password="",
		db="proyecto"
	)

	cursor = connection.cursor()
	
	sql = "UPDATE encargado SET nombre = %s, apellido = %s, direccion = %s, telefono = %s, correo = %s  WHERE codigo = %s"
	cursor.execute(sql,(nombre, apellido, direccion, telefono, correo, codigo))
	resultado = cursor.fetchone()
	connection.commit()
	'''cursor.close()
	conexion.close()'''

	print("")
	print("[m] Volver al menu.")
	print("[s] Salir.")
 
	opcion = input("Digite una opcion: ")

	if opcion == "m":
		menu()
	elif opcion == "s":
		sys.exit()

def modificar_producto():
	os.system("cls")
	print("--modificar producto--")
	print("")

	codigo = input("Digite el codigo del cliente: ")
	descripcion = input("Digite la descripcion del producto: ")
	precio = input("Digite el nuevo precio: ")
	observacion = input("Digite alguna observacion:")

	connection = pymysql.connect(
		host="localhost",
		user="root",
		password="",
		db="proyecto"
	)

	cursor = connection.cursor()
	
	sql = "UPDATE producto SET descripcion = %s, precio = %s, observacion = %s WHERE codigo = %s"
	cursor.execute(sql,(descripcion,precio,observacion,codigo))
	resultado = cursor.fetchone()
	connection.commit()
	'''cursor.close()
	conexion.close()'''

	print("")
	print("[m] Volver al menu.")
	print("[s] Salir.")
 
	opcion = input("Digite una opcion: ")

	if opcion == "m":
		menu()
	elif opcion == "s":
		sys.exit()

def modificar_proveedor():
	os.system("cls")
	print("--modificar proveedor--")
	print("")

	codigo = input("Digite codigo del proveedor: ")
	nombre = input("Digite nuevo nombre: ")
	apellido = input("Digite nuevo apellido: ")
	direccion = input("Digite nueva direccion: ")
	Producto = input("Digite nuevo producto: ")
	telefono = input("Digite nuevo telefono: ")
	observacion = input("Digite nueva observacion: ")

	connection = pymysql.connect(
		host="localhost",
		user="root",
		password="",
		db="proyecto"
	)

	cursor = connection.cursor()
	
	sql = "UPDATE proveedor SET nombre = %s, apellido = %s, direccion = %s, producto = %s, telefono = %s, observacion = %s WHERE codigo = %s"
	cursor.execute(sql,(nombre, apellido,direccion, Producto, telefono, observacion, codigo))
	resultado = cursor.fetchone()
	connection.commit()
	'''cursor.close()
	conexion.close()'''

	print("")
	print("[m] Volver al menu.")
	print("[s] Salir.")
 
	opcion = input("Digite una opcion: ")

	if opcion == "m":
		menu()
	elif opcion == "s":
		sys.exit()

def eliminar_cliente():
	os.system("cls")
	print("--eliminar cliente--")
	print("")

	codigo = input("Digite el codigo del cliente: ")

	connection = pymysql.connect(
		host="localhost",
		user="root",
		password="",
		db="proyecto"
	)

	cursor = connection.cursor()
	
	sql = "DELETE FROM cliente WHERE  codigo = %s"
	cursor.execute(sql,(codigo))
	resultado = cursor.fetchone()
	connection.commit()
	'''cursor.close()
	conexion.close()'''

	print("")
	print("[m] Volver al menu.")
	print("[s] Salir.")
 
	opcion = input("Digite una opcion: ")

	if opcion == "m":
		menu()
	elif opcion == "s":
		sys.exit()

def eliminar_encargado():
	os.system("cls")
	print("--eliminar encargado--")
	print("")

	codigo = input("Digite el codigo del encargado: ")

	connection = pymysql.connect(
		host="localhost",
		user="root",
		password="",
		db="proyecto"
	)

	cursor = connection.cursor()
	
	sql = "DELETE FROM encargado WHERE  codigo = %s"
	cursor.execute(sql,(codigo))
	resultado = cursor.fetchone()
	connection.commit()
	'''cursor.close()
	conexion.close()'''

	print("")
	print("[m] Volver al menu.")
	print("[s] Salir.")
 
	opcion = input("Digite una opcion: ")

	if opcion == "m":
		menu()
	elif opcion == "s":
		sys.exit()

def eliminar_producto():
	os.system("cls")
	print("--eliminar producto--")
	print("")

	codigo = input("Digite el codigo del producto: ")

	connection = pymysql.connect(
		host="localhost",
		user="root",
		password="",
		db="proyecto"
	)

	cursor = connection.cursor()
	
	sql = "DELETE FROM producto WHERE  codigo = %s"
	cursor.execute(sql,(codigo))
	resultado = cursor.fetchone()
	connection.commit()
	'''cursor.close()
	conexion.close()'''

	print("")
	print("[m] Volver al menu.")
	print("[s] Salir.")
 
	opcion = input("Digite una opcion: ")

	if opcion == "m":
		menu()
	elif opcion == "s":
		sys.exit()

def eliminar_proveedor():
	os.system("cls")
	print("--eliminar proveedor--")
	print("")

	codigo = input("Digite el codigo del proveedor: ")

	connection = pymysql.connect(
		host="localhost",
		user="root",
		password="",
		db="proyecto"
	)

	cursor = connection.cursor()
	
	sql = "DELETE FROM proveedor WHERE  codigo = %s"
	cursor.execute(sql,(codigo))
	resultado = cursor.fetchone()
	connection.commit()
	'''cursor.close()
	conexion.close()'''

	print("")
	print("[m] Volver al menu.")
	print("[s] Salir.")
 
	opcion = input("Digite una opcion: ")

	if opcion == "m":
		menu()
	elif opcion == "s":
		sys.exit()

def factura(): #Creado por Diego Antonio Martinez Yucute
	os.system("cls")
	print("--Agregar datos de la factura--")
	print("")

	codigo = input("Digite el numero de factura: ")
	id_cliente = input("ingrese codigo del cliente: ")
	fecha = input("Digite la fecha: ")
	nit = input("Digite el nit: ")
	id_producto = input("Digite el codigo del producto: ")
	cantidad = input("Digite la cantidad: ")
	print("****")
	print("****")
	print("FACTURA GENERADO")


	connection = pymysql.connect(
		host="localhost",
		user="root",
		password="",
		db="proyecto"
	)

	cursor = connection.cursor()
	
	sql = "INSERT INTO factura (codigo, idcliente, fecha, nit, idproducto, cantidad) VALUES (%s, %s, %s, %s, %s, %s)"
	cursor.execute(sql,(codigo, id_cliente, fecha, nit, id_producto, cantidad))
	connection.commit()

	print("[m] Volver al menu.")
	print("[s] Salir.")

	opcion = input("Digite una opcion: ")

	if opcion == "m":
		menu()
	elif opcion == "s":
		sys.exit()

def mostrar_factura(): #Creado por Diego Antonio Martinez Yucute
	os.system("cls")
	print("--factura--")
	print("")

	connection = pymysql.connect(
		host="localhost",
		user="root",
		password="",
		db="proyecto"
	)

	cursor = connection.cursor()
	
	sql = "SELECT f.codigo, (SELECT CONCAT(c.nombre,' ', c.apellido) FROM  cliente c WHERE c.codigo = f.idcliente )cliente, f.fecha, f.nit, f.cantidad, (SELECT p.descripcion FROM producto p WHERE p.codigo = f.idproducto)producto, (SELECT p.precio FROM producto p WHERE p.codigo = f.idproducto)precio, FORMAT((f.cantidad*(SELECT p.precio FROM producto p WHERE p.codigo = f.idproducto)),2)total FROM factura f "
	cursor.execute(sql)
	#connection.commit()
	resultado = cursor.fetchall()

	for datos in resultado:
		print("|No.Fac| |Nombre Cliente| |Fecha|  |Nit|  |Detalles del producto|  |TOTAL A PAGAR|")
		print("__________________________________________________________________________________")
		print(datos)
	print("")
	print("[m] Volver al menu.")
	print("[s] Salir.")
 
	opcion = input("Digite una opcion: ")

	if opcion == "m":
		menu()
	elif opcion == "s":
		sys.exit()

def eliminar_factura():
	os.system("cls")
	print("--eliminar factura--")
	print("")

	codigo = input("Digite el codigo de la factura: ")

	connection = pymysql.connect(
		host="localhost",
		user="root",
		password="",
		db="proyecto"
	)

	cursor = connection.cursor()
	
	sql = "DELETE FROM factura WHERE  codigo = %s"
	cursor.execute(sql,(codigo))
	resultado = cursor.fetchone()
	connection.commit()
	'''cursor.close()
	conexion.close()'''

	print("")
	print("[m] Volver al menu.")
	print("[s] Salir.")
 
	opcion = input("Digite una opcion: ")

	if opcion == "m":
		menu()
	elif opcion == "s":
		sys.exit()

def menu():
	os.system("cls")
	print("*********BOUTIQUE FASHION PYTHON*********")
	print("")
	print("--CONTROL DE INVENTARIO,COMPRAS y VENTAS--")
	print("")
	print("-------------------------------")
	print("| ☞ 1)  Clientes.             |")
	print("| ☞ 2)  Encargado.            |")
	print("| ☞ 3)  Producto.             |")
	print("| ☞ 4)  Proveedor.            |")
	print("| ☞ 5)  Mostrar clientes.     |")
	print("| ☞ 6)  Mostrar encargados.   |")
	print("| ☞ 7)  Mostrar producto.     |")
	print("| ☞ 8)  Mostrar proveedor.    |")
	print("| ☞ 9)  Modificar cliente.    |")
	print("| ☞ 10) Modificar encargado.  |")
	print("| ☞ 11) Modificar producto.   |")
	print("| ☞ 12) Modificar proveedor.  |")
	print("| ☞ 13) Eliminar cliente.     |")
	print("| ☞ 14) Eliminar encargado.   |")
	print("| ☞ 15) Eliminar producto.    |")
	print("| ☞ 16) Eliminar proveedor.   |")
	print("| ☞ 17) Factura.              |")
	print("| ☞ 18) Mostrar factura.      |")
	print("| ☞ 19) Eliminar factura.     |")
	print("| ☞ 20) Salir.                |")
	print("-------------------------------")
	print("")

	opcion = input("Digite una opcion: ")

	if opcion == "1":
		Clientes()
	elif opcion == "2":
		Encargado()
	elif opcion == "3":
		Producto()
	elif opcion == "4":
		proveedor()
	elif opcion == "5":
		mostrar_clientes()
	elif opcion == "6":
		mostrar_encargado()
	elif opcion == "7":
		mostrar_producto()
	elif opcion == "8":
		mostrar_proveedor()
	elif opcion == "9":
		modificar_cliente()
	elif opcion == "10":
		modificar_encargado()
	elif opcion == "11":
		modificar_producto()
	elif opcion == "12":
		modificar_proveedor()
	elif opcion == "13":
		eliminar_cliente()
	elif opcion == "14":
		eliminar_encargado()
	elif opcion == "15":
		eliminar_producto()
	elif opcion == "16":
		eliminar_proveedor()
	elif opcion == "17":
		factura()
	elif opcion == "18":
		mostrar_factura()
	elif opcion == "19":
		eliminar_factura()
	elif opcion == "20":
		os.system("cls")
		print("*****************BOUTIQUE FASHION PYTHON*****************")
		print("👐 UN GUSTO SERVIRLE... ADIOS 👐")
		sys.exit()
	else:
		opcion = input("Digite una opcion valida: ")
		menu(opcion)
menu()