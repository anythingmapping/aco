# from pyQt5.QtGui import QColor
# from pyQt5.QtCore import Qt

"""
hxdrCatalogLoader
"""
from qgis.utils import iface
from qgis.core import QgsProject, QgsMessageLog, QgsVectorLayer, QgsRasterLayer, QgsPoint, QgsFeature, QgsGeometry

class BuildMap:

    def __init__(self, iface):
        self.iface = iface


    def load_raster(self):
        natural_earth = QgsRasterLayer('/Users/mosl/Documents/PROJECTS_2023/20231001_python_plugin/pyqgis3_files/data/natural_earth/natural_earth.tif', 'NaturalEarth')
        natural_earth.isValid()
        QgsProject.instance().addMapLayer(natural_earth)
        QgsMessageLog.logMessage("This is a warning")


    def load_vector(self):
        world_borders = QgsVectorLayer('/Users/mosl/Documents/PROJECTS_2023/20231001_python_plugin/pyqgis3_files/data/world_borders.shp', 'world_borders', 'ogr')
        world_borders.isValid()
        QgsProject.instance().addMapLayer(world_borders)
        QgsMessageLog.logMessage("This is a warning")


    # def load_gpkg(self):
    #     path = '/Users/mosl/Documents/PROJECTS_2023/20231001_python_plugin/pyqgis3_files/data/GEOM_container_4326.gpkg'
    #     gp = gdal.OpenEx(path)
    #     for i in range(gp.GetLayerCount()):
    #         lyr = gp.GetLayer(i)
    #         gpkg_lyr = QgsVectorLayer("{}|layername={}".format(path, lyr.GetName()), lyr.GetName(), 'ogr')


        # gpkg = QgsVectorLayer('/Users/mosl/Documents/PROJECTS_2023/20231001_python_plugin/pyqgis3_files/data/GEOM_container_4326.gpkg|layername=geom_container_4326', 'geom_container_4326', 'ogr')
        # QgsProject.instance().addMapLayer(gpkg)



    def mem_layer(self):

        mem_layer = QgsVectorLayer(
            "LineString?crs=epsg:4326&field=id:integer"
            "&field=road_name:string&index=yes",
            "Roads",
            "memory"
        )

        QgsProject.instance().addMapLayer(mem_layer)

        mem_layer.startEditing()
        points = [QgsPoint(-150, 61), QgsPoint(-150, 62)]
        feature = QgsFeature()
        feature.setGeometry(QgsGeometry.fromPolyline(points))
        feature.setAttributes([1, 'QGIS Lane'])
        mem_layer.addFeature(feature)
        mem_layer.commitChanges()


    def change_color(self):
        active_layer = self.iface.activeLayer()
        renderer = active_layer.renderer()
        symbol = renderer.symbol()
        symbol.setColor(QColor('#74c475'))
        active_layer.triggerRepaint()
        self.iface.layerTreeView().refreshLayerSymbology(active_layer.id())


    def open_attribute_table(self):
        self.iface.showAttributeTable(iface.activeLayer())

def run_script(iface):
    map = BuildMap(iface)
    map.load_vector()
    map.change_color()
    # map.open_attribute_table()

def QGIS_stats():
    print(QgsApplication.pluginPath())
    print(QgsApplication.prefixPath())
    print(QgsApplication.qgisSettingsDirPath())
    print(QgsApplication.showSettings())

class GFG:
	
	# methods
	def add(self, a, b):
		return a + b
	def sub(self, a, b):
		return a - b

# explicit function	
def method():
	print("GFG")



