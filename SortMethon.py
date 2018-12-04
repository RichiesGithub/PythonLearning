#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = 'qli25'

#冒泡排序
List=[34,6,3,88,23,61,90,34,26,63,42]
L=len(List)
for i in range(L):
    for j in range(L-1):
        if List[j]>List[j+1]:
            List[j],List[j+1] = List[j+1],List[j]
print List

#快速排序
def QuickSort(Start,end,myList):
    if Start<end:
        i,j = Start,end
        #设置基准数
        base=myList[0]
        while(i<j):
            while(i<j)and (myList[j]>=base):
                j-=1
            myList[i]=myList[j]
            while(i<j) and (myList[i]<=base):
                i+=1
            myList[j]=myList[i]
        myList[i]=base
        QuickSort(Start,i-1,myList,)
        QuickSort(j+1,end,myList)
    return myList

myList = [34,6,3,88,23,61,90,34,26,63,42]
QuickSort(0,len(myList)-1,myList)
print myList