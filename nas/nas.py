import os
import re

home = "/home/moog/nas"
chak = "/착샷"
bak = "/바닥샷"
chakList = os.listdir(home + chak)
bakList = os.listdir(home + bak)
clist = []
fileName = "error.txt"
chakReJPG = re.compile('[A-Z]+[0-9]+[0-9]+[0-9]+[_]+[0-9]+[0-9]+[0-9]')
chakReMP4 = re.compile('[A-Z]+[0-9]+[0-9]+[0-9]+')
bakJPG = re.compile('[0-9]+[0-9]+[0-9]+[0-9]+[0-9]+[0-9]+[0-9]+[ ]+[A-Z]')

with open(fileName, 'w') as f:
        f.write("%s" % "")
f.close()

for i in chakList :
  chakList1 = home+chak+"/"+i
  chakList2 = os.listdir(chakList1)
  for j in chakList2 :
    chakList3 = chakList1 + "/" + j
    chakList4 = os.listdir(chakList3)
    for k in chakList4 :
      tmp = os.path.splitext(k)
      if tmp[1] == '':
        chakList5 = os.listdir(chakList3 + "/" + tmp[0])
        path = str(chakList3+ "/" + tmp[0] + "/")
        with open(fileName, 'a') as f:
          for item in chakList5:
              file = os.path.splitext(item)
              if file[1] == '.jpg':
                if chakReJPG.match(file[0]) == None:
                  finalPath = path + item
                  ff = finalPath[15:]
                  f.write("%s\n" % ff)
              elif file[1] == '.MP4':
                if chakReMP4.match(file[0]) == None:
                  finalPath = path + item
                  ff = finalPath[15:]
                  f.write("%s\n" % ff)
        f.close()

for i in bakList :
  # 1007
  chakList1 = home+bak+"/"+i
  chakList2 = os.listdir(chakList1)
  for j in chakList2 :
    file = os.path.splitext(j)
    with open(fileName, 'a') as f:
      if file[1] == '.jpg':
        if bakJPG.match(file[0]) == None:
          finalPath = chakList1 + "/" + j
          ff = finalPath[15:]
          f.write("%s\n" % ff)
  f.close()
