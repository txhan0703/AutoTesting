#提取文件夹下所有日志文件并重命名
import os,shutil

filepath = os.getcwd()
txtfiles = []
newfilepath = "C:\\Users\\Too_K\\Desktop\\HuaweiJS\\BuildLogData"

for root,dirs,files in os.walk(r"%s"%filepath):
    for file in files:
        if(file[-3:]=="txt"):
            t = os.path.join(root, file)
            txtfiles.append(t)

for file in txtfiles:
    with open(file, encoding='utf-8') as f:
        s = ""
        while "Build Project Name" not in s:
            s = f.readline()
        timeinfo = s[1:20].replace("-","").replace(" ","").replace(":","")
        newfilename = s.split("Build Project Name")[1][4:-1]+" "+timeinfo
        print(newfilename)
        shutil.copy(file,"%s\\%s.txt"%(newfilepath,newfilename))



