import logging
# Logs (Code on next slide)
class logclass:
    def getthelogs(self):
        logger = logging.getLogger()
        filehandler = logging.FileHandler("mylogfile.log")
        formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(module)s: %(funcName)s: %(message)s',datefmt='%d/%m/%Y %I:%M:%S %p')
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)
        logger.setLevel(logging.DEBUG)
        logger.debug("Debug message")
        return logger

