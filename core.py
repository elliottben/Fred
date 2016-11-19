#lstm keras seq seq implementation
import numpy
#import matplotlib.pyplot as plt
import pandas
import math
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
#rec.
from keras.utils.visualize_util import plot
#import pydot

class init_fred:
    def __init__(self, depth, max_sentence_length):
        model = Sequential()
        model.add(LSTM(4, input_dim=1))
        model.add(Dense(1)) #max_sentence_length here
        model.compile(loss="mean_squared_error", optimizer="adam")
        plot(model, to_file="model.png")

if __name__ == "__main__":
    #init_model
    init_fred(16, 1)
    #display model--testing
    #input_data
    #train_model
    #testing heuristics
