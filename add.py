import logging

logging.basicConfig(filename='output.log', level=logging.DEBUG)

def add(a, b):
    return a + b

logging.info(add(4,2))