import logging
import sys


formatter = logging.Formatter('%(asctime)s - %(levelname)s: %(pathname)s %(funcName)s -> %(message)s' , datefmt=('%Y-%m-%d %H:%M'))
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

console = logging.StreamHandler()
console.setFormatter(formatter)
logger.addHandler(console)

file_handler = logging.FileHandler('my.log')
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.WARNING)
logger.addHandler(file_handler)