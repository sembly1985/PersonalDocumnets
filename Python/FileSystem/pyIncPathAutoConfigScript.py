from enumFiles import enumFiles
import sys
import os
import shutil
#pyNurseScript.py ..\..\..\ "NurseRobot_Gold" ..\..\..\..\MDK-ARM\TimerTest.uvprojx
RobotPath=sys.argv[1];

#RobotPath="..\\..\\..\\"
#groupName="NurseRobot_Gold"
#keilPrj="..\..\..\..\MDK-ARM\TimerTest.uvprojx"
#print os.path.abspath(keilPrj)

''' enum all .c and .h file '''
h_list=enumFiles(RobotPath,'.h');

pathNames=[];
for item in h_list:
    ''' check if from Public or Config '''
    pathName=os.path.abspath(item);
    temp=os.path.split(pathName);
    pureName=temp[1];
    purePath=temp[0];
    temp=os.path.split(purePath);
    parentPath=temp[1];
    if(parentPath=="PublicInt" or "config"==parentPath):
        pathNames.append(pathName);
        print(pathName)
        shutil.copyfile(pathName, os.path.join(RobotPath,"..\\UserInc",pureName))
        shutil.copystat(pathName, os.path.join(RobotPath,"..\\UserInc",pureName))