import pytest
import logging
from Utils import Utility as util
from datetime import datetime
import os


@pytest.mark.usefixtures("test_setup")
class BaseClass:

    def getLogger(self, func_name):
        # loggerName = util.func_name()
        logger = logging.getLogger(func_name)
        fileHandler = logging.FileHandler(filename='C:/KBData/PyCharmProjects/PythonSeleniumFrame/Reports/LogFiles/'+func_name+'_logfile_{:%d-%m-%Y_%H-%M-%S}.log'.format(datetime.now()))
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.DEBUG)
        return logger
