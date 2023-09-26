import logging


class LoGen:

    @staticmethod
    def logen():
        logging.basicConfig(filename= ".\\Logs\\automation.log",
                            format='%(asctime)s: %(levelname)s: %(message)s', datefmt="%d/%m/%Y %I:%M:%S %p")
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger

    @staticmethod
    def logenError():
        logging.basicConfig(filename=".\\Logs\\automation.log",
                            format='%(asctime)s: %(levelname)s: %(message)s', datefmt="%d/%m/%Y %I:%M:%S %p")
        logger = logging.getLogger()
        logger.setLevel(logging.ERROR)
        return logger
