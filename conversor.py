layers = iface.mapCanvas().layers()
#print(layers)

diretorio = 'C:/Users/lpzam/Desktop/Conversor_CRS/Convertidos'
crs = QgsCoordinateReferenceSystem("EPSG:31985")

contador = 1

for layer in layers:
	#print(layer.name())
	diretorio_final = diretorio + '/' + layer.name() + '_' + str(contador)
	convertidos = QgsVectorFileWriter.writeAsVectorFormat(layer, diretorio_final, 'utf-8', crs, driverName="ESRI Shapefile")
	contador += 1