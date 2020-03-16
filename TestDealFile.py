#把所有文件处理
import os,shutil
import csv

filepath = os.getcwd()
txtfiles = []
newfilepath = "C:\\Users\\Too_K\\Desktop\\助教\\vb1-hw2"
if not os.path.exists(newfilepath):
    os.makedirs(newfilepath)

with open('2020-03-11.csv','r',encoding='UTF-8') as csvfile:
    reader = csv.reader(csvfile)
    column = [[row[0],row[2]] for row in reader if '.07' in row[3]]
print(column[:-2])

for root,dirs,files in os.walk(r"%s"%filepath):
    for file in files:
        if file[-3:]=="rar" or file[-3:]=="zip":
            for num in column:
                if num[1] in file:
                    shutil.copy(file, "%s\\%s" % (newfilepath, num[1]+num[0]+file[-4:]))
