# coding: utf-8
import os
import sys
import shutil


def test_path(path):
    """
    指定した path が存在するかどうかを確認します。
    指定した path が存在しない場合は終了ステータス 1 を返して終了します。

    :param str path: 存在を確認する path 。
    """
    if not os.path.exists(path):
        print(path + " は存在しません。")
        sys.exit(1)


def new_item(path, item_type, value=""):
    """
    ファイル / ディレクトリを新規作成します。
    指定した path が既に存在する場合は終了ステータス 1 を
    返して終了します。

    :param str path: 作成するファイル / ディレクトリの path 。
    :param str item_type:
        * file: ファイルを作成します。
        * directory: ディレクトリを作成します。
    :param str value: ファイルへ書き込む値。
    """
    if os.path.exists(path):
        print(path + " は既に存在します。")
        sys.exit(1)

    if item_type == "file":
        if value:
            with open(path, 'wt') as file:
                file.write(value + "\n")
        else:
            open(path, "wb").close()
    elif item_type == "directory":
        os.makedirs(path)

    print(path + " を作成しました。")


def remove_item(path, recurse=False):
    """
    指定した path を削除します。
    指定した path が存在しない場合は終了ステータス 1 を返して終了します。

    :param str path: 削除するファイル / ディレクトリの path 。
    :param bool recurse: True を指定した場合は再帰的な削除を実行します。
        False を指定した場合はファイルまたは空のディレクトリを削除します。
    """
    test_path(path)

    if os.path.isfile(path):
        os.remove(path)
    elif os.path.isdir(path) and recurse:
        shutil.rmtree(path)
    elif os.path.isdir(path) and not recurse:
        os.rmdir(path)

    print(path + " を削除しました。")


def copy_item(path, destination):
    """
    ファイル / ディレクトリをコピーします。
    指定した path が存在しない場合は終了ステータス 1 を返して終了します。

    :param str path: コピー元ファイル / ディレクトリのパス。
        ディレクトリを指定した場合は再帰的にコピーします。
    :param str destination: コピー先のパス。
    """
    test_path(path)

    if os.path.isfile(path):
        shutil.copy(path, destination)
    elif os.path.isdir(path):
        shutil.copytree(path, destination)

    print(path + " を " + destination + " へコピーしました。")


def move_item(path, destination):
    """
    ファイル / ディレクトリの移動または名前の変更を実行します。
    指定した path が存在しない場合は終了ステータス 1 を返して終了します。

    :param str path: 移動元ファイル / ディレクトリのパス。
    :param str destination: 移動先ファイル / ディレクトリのパス。
    """
    test_path(path)

    shutil.move(path, destination)
    print(path + " を " + destination + " へ移動しました。")


def get_child_item(path=".", recurse=False):
    """
    指定した path に存在するファイル / ディレクトリの一覧を
    配列に収めて返します。
    指定した path が存在しない場合は終了ステータス 1 を返して終了します。

    :param str path: 一覧を取得するディレクトリの path 。
        既定値は現在のディレクトリです。
    :param bool recurse: True を指定した場合は再帰的に一覧を取得します。
        既定値は False です。
    :return: ファイル / ディレクトリの一覧を収めた配列。
    :rtype: list
    """
    test_path(path)

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
