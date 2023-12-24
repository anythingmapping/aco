#create ant agents
from qgis.utils import iface
from qgis.core import QgsProject, QgsMessageLog, QgsVectorLayer, QgsRasterLayer, QgsPoint, QgsFeature, QgsGeometry
from PyQt5.QtGui import QColor

import random

mem_layer = QgsVectorLayer(
            "point?crs=epsg:4326&field=id:integer"
            "&field=road_name:string&index=yes",
            "Roads",
            "memory"
        )


class Agent_ACO:
    def __init__(self, x, y):
        """ setup a default agent template """
        self.x = x
        self.y = y


    def random_start_position(self):
        """ dev function to overwrite the start location """
        self.x = random.randrange(145, 155)
        #self.x = random.randrange(55, 65)
        self.y = random.randrange(55, 65)


    def create_agent(self):
        """" Agent creation """
        mem_layer.startEditing()
        QgsProject.instance().addMapLayer(mem_layer)       
        self.feature = QgsFeature()
        self.feature.setGeometry(QgsPoint(self.x, self.y))
        self.feature.setAttributes([1, 'QGIS Lane'])
        self.feature
        mem_layer.addFeature(self.feature)
        mem_layer.commitChanges()


    def change_color(self):
        active_layer = iface.activeLayer()
        renderer = active_layer.renderer()
        symbol = renderer.symbol()
        symbol.setSize(30)
        color = QColor(255, 0, 0)  # RGB values for red
        symbol.setColor(color)
        active_layer.triggerRepaint()
        iface.layerTreeView().refreshLayerSymbology(active_layer.id())


class Build_ACO():
    def __init__(self, noa):
        self.number_of_agents = noa


agent = Agent_ACO(-150, 62)

for i in range(10):
    print("number is: {0}".format(i))
    agent.random_start_position()
    agent.create_agent()
    agent.change_color()
    



