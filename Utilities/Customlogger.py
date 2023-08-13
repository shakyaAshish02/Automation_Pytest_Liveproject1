import logging
#import inspect

class logclass:
    @staticmethod
    def getthelogs():

        logger = logging.getLogger()
        filehandler = logging.FileHandler(filename="C:\\Users\\ashis\PycharmProjects\\IIMjobs\\Logs\\automation1.log",mode='w')
        formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(module)s: %(funcName)s: %(message)s', datefmt='%d/%m/%Y %I:%M:%S %p')
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)
        logger.setLevel(logging.INFO)
        return logger
