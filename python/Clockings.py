# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 11:11:37 2017

@author: AlexanderYarwood
"""
"""import "tc_b.h"  """
#def main():
    #if you use the RS232 communication method,
    #please register the comm. port number
    #which is occupied by the machine.
    
    #CKT_ResgisterSno(12345678, 1)
    #CKT_ResgisterSno(87654321, 2)
    
    #if you use the TCP\IP communication method,
    #please register each machines IP adress.
    
    #CKT_RegisterNet(12345678, "192.168.0.1")
    #CKT_RegisterNet(87654321, "192.168.0.2")
    
    #enable real-time data transmission
    #if you use the RS232 communication method,
    #please run the daemon threads to recieve
    #the real-time data
    
    #CKT_ComDaemon()
    
    #if you use the TCP\IP communication method,
    #please run the daemon threads to recieve
    #the real-time data
    
    #CKT_NetDaemon()
    
    #Disconnect the COM and TCP\IP connection
    
    #CKT_Disconnect()


"""
Created on Thu Jul 27 11:11:37 2017

@author: https://stackoverflow.com/questions/252417/how-can-i-use-a-dll-file-from-python
"""
    
import ctypes

# Load DLL into memory.

#hllDll = ctypes.WinDLL ("c:\\PComm\\ehlapi32.dll")
hllDll = ctypes.WinDLL ("C:\\Users\\Alexander Yarwood\\Documents\\TC400Dll\\2.1.10.9\\tc400.dll")
#hllDll = ctypes.WinDLL ()
# Set up prototype and parameters for the desired function call.
# HLLAPI

#hllApiProto = ctypes.WINFUNCTYPE (
#    ctypes.c_int,      # Return type.
#    ctypes.c_void_p,   # Parameters 1 ...
#    ctypes.c_void_p,
#    ctypes.c_void_p,
#    ctypes.c_void_p)   # ... thru 4.
#hllApiParams = (1, "p1", 0), (1, "p2", 0), (1, "p3",0), (1, "p4",0),
    
#CKT_GetDeviceClock(IDNumber, devclock)
hllApiProto2= ctypes.WINFUNCTYPE (
    ctypes.c_int,      # Return type.
    ctypes.c_void_p,   # Parameters 1 ...
    ctypes.c_void_p)   # ... thru 4.
hllApiParams2 = (1, "p1", 0), (1, "p2", 0),
# Actually map the call ("HLLAPI(...)") to a Python name.

#hllApi = hllApiProto (("HLLAPI", hllDll), hllApiParams)
hllApi2 = hllApiProto2 (("CKT_GetClockingRecordEx", hllDll), hllApiParams2)

# This is how you can actually call the DLL function.
# Set up the variables and call the Python name with them.
IDNumber = 0
devclock = 0

p1 = ctypes.c_int (IDNumber)
p2 = ctypes.c_int (devclock)
hllApi2 (ctypes.byref (p1), ctypes.byref (p2))


