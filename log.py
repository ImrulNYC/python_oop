import logging 
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s- %(name)s- %(levelname)s- %(message)s',
                     datefmt='%m/%d/%Y %H:%M:%S')


import log2



logging.debug("debug")
logging.info("info")

logging.warning("warning")
logging.error("error")
logging.critical("Critical")



