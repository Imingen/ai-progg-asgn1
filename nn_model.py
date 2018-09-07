import tensorflow as tf
import numpy as np




class NeuralNetModel():
    '''
    This class represent a general neural net model
    '''
    def __init__(self, num_nodes, activation_function, 
                learning_rate, optimizer, mini_batch_size):
        self.nodes = num_nodes
        #self.weights = None
        self.num_layers = len(num_nodes)
        self.activation_function = activation_function
        #self.output_activation_function = None
        self.learning_rate = learning_rate
        self.optimizer = optimizer
        self.mini_batch_size = mini_batch_size
        self.create_model()


    def create_model():
        input_nodes = self.nodes[1]
        output_nodes = self.nodes[-1]
        hidden_nodes = self.nodes[1:-1]

        for layer in range(self.num_layers):
            continue


    def train_model(data):
        x = 1337





