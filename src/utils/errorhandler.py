from src import *

def errorhandler(exc_type, exc_value, exc_traceback):
    tracebk = ''.join(traceback.format_exception(exc_type, exc_value, exc_traceback))
    print(tracebk)
    input('')
    sys.exit()