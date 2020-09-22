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
    ctypes.c_void_p,   # Parameters 1 ...
    ctypes.c_void_p)   # ... thru 4.
hllApiParams = (1, "p1", 0), (1, "p2", 0),

hllApi = hllApiProto (("CKT_RegisterUSB", hllDll), hllApiParams)

gSno = 1
index = 0

p1 = ctypes.c_int (gSno)
p2 = ctypes.c_int (index)
hllApi (ctypes.byref (p1), ctypes.byref (p2))





hllApiProto2= ctypes.WINFUNCTYPE (
    ctypes.c_int,      # Return type.
    ctypes.c_void_p,   # Parameters 1 ...
    ctypes.c_void_p,
    ctypes.c_void_p,
    ctypes.c_void_p)   # ... thru 4.
hllApiParams2 = (1, "p3", 0), (1, "p4", 0), (1, "p5", 0), (1, "p6", 0)

hllApi2 = hllApiProto2 (("CKT_SetDeviceDate", hllDll), hllApiParams2)

sno = 0
year = 0
month = 0
day = 0

p3 = ctypes.c_int (sno)
p4 = ctypes.c_int (year)
p5 = ctypes.c_int (month)
p6 = ctypes.c_int (day)
hllApi2 (ctypes.byref (p3), ctypes.byref (p4), ctypes.byref (p5), ctypes.byref (p6))






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
    
