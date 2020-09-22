# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 17:38:51 2017

@author: AlexanderYarwood
"""

#CKT_RESULT WINAPI CKT_RegisterSno(int sno, int ComPort)

import ctypes
from ctypes import POINTER

hllDll = ctypes.WinDLL ("C:\\Users\\Alexander Yarwood\\Documents\\TC400Dll\\2.1.10.9\\tc400.dll")


hllApiProto= ctypes.WINFUNCTYPE (
    ctypes.c_int,      # Return type.
    POINTER(ctypes.c_void_p),   # Parameters 1 ...
    POINTER(ctypes.c_void_p))   # ... thru 4.
hllApiParams = (1, "p1", 0), (1, "p2", 0),

hllApi = hllApiProto (("CKT_RegisterUSB", hllDll), hllApiParams)

gSno = 1
index = 0

p1 = ctypes.c_int (gSno)
p2 = ctypes.c_int (index)
hllApi (ctypes.byref (p1), ctypes.byref (p2))





hllApiProto2= ctypes.WINFUNCTYPE (
    ctypes.c_int,      # Return type.
    POINTER(ctypes.c_void_p),   # Parameters 1 ...
    POINTER(ctypes.c_void_p))   # ... thru 4.
hllApiParams2 = (1, "p3", 0), (1, "p4", 0),

hllApi2 = hllApiProto2 (("CKT_GetDeviceClock", hllDll), hllApiParams2)

IDNumber = 0
devclock = 0

p3 = ctypes.c_int (IDNumber)
p4 = ctypes.c_int (devclock)
hllApi2 (ctypes.byref (p3), ctypes.byref (p4))






hllApiProto3= ctypes.WINFUNCTYPE (
        ctypes.c_int
    )


hllApi3 = hllApiProto3 (("CKT_Disconnect", hllDll))


hllApi3 ()

pint3 = p3.value
pint4 = p4.value

pin3 = str(pint3)
pin4 = str(pint4)

with open('Failed.txt', 'w') as file:
    file.write(pin3)
    file.write(pin4)
    
