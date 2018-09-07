'''
This file is intended as a starting point
for the TF interface

HOW TO: 
1. Lage klassen som skal være NN modellen
2: Lage en klasse som parser data riktig (onehotencoder og setter opp training/test etc) 

'''
import nn_model

number_of_layers = 0
input_layer_size = 0
hidden_layer_size = 0
output_layer_size = 0
hidden_layer_activation_function = None
output_layer_activation_function = None
cost_function = None
learning_rate = 0.0
initial_weight_range = (0,0)
optimizer = None
data_source = None


def main_event():
    a = 2
    #create a model 
    nn = nn_model()
    #train it
    #test it

if __name__ == "__main__":
    main_event()


