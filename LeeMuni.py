from conexion.conexionbd import *
from patron.comuna import Comuna

def consultaParSis():
	listaComunas = []
	conn = conexion();
	c = conn.cursor()
	c.execute(u'select PAR_COD,PAR_VAL from TBL_PAR_SIS')
	for row in c:
	    print (row[0], "-", row[1])
	conn.close()
	return listaComunas

consultaParSis()