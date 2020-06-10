import pytest
import logging
from Utils import Utility as util


@pytest.mark.usefixtures("test_setup")
class BaseClass:

    def getLogger(self):
        loggerName = util.func_name()
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.DEBUG)
        return logger
