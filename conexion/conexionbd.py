import cx_Oracle

def conexion():
	connection = cx_Oracle.connect("user","pass","server_oracle") #Haciendo referencia al nombre de tnsnames.ora
	return connection