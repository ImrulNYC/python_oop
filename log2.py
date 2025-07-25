import logging
import time
''''
logger=logging.getLogger(__name__)
logger.propagate
logger.info('Hello from log2')
'''
logger=logging.getLogger(__name__)
stream_h=logging.StreamHandler()
file_h=logging.FileHandler('file.log')

stream_h.setLevel(logging.WARNING)
file_h.setLevel(logging.ERROR)

formatter=logging.Formatter('%(name)s-%(levelname)s -%(message)s ')
stream_h.setFormatter(formatter)
file_h.setFormatter(formatter)

logger.addHandler(stream_h)
logger.addHandler(file_h)

logger.warning("this is warning")
logger.error(f"this is an error, {time.time()}")

