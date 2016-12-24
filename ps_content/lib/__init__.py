# coding: utf-8
import os
import sys
import fileinput


def test_path(path):
    """
    指定したパスが存在するかどうかを確認します。

    :param str path: 存在を確認する path 。
        path が存在しない場合、または path がディレクトリである場合は
        終了ステータス 1 を返して終了します。
    """
    if not os.path.exists(path):
        print(path + " は存在しません。")
        sys.exit(1)
    elif os.path.isdir(path):
        print(path + " はディレクトリです。")
        sys.exit(1)


def write_content(path, value, append_text=False):
    """
    ファイルへの書込を実行します。

    :param str path: 書込を実行するファイルのパス。
        ファイルが存在しない場合は新規作成します。
    :param str value: ファイルへ書き込む値。
    :param bool append_text: True を指定した場合はファイル末尾へ追記し、
        False を指定した場合はファイルの内容を上書きします。
        既定値は False です。
    """
    if not append_text:
        mode = "wt"
    elif append_text:
        mode = "at"

    with open(path, mode) as file:
        file.write(value + "\n")

    sys.exit(0)


def clear_content(path):
    """
    ファイルの内容を削除します。

    :param str path: 内容を削除するファイルのパス。
    """
    test_path(path)

    with open(path, "wt") as file:
        file.write("")

    sys.exit(0)


def get_content(path):
    """
    ファイルの内容を取得し、配列に収めて返します。

    :param str path: 読み込むファイルの path 。
    :return: 行単位で区切ったファイル内容の配列。
    :rtype: list
    """
    test_path(path)

    result = []

    for line in fileinput.input(path):
        result.append(line.rstrip("\r\n"))

    fileinput.close()
    return result
