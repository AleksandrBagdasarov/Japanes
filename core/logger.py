import logging


# logging.basicConfig(level=logging.ERROR, filename='my.log', filemode='a', format='%(levelname)s: %(asctime)s - %(message)s')

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
fh = logging.StreamHandler()
fh.setLevel(logging.DEBUG)

sh = logging.StreamHandler()
sh.setLevel(logging.ERROR)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(levelname)s: %(message)s')

# add formatter to ch
fh.setFormatter(formatter)
sh.setFormatter(formatter)

# add ch to logger
logger.addHandler(fh)
logger.addHandler(sh)
