# 利用向量间的相似度
import jieba
import math
def countKey(fileName,resultName):
    #分词
    lineNums=len(open(fileName,"r",encoding="utf-8").readline())
    print("文本的行数:"+str(lineNums))
    i = 0
    table = {}
    source = open(fileName,'r',encoding="utf-8")
    result = open(resultName,'w',encoding="utf-8")
    while i<lineNums:
        line=source.readline()
        words=[word for word in jieba.cut(line)]
        for word in words:
            if word!="" and word in table:
                num=table[word]
                table[word]=num+1
            else:
                table[word]=1
        i=i+1

#键值从大到小排序 函数原型：sorted(dic,value,reverse)
    dic = sorted(dict2list(table),key=lambda d:d[1] ,reverse=True)
    print(dic)
    for i in range(len(dic)):
        result.write('<'+dic[i][0]+':'+str(dic[i][1])+'>')
    return dic

#统计关键词及个数 并计算相似度
def MergeKeys(dic1,dic2):
    arrayKey = []
    for i in range(len(dic1)):
         arrayKey.append(dic1[i][0])
    for i in range(len(dic1)):
         if dic1[i][0] in arrayKey:
             print('has_key',dic2[i][0])
         else:
            arrayKey.append(dic1[i][0])
    print (arrayKey)
    #计算词频

    arrayNum1 = [0]*len(arrayKey)
    arrayNum2 = [0]*len(arrayKey)
 
     #构造第一个文本的向量
    for i in range(len(dic1)):

        key = dic1[i][0]
        value = dic1[i][1]
        j = 0
        while j < len(arrayKey):
             if key == arrayKey[j]:
                arrayNum1[j] = value
                break
             else:
                j=j+1
    # #构造第二个文本的向量
    for i in range(len(dic2)):
        key = dic2[i][0]
        value = dic2[i][1]
        j = 0
        while j < len(arrayKey):
             if key == arrayKey[j]:
                arrayNum2[j] = value
                break
             else:
                j=j+1

    # 求两个向量的余弦值
    #计算两个向量的点积
    x = 0
    i = 0
    while i<len(arrayKey):
        x=x+arrayNum1[i]*arrayNum2[i]
        i=i+1
    print (x)
    #计算两个向量的模
    #计算第一个文本向量的模
    a=0
    i=0
    while i<len(arrayNum1):
        a=a+arrayNum1[i]*arrayNum1[i]
        i=i+1
    #计算第二个文本向量的模
    b=0
    i=0
    while i<len(arrayNum2):
        b=b+arrayNum2[i]*arrayNum2[i]
        i=i+1
    result=float(x)/(math.sqrt(a)*math.sqrt(b))
    return result
#将字典转为列表
def dict2list(dic:dict):
    keys=dic.keys()
    values=dic.values()
    lst=[(key,value) for key,value in zip(keys,values)]
    return lst
#主入口
if __name__ == '__main__':
    fileName="input.txt"
    resultName="result_1.txt"
    dic1=countKey(fileName,resultName)
    fileName2="input2.txt"
    resultName2="result_2.txt"
    dic2=countKey(fileName2,resultName)
    result=MergeKeys(dic1,dic2)
    print (result)