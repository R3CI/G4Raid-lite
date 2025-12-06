from src import *
from src.utils.logging import logger

def errorhandler(exc_type, exc_value, exc_traceback):
    tracebk = ''.join(traceback.format_exception(exc_type, exc_value, exc_traceback))
    
    logger.error(f'Error » {tracebk}')
    logger.error('If this keeps happening join the discord and report the error')
    input('')
    sys.exit()