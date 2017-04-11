import os
list_file=open('user_directory_list.txt');
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
for i in range(0,len(list_array)):
    print i, list_array[i];
''' input item '''
item=raw_input('plsea input item:');
try:
    list_item=list_array[int(item)];
    tmp_array=str.split(list_item,' ');
    os.startfile(tmp_array[1]);
except:
    print 'error select';