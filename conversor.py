layers = iface.mapCanvas().layers()

epsg = 'EPSG:31982'
crs = QgsCoordinateReferenceSystem(epsg)
fn = 'C:/Seu/Diretorio/'

for layer in layers:
    fn_atual = fn + str(layer.name())
    _writer = QgsVectorFileWriter.writeAsVectorFormat(layer, fn_atual, "utf-8", crs, driverName="ESRI Shapefile")
