# coding: utf-8
import os
import sys
import shutil


def new_item(path, item_type, value=""):
    if os.path.exists(path):
        print path + " は既に存在します。"
        sys.exit(1)

    if item_type == "file":
        if value:
            with open(path, 'wt') as file:
                file.write(value + "\n")
        else:
            open(path, "wb").close()
    elif item_type == "directory":
        os.makedirs(path)

    print path + " を作成しました。"
    sys.exit(0)


def remove_item(path, recurse=False):
    if not os.path.exists(path):
        print path + " は存在しません。"
        sys.exit(1)

    if os.path.isfile(path):
        os.remove(path)
    elif os.path.isdir(path) and recurse:
        shutil.rmtree(path)
    elif os.path.isdir(path) and not recurse:
        os.rmdir(path)

    print path + " を削除しました。"
    sys.exit(0)


def copy_item(path, destination):
    if not os.path.exists(path):
        print path + " は存在しません。"
        sys.exit(1)

    if os.path.isfile(path):
        shutil.copy(path, destination)
    elif os.path.isdir(path):
        shutil.copytree(path, destination)

    print path + " を " + destination + " へコピーしました。"
    sys.exit(0)


def move_item(path, destination):
    if not os.path.exists(path):
        print path + " は存在しません。"
        sys.exit(1)

    shutil.move(path, destination)
    print path + " を " + destination + " へ移動しました。"
    sys.exit(0)


def get_child_item(path=".", recurse=False):
    if not os.path.exists(path):
        print path + " は存在しません。"
        sys.exit(1)

    if not recurse:
        result = os.listdir(path)
    elif recurse:
        base_list = os.walk(path)
        dir_list = []
        result = []

        for root, dirs, files in base_list:
            dir_list.append(root)

        for i in dir_list:
            content_list = os.listdir(i)

            for j in content_list:
                result.append(os.path.join(i, j))

    result.sort()
    return result
