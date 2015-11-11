#include <SCI/Mat4.h>
import numpy as np
from _pyio import __metaclass__
from abc import ABCMeta, abstractmethod

class CameraControls():
    __metaclass__ = ABCMeta
    @abstractmethod
    def GetView(self):
    
