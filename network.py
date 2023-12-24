# Import necessary QGIS modules
from qgis.core import QgsVectorLayer, QgsMessageLog

# Import the previously defined classes for ACO
from ant_colony_optimization import Ant, AntColony  # Assuming you've saved the classes in 'ant_colony_optimization.py'
from qgis.core import QgsProject


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
        filepath1 = "/Users/mosl/Documents/CODE/ACO_QGIS/data/road_network.gpkg"
        network_layer = QgsVectorLayer(filepath1, "Transport for London Road Network", "ogr")
        
        # # Load the Bus Stops layer
        # filepath2 = "/Users/mosl/Documents/CODE/ACO_QGIS/data/Bus_Stops/Bus_Stops.shp"
        # node_layer = QgsVectorLayer(filepath2, "Bus Stops", "ogr")

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




        # Convert layer features to a graph representation
        # For simplicity, let's assume you have a method to convert layer features to a graph

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



instance =  Build_vector_network(iface)
combined_extent = instance.load_data()
QgsMessageLog.logMessage(f"Combined Extent: {combined_extent.toString()}")