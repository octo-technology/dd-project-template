import logging
from logging.config import fileConfig

def getProjectLogger(conf_file='conf/{{ cookiecutter.project_slug }}.cfg'):
    '''
    Returns the current project logger configured with the current configuration file
    
    :param conf_file: configuration file name 
    :return: a logger
    '''
    fileConfig(conf_file)
    return logging.getLogger()

