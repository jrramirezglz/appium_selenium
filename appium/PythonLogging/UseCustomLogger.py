import logging
from appium.PythonLogging import PythonLogging as cl


class CustomLoggerDemo():
    log =cl.customLogger()

    def methodOne(self):
        logging.critical("Este es un Error critico")
        logging.error("Este es un Error")
        logging.warning("Este es un Warning")
        logging.info("Este es un Info")
        logging.debug("Este es un debug")

    def methodTwo(self):
        m2 = cl.customLogger()
        m2.critical("Critical msg")
        m2.error("error msg")
        m2.warning("warning msg")
        m2.info("info msg")
        m2.debug("debug msg")

cld = CustomLoggerDemo()
cld.methodOne()
cld.methodTwo()