# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 08:55:47 2016

@author: wangsp1
"""
import serial
import _thread
import runTime
import time
class MultiThreadCom:
    Ser=serial.Serial();
    readLock=_thread.allocate_lock();
    ReadStatus=0;
    retStr=[];
    # initial serial port
    def __init__(self,comport='COM1',baudRate=0,timeout_value=0.01,dataBit=8,stopBit=1):
        self.Ser=serial.Serial(port=comport,baudrate=baudRate,bytesize=dataBit,stopbits=stopBit,timeout=timeout_value);
        self.ReadStatus=1;
        
    def Close(self):
        self.ReadStatus=0;
        self.Ser.close();
        
    def StartReadThread(self):
        _thread.start_new_thread(self.Read,())
        self.ReadStatus=2;
        #
    def StopReadThread(self):
        #
        pass;
        
    def ClrReadBuff(self):
        self.readLock.acquire();
        self.retStr=[];
        self.ClrCOM();
        self.readLock.release();
        #
    def ClrCOM(self):
        self.Ser.readall();
        
        #
    def Send(self,buff):
        self.Ser.write(buff);
        self.Ser.flush();
        #
    def Receive_Timeout(self,dataCount,timeOut):
        rt=runTime.runTime();
        while(self.GetReadBuffLength()<dataCount):
            if(rt.DeltaMiniTime()>timeOut):
                return '';
                break;
        return self.Receive(dataCount);
        pass;
        
    def Receive(self,dataCount):
        while(self.GetReadBuffLength()<dataCount):
            pass;
        self.readLock.acquire();
        ret=self.retStr[0:dataCount];
        self.retStr=self.retStr[dataCount:];
        self.readLock.release();
        return ret
        #
    def TryReceive(self,dataCount):
        current_len=self.GetReadBuffLength()
        self.readLock.acquire();
        if(current_len<=dataCount):
            ret=self.retStr;
            self.retStr=[];
        else:
            ret=self.retStr[0:dataCount];
            self.retStr=self.retStr[dataCount:];
        self.readLock.release();
        return ret
        #
    def GetReadBuffLength(self):
        self.readLock.acquire();
        tmp=len(self.retStr);
        self.readLock.release();
        return tmp;
        
    def GetAllReadBuff(self):
        return self.retStr;
        
    def ReadCom(self):
        return list(self.Ser.readall());
        
    def Read(self):
        while(1):
            time.sleep(0.01);
            if(self.ReadStatus==2):
                self.readLock.acquire();
                self.retStr=self.retStr+self.ReadCom();
                self.readLock.release();
            else:
                if(self.ReadStatus==0):
                    break;
        _thread.exit_thread();