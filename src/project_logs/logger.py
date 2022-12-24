from datetime import date
import logging

logger_file = "./project_logs/project_log.log"
today = date.today()

logging.basicConfig(format='%(asctime)s [%(levelname)s] %(message)s', 
                    datefmt='%Y-%m-%dT%H:%M:%S%z', 
                    filename=logger_file, 
                    level=logging.DEBUG, 
                    encoding='utf-8',
                    filemode="a+")
