# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 17:38:51 2017

@author: AlexanderYarwood
"""

#from ctypes import c_int, WINFUNCTYPE, windll
#from ctypes.wintypes import HWND, LPCSTR, UINT
#prototype = WINFUNCTYPE(c_int, HWND, LPCSTR, LPCSTR, UINT)
#paramflags = (1, "hwnd", 0), (1, "text", "Hi"), (1, "caption", None), (1, "flags", 0),
#MessageBox = prototype(("MessageBoxA", windll.user32), paramflags)

#MessageBox()
#MessageBox(text="Spam, spam, spam")
#MessageBox(flags=2, text="foo bar")
#CKT_RESULT WINAPI CKT_RegisterSno(int sno, int ComPort)


import ctypes

tc400Dll = ctypes.WinDLL ("C:\\Users\\Alexander Yarwood\\Documents\\TC400Dll\\2.1.10.9\\tc400.dll")


registerUSBProto= ctypes.WINFUNCTYPE (
    ctypes.c_int,      # Return type.
    ctypes.c_void_p,   # Parameters 1 ...
    ctypes.c_void_p)   # ... thru 2.
registerUSBParams = (1, "snoParam", 0), (1, "comPortParam", 0),

registerUSBApi = registerUSBProto (("CKT_RegisterUSB", tc400Dll), registerUSBParams)

gSno = 1
comPort = 0

snoParam = ctypes.c_int (gSno)
comPortParam = ctypes.c_int (comPort)

registerUSBApi (ctypes.byref (snoParam), ctypes.byref (comPortParam))



getDeviceClockProto= ctypes.WINFUNCTYPE (
    ctypes.c_int,      # Return type.
    ctypes.c_void_p,   # Parameters 1 ...
    ctypes.c_void_p)   # ... thru 2.
getDeviceClockParams = (1, "idNumber", 0), (2, "devClock",0),

getDeviceClockApi = getDeviceClockProto (("CKT_GetDeviceClock", tc400Dll), getDeviceClockParams)

IDNumber = 0
devclock = 0

idNumber = ctypes.c_int (IDNumber)
devClock = ctypes.c_int (devclock)
getDeviceClockApi (ctypes.byref (idNumber), ctypes.byref (devClock))




noArgumentsProto= ctypes.WINFUNCTYPE (
        ctypes.c_int
    )


disconnectApi = noArgumentsProto (("CKT_Disconnect", tc400Dll))


disconnectApi ()

pint3 = idNumber.value
pint4 = devClock.value

pin3 = str(pint3)
pin4 = str(pint4)

with open('Failed.txt', 'w') as file:
    file.write(pin3)
    file.write(pin4)
    
