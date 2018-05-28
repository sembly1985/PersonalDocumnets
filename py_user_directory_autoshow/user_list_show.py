import os
from cmd_color_printers import *

def reloadList():
    global list_array
    list_file=open('user_list.txt');
    list_array=[];
    while(1):
        line=list_file.readline();
        if not line:
            break;
        if(line[-1]=='\n'):
            list_array.append(line[0:-1]);
        else:
            list_array.append(line);
    ''' print each item in list '''
    print("********************************")
    for i in range(0,len(list_array)):
        space_Index=str.find(list_array[i],' ')
        print(i,list_array[i][0:space_Index]);
    list_file.close()

list_array=[];
reloadList();

while(1):
    ''' input item '''
    set_cmd_text_color(FOREGROUND_RED)
    item=input('plsea input item, o(open list),r(reload),-1(exit):');
    resetColor()
    try:
        if(item=='o'):
            os.startfile('user_list.txt')
            continue
        if(item=='r'):
            reloadList();
            continue
        if(int(item)==-1):
            break
        list_item=list_array[int(item)];
        space_Index=str.find(list_item,' ')
        foldStr=list_item[space_Index+1:]
        os.startfile(foldStr);
    except:
        print('error select');