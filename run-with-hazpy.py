import json
from subprocess import call

try:
    virtual_env = 'hazus_env'
    call('CALL conda.bat activate '+virtual_env +
         ' && python xml-grid-to-shapefile.py', shell=True)
except:
    import ctypes
    import sys
    messageBox = ctypes.windll.user32.MessageBoxW
    error = sys.exc_info()[0]
    messageBox(0, u"Unexpected error: {er} | If this problem persists, and you're sure it's not user error, ask your developers to write better code.".format(
        er=error), u"HazPy", 0x1000)
