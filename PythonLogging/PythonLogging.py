"""
 se refiere a trackerar eventos y pasos durante la ejecucion del software
Log events
Critical
Error
Warnbing
Info
Debug

"""

import logging

# logging.basicConfig(filename= "Test.log", level=logging.DEBUG) # log basico
"""
logs con formato  para fecha file mode = W reemplaza los valores , si no se agrega solo se agregan los nuevos datos al final 
"""
logging.basicConfig(format='%(asctime)s: %(levelname)s',datefmt='%d/%m/%y %I:%M:%S %p %A', filename= "Test.log", level=logging.DEBUG, filemode='w')


logging.critical("Este es un Error critico")
logging.error("Este es un Error")
logging.warning("Este es un Warning")
logging.info("Este es un Info")
logging.debug("Este es un debug")
