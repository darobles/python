class Comuna:

	def __init__(self,idcomuna,idregion,nombre,url_logo=None,latitud=None,longitud=None,
	email=None,telefono=None,moviles=None,ind_mon=None,zoom=5,aut_ouct=None):
		self.idcomuna = idcomuna
		self.idregion = idregion
		self.nombre   = nombre
		self.url_logo = url_logo
		self.latitud  = latitud
		self.longitud = longitud
		self.email    = email
		self.telefono = telefono
		self.moviles  = moviles
		self.ind_mon  = ind_mon
		self.zoom	  = zoom
		self.aut_ouct = aut_ouct

	def __str__(self):
		return 'Comuna: idcomuna: {}, idregion: {}, nombre: {}, url_logo: {}, latitud: {}, longitud: {}, email: {}, telefono: {}, moviles: {}, ind_mon: {}, zoom: {}, aut_ouct: {}'.format(self.idcomuna,self.idregion,self.nombre,self.url_logo,
			self.latitud, self.longitud,self.email,self.telefono,self.moviles,self.ind_mon,self.zoom,self.aut_ouct)