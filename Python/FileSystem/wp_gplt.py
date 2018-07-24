''' wrapper of gnuplot '''
from subprocess import Popen as _Popen,PIPE as _PIPE
import time
import os
class gplt:
	"""docstring for gplt"""
	def __init__(self, gpltpath):
		self.gpltpath = gpltpath
		self.terminalIndex=0
	def start(self):
		self.gnuplot = _Popen([self.gpltpath,'-p'],shell=False,stdin=_PIPE,universal_newlines=True)
	def close(self):
		self.gnuplot.stdin.close()
		self.gnuplot.terminate()

	def writeCmd(self,cmdstr):
		print(cmdstr)
		self.gnuplot.stdin.write((cmdstr+'\n'));
		self.gnuplot.stdin.flush();

	def figure(self):
		self.writeCmd('set terminal wxt '+str(self.terminalIndex) + '\n');
		self.terminalIndex+=1

	def plot(self,line_list):

		fileArray=[];
		for i in range(0,len(line_list)):
			fileArray.append(self.array2file(line_list[i][0],line_list[i][1],i));
		# build plot cmd
		cmdStr='plot '
		for i in range(0,len(fileArray)):
			if(i==(len(fileArray)-1)):
				tmpStr="'"+fileArray[i]+"'"+' '+line_list[i][2]
			else:
				tmpStr="'"+fileArray[i]+"'"+' '+line_list[i][2]+','
			cmdStr+=tmpStr
		self.writeCmd(cmdStr)

#		time.sleep(2)
#		for i in range(0,len(fileArray)):
#			os.remove(fileArray[i])

		pass

	def array2file(self,x_array,y_array,index):
#		curTime=int(time.time()*10000);
#		filename=str(curTime)+'.txt'
		filename="gnuplot_tmp_datafile_"+str(index)+".txt"
		filehandle=open(filename,'w')
		for i in range(0,len(x_array)):
			filehandle.write(str(x_array[i])+' '+str(y_array[i])+'\n');
		filehandle.close();
		return filename