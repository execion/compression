import logging

class Logger:
    def __init__(self, path_file):
        self.logger = logging.getLogger()
        logging.basicConfig(filename=path_file, level=logging.INFO, format='%(asctime)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    def info(self, msg):
        self.logger.info(msg)