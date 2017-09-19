import ctypes
from encapsulate_callback import encapsulate_callback

lib_motors = ctypes.cdll.LoadLibrary(LIBNAME)

lib_motors.setPosition.restype = None
lib_motors.moveTo.restype = None
lib_motors.moveTo.restype = None


def check_number(x):
    assert(isinstance(x, int) or isinstance(x, float))

def setPosition(x, y):

    check_number(x)
    check_number(y)
    lib_motors.setPosition(ctypes.c_int(x), ctypes.c_int(y))


def moveTo(x, y, goalAngle, callback = lambda: None):

    check_number(x)
    check_number(y)
    check_number(goalAngle)

    lib_motors.moveTo(ctypes.c_int(x), ctypes.c_int(y), ctypes.c_int(goalAngle),
                      encapsulate_callback(callback))



def addPointInPath(x, y, goalAngle, callback = lambda: None):

    check_number(x)
    check_number(y)
    check_number(goalAngle)

    lib_motors.addPointInPath(ctypes.c_int(x), ctypes.c_int(y),
                              ctypes.c_int(goalAngle),
                              encapsulate_callback(callback))

    
