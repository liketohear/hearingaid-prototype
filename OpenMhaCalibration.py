#!/usr/bin/python3

#
# Calibration Meter using the openMHA TCP/IP Interface
#
# @author Tobias Bruns
# @version 0.1
# @date 03.04.2019


import socket, time




class OpenMhaCalibration(object):

    _openMhaAddr = "127.0.0.1"; #standard address
    _openMhaPort = 33337; #standard port
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
        self._conn.close()
    
        
    def ShowCalibrationLevels(self,dur_sec=30):
        msg = 'mha.transducers.calib_in.rmslevel?\n'
        time_intervall = 4 # Hz
        
        for idx in range(int(dur_sec*time_intervall)):
            self._conn.send(msg.encode('utf-8'))
            print(self._conn.recv(1024).decode('utf-8'))
            time.sleep(1/time_intervall)

        self.close()
        
            
    
if __name__ == "__main__":

    openMHACalibration = OpenMhaCalibration();
    openMHACalibration.ShowCalibrationLevels(4);
