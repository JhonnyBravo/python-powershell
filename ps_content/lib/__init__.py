# coding: utf-8
import os
import sys
import fileinput


def write_content(path, value, append_text=False):
    if not append_text:
        mode = "wt"
    elif append_text:
        mode = "at"

    with open(path, mode) as file:
        file.write(value + "\n")

    sys.exit(0)


def clear_content(path):
    if not os.path.exists(path):
        print path + " は存在しません。"
        sys.exit(1)
    elif os.path.isdir(path):
        print path + " はディレクトリです。"
        sys.exit(1)

    with open(path, "wt") as file:
        file.write("")

    sys.exit(0)


def get_content(path):
    if not os.path.exists(path):
        print path + " は存在しません。"
        sys.exit(1)
    elif os.path.isdir(path):
        print path + " はディレクトリです。"
        sys.exit(1)

    result = []

    for line in fileinput.input(path):
        result.append(line.rstrip("\r\n"))

    fileinput.close()
    return result
