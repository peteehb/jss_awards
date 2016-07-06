import os
import time
import ConfigParser


def current_path(filename):
    return os.getcwd() + '/' + filename


def load_cfg(config_file):
    config = ConfigParser.ConfigParser()
    config.readfp(open(current_path(config_file)))
    return config


def timestamp():
    return str(int(time.time() * 1000))


def create_folder(folder):
    output_folder = folder + '_' + str(int(time.time()))
    os.makedirs(output_folder)
    return os.path.abspath(output_folder)


def zip_output():
    """
    Zip the pdfs into one file
    :return:
    """
    return


def clean_up():
    return
