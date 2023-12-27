import os
import yaml
from keras.models import Sequential
from keras.layers import LSTM, Dense


def time_stamp_fnamer(tstamp):
    """
    A function to generate filenames from timestamps
    """
    cdate, ctime = str(tstamp).split(" ")
    current_date = "_".join(cdate.split("-"))
    chour, cmin, csec = ctime.split(":")
    csec, cmilli = csec.split(".")
    current_time = "_".join([chour, cmin, csec, cmilli])
    current_date_time_name = "_".join([current_date, current_time])
    return current_date_time_name


def load_config(config_name):
    """
    A function to load and return config file in YAML format
    """
    CONFIG_PATH = "/home/pi/raingauge/rainfall_monitor/config/"
    with open(os.path.join(CONFIG_PATH, config_name)) as file:
        config = yaml.safe_load(file)

    return config


def create_folder(directory):
    """Function to create a folder in a location if it does not exist"""
    if not os.path.exists(directory):
        os.makedirs(directory)


def create_log_file(log_folder, log_file):
    with open(os.path.join(log_folder, log_file), "a") as f:
        f.write("")


def create_lstm_model():
    model = Sequential()
    model.add(LSTM(50))
    model.add(Dense(30))
    model.add(Dense(10))
    model.add(Dense(1))
    return model


def load_estimate_model(model_path):
    model = create_lstm_model()
    config = load_config("config.yaml")
    model.build(input_shape=config["stft_shape"])
    model.load_weights(model_path)
    return model
