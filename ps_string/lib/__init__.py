# coding: utf8
import os,sys,re

def select_string(string_list,pattern):
    result=[]

    for line in string_list:
        if re.search(pattern,line):
            result.append(line.rstrip("\r\n"))

    return result
