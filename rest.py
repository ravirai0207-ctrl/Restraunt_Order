#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 20 12:16:00 2025

@author: raviprakashrai
"""


print("Welcome to our Restaurant")
import menu
import order
j=1
def st(i):
    z=""
    it,pr,q="",0,0
    k=int(input("Enter 1 for starter 2 for main cource  3 for dessert & 4 for roti and naan"))
    if(k==1):
        menu.dis1()
        it,pr,q=order.o1()
    elif(k==2):
        menu.dis2()
        it,pr,q=order.o2()
    elif(k==3):
        menu.dis3()
        it,pr,q=order.o3()
    elif(k==4):
        menu.dis4()
        it,pr,q=order.o4()
    z=z+str(i)+"\t\t"+str(q)+"\t\t\t"+str(pr)+"\t\t"+it+"\n"
    k=int(input("Want to order more 1 for yes 2 for no"))
    if(k==1):
        return z+st(i+1)
    elif(k==2):
        return z
    else:
        return "wrong input"
print("\n\n\t\t\tBill\n\n","Sno.\tQuantity\t\tPrice\tItem\n",st(j))

