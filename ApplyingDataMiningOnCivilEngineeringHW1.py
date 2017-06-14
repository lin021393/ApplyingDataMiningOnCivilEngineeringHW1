import re
import matplotlib.pyplot as plt
import numpy as np
import statistics
import scipy
from scipy import stats

def ascending(a, b): 	#	有參考教育資源
	return a - b
def descending(a, b): 	#	有參考教育資源
	return -ascending(a, b)

def insertionSort(inList, comparing = ascending):	#	有參考教育資源
    return ([] if not inList
               else __insert(inList[0], 
                   insertionSort(inList[1:], comparing), comparing))
        
def __insert(x, inList, comparing):		#	有參考教育資源
    return ([x] + inList if not inList or comparing(x, inList[0]) <= 0
                     else [inList[0]] + __insert(x, inList[1:], comparing))
					 
def running_mean(l, N):		#	有參考stackoverflow的資料
    sum = 0
    result = list( 0 for x in l)

    for i in range( 0, N ):
        sum = sum + l[i]
        result[i] = sum / (i+1)

    for i in range( N, len(l) ):
        sum = sum - l[i-N] + l[i]
        result[i] = sum / N

    return result
					 
file=open('ori_data_hw01.txt','r')	# 開檔讀檔
x=[]
y=[]
y1=[]
y2=[]
y3=[]

while True:		
	line = file.readline()
	elements=re.split(r'[;,=\s]\s*', line)
	if not line: break
	x.append(float(elements[0]))
	y.append(float(elements[1]))
	
#print(insertionSort(y, descending))

y1=insertionSort(y, descending)
#print(y1)

#print(y1)
#print(min(y1[0:6]))

numBin=0
numBin=input('bin size: ')
#numBin=1
InumBin=int(numBin)
# bin=7

j=0

i=0
while i<=len(y1)-1:
	if i%InumBin==InumBin-1:
		Maximum=max(y[j:i+1])
		Minimun=min(y[j:i+1])
		Mean=statistics.mean(y[j:i+1])
		while  j<=i-1:
			if j<=i:
				y1[j]=Minimun
			else:
				y1[j]=Maximum
			j=j+1
	i +=1

#print(running_mean(y, 201))
#print(scipy.stats.pearsonr(y, y1))
#plt.plot(x, y, "go", ms=1)
#plt.plot(x, y1)

print("S: ", scipy.stats.pearsonr(y, y1))

plt.plot(x, y, "b.")
plt.plot(x, y1, "g")
#plt.plot(x, running_mean(y, InumBin), "g")

plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.savefig("test_BinBoundaries_bin85.png")
plt.show()
