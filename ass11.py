#Que1-->Print the current day using datetime module
import datetime
x=datetime.date.today()
'''here datetime is the module , date is the class in the /
    module and today is the function'''
print(x.day)
print()

#Que2-->Open your browser and play a video using webbrowser module in python.
import webbrowser
webbrowser.open("https://www.youtube.com/watch?v=92S4zgXN17o&t=0s&"   #NOQA
                "index=2&list=PL2_aWCzGMAwI3W_JlcBbtYTwiQSsOTa6P")
print()

#Que3-->Write a program to rename all the files in a directory and convert them into .jpg file format
import os,sys
folder = r'C:\Users\admin\Desktop\ass11doc'
for file in os.listdir(folder):    
    infile = os.path.join(folder,file)
    if not os.path.isfile(infile):
        continue
    oldbase = os.path.splitext(file)
    newname = infile.replace('.txt', '.jpg')
    output = os.rename(infile, newname)
