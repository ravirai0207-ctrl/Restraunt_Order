#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 20 12:08:20 2025

@author: raviprakashrai
"""

def o1():
    a=int(input("Enter item no. : "))
    b=int(input("Enter item quantity: "))
    l=[150,100,100,250]
    nl=["Paneer Tikka","Dahi Puri","Vegetable Samosa","Tandoori Gobi"]
    return nl[a-1],l[a-1]*b,b
def o2():
    a=int(input("Enter item no. : "))
    b=int(input("Enter item quantity: "))
    l=[450,300,400,350]
    nl=["Paneer Butter Masala","Dal Makhani","Veg Biryani","Bhindi Masala"]
    return nl[a-1],l[a-1]*b,b
def o3():
    a=int(input("Enter item no. : "))
    b=int(input("Enter item quantity: "))
    l=[70,100,100,250]
    nl=["Gulab Jamun","Rasmalai","Gajar Halwa","Kesar Pista Kulfi"]
    return nl[a-1],l[a-1]*b,b
def o4():
    a=int(input("Enter item no. : "))
    b=int(input("Enter item quantity: "))
    l=[50,60,45,25]
    nl=["Butter Naan","Garlic Naan","Tandoori Roti","Butter Roti"]
    return nl[a-1],l[a-1]*b,b

