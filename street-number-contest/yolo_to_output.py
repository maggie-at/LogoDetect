import os


img_dir='./data/images/mchar_test_a/' #测试图片路径  
label_dir='./runs/detect/exp3/labels/' #识别结果路径  
out_dir = './runs/detect/exp3/' # 输出的 txt 文件路径  
  
  
# 获取列表的第二个元素  
def takeSecond(elem):  
    return elem[1]  
  
# 读取  
dirs=os.listdir(img_dir)  
  
fp = open(out_dir+'result.csv', mode="w+", encoding="utf-8")  
  
for file in dirs:  
  
    txtFileName=file.title().split(".")[0]+'.txt'  
  
    listCode = []  
  
    if os.access(label_dir+txtFileName,os.F_OK):  
  
        with open(label_dir+txtFileName, "r") as f:  
            for line in f.readlines():  
                tmp = line.split(' ') 
                listCode.append((tmp[0],float(tmp[1])))  
  
    # 按tmp[1]从小到大排序  
    listCode.sort(key=takeSecond)  
  
    theNumber=''  
    for code in listCode:  
        theNumber+=code[0]  
  
    #保存到文件，格式：fileName,theNumber   
    fileName=file.title()    
    fp.write(fileName+','+ theNumber+ '\n')
    
fp.close()