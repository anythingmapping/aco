# Import necessary QGIS modules
from qgis.core import QgsVectorLayer, QgsMessageLog
from qgis.core import QgsProject, QgsPalLayerSettings, QgsTextFormat, QgsRuleBasedLabeling
from PyQt5.QtGui import QColor
from qgis.core import QgsPalLayerSettings, QgsTextFormat, QgsVectorLayerSimpleLabeling


# Import the previously defined classes for ACO
from ant_colony_optimization import Ant, AntColony  # Assuming you've saved the classes in 'ant_colony_optimization.py'

NETWORK_NAME = "world_hex"
LABEL_FIELD_NAME = 'country'


class Build_vector_network:
    """ 
    Builds the vector network and return the extent of the network
    At the moment the network extent is the most important thing 
    """
    def __init__(self, iface):
        self.iface = iface
        # Connect to the necessary QGIS signals and set up the user interface

    def load_data(self):
        """Load data from the QGIS layers and return their combined extent."""
        
        # These will become QGIS plugin inputs
        # Load the Transport for London Road Network layer
        # filepath1 = "/Users/mosl/Documents/CODE/ACO_QGIS/data/road_network.gpkg"
        # network_layer = QgsVectorLayer(filepath1, "Transport for London Road Network", "ogr")
        
        filepath2 = "/Users/mosl/Documents/CODE/ACO_QGIS/data/world_hex.shp"
        network_layer = QgsVectorLayer(filepath2, NETWORK_NAME, "ogr")

        # Check if the layers were successfully loaded
        # if not network_layer.isValid() or not node_layer.isValid():
        #     print("Error loading one or both layers!")
        #     return None

        # Add the layers to the QGIS project (optional)
        QgsProject.instance().addMapLayer(network_layer)
        # QgsProject.instance().addMapLayer(node_layer)

        # Calculate the combined extent of both layers
        # extent = network_layer.extent().combineExtentWith(node_layer.extent())
        extent = network_layer.extent()
        return extent
    

    def iterate_features_to_list(self):
        """
        Iterate over every feature in the 'world_3857' dataset and add to a list.
        
        Returns:
            list: List containing all features from the 'world_3857' dataset.
        """
        # Retrieve the layer by its name
        layer = QgsProject.instance().mapLayersByName('world_hex')[0]
        # Initialize an empty list to store features
        feature_list = []

        # Iterate over each feature in the layer and append to the list
        for feature in layer.getFeatures():
            feature_list.append(feature)

        return feature_list
    


    def label_features(self):
        """
        Label individual features in the 'world_3857' dataset.
        """
        # Retrieve the layer by its name
        layer = QgsProject.instance().mapLayersByName(NETWORK_NAME)[0]
        # Enable labeling for the layer
        layer.setLabelsEnabled(True)
        
        label = QgsPalLayerSettings()
        label.readFromLayer(layer)
        label.enabled = True
        label.fieldName = "country"
        label.placement= QgsPalLayerSettings.AroundPoint
        label.setDataDefinedProperty(QgsPalLayerSettings.Size,True,True,"30")
        label.writeToLayer(layer)









        text_format = QgsTextFormat()
        text_format.setSize(12)

        layer_settings.setFormat(text_format)
        layer_settings.enabled = True
        layer_settings = QgsVectorLayerSimpleLabeling(layer_settings)

        layer.setLabelsEnabled(True)
        layer.setLabeling(layer_settings)
        layer.triggerRepaint()   


    def run_aco(self):
        """Run the ACO algorithm."""
        graph = self.load_data()
        num_ants = 10  # Example value
        evaporation_rate = 0.5  # Example value
        initial_pheromone = 1.0  # Example value

        colony = AntColony(graph, num_ants, evaporation_rate, initial_pheromone)
        num_iterations = 100  # Example value
        colony.simulate(num_iterations)
        
        # Further processing or visualization can be added here



network =  Build_vector_network(iface)
combined_extent = network.load_data()
QgsMessageLog.logMessage(f"Combined Extent: {combined_extent.toString()}")

features = network.iterate_features_to_list()
QgsMessageLog.logMessage(f"Feature List: {features}")

# Call the function to label features
network.label_features()

# Example usage:

print(f"Total features in the list: {len(features)}")