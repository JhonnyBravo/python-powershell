# coding: utf-8
import os

def test_path(path,path_type="any"):
    if path_type=="leaf":
        result=os.path.isfile(path)
    elif path_type=="container":
        result=os.path.isdir(path)
    elif path_type=="any":
        result=os.path.exists(path)

    return result

def split_path(path,leaf,qualifier,parent):
    if leaf:
        result=os.path.basename(path)
    elif qualifier:
        result_list=os.path.splitdrive(path)
        result=result_list[0]
    elif parent:
        result=os.path.dirname(path)

    return result
