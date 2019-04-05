#!/usr/bin/python3
# -*- utf-8 -*-

##@package websocket.py
#
# Control Class for the openMHA TCP/IP Interface
#
# @author Tobias Bruns
# @version 0.1
# @date 03.04.2019

# 2014 Fraunhofer IDMT, Oldenburg
# This software and/or program is protected by copyright law and international
# treaties. Any reproduction or distribution of this software and/or program,
# or any portion of it, may result in severe civil and criminal penalties, and
# will be prosecuted to the maximum extent possible under law.


import socket, time




class OpenMhaCalibration(object):
    '''
    classdocs
    '''
    _openMhaAddr = "127.0.0.1"; #standard address
    _openMhaPort = 33337; #standard port
    _openMhaGainPresets = {};
    _normalUCL = 85; # normal value for loud voice
    _normalMCL = 65; # normal vlaue for loud voice
    _debug = True;
    
    def __init__(self):
        # starting socket connection
        self._conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try: 
            self._conn.connect((self._openMhaAddr,self._openMhaPort))
            print('New connection to openMHA established')
        except Exception: 
            print('error: Cannot establish connection to open MHA')

        
    def close(self):
        self.setLog = False
    
        
    def ShowCalibrationLevels(self,dur_sec=30):
        msg = 'mha.transducers.calib_in.rmslevel?\n'
        time_intervall = 4 # Hz
        
        for idx in range(int(dur_sec*time_intervall)):
            self._conn.send(msg.encode('utf-8'))
            print(self._conn.recv(1024).decode('utf-8'))
            time.sleep(1/time_intervall)
        
            
    
if __name__ == "__main__":

    openMHACalibration = OpenMhaCalibration();
    openMHACalibration.ShowCalibrationLevels(60);
