# coding: utf-8
import os


def test_path(path, path_type="any"):
    """
    指定した path が存在するかどうかを確認します。

    :param str path: 存在を確認するファイル / ディレクトリの path 。
    :param str path_type:
        * leaf: 指定した path がファイルである場合に True を返します。
        * container: 指定した path がディレクトリである場合に True を返します。
        * any: ファイルであるかディレクトリであるかを問わず、
          指定した path が存在すれば True を返します。
    :return: path が存在する場合は True を存在しない場合は False を返します。
    :rtype: bool
    """
    if path_type == "leaf":
        result = os.path.isfile(path)
    elif path_type == "container":
        result = os.path.isdir(path)
    elif path_type == "any":
        result = os.path.exists(path)

    return result


def split_path(path, leaf, qualifier, parent):
    """
    指定したパスの一部分を取得します。

    :param str path: ファイル / ディレクトリの path 。
    :param bool leaf: True を指定した場合は path の末尾を取得して返します。
    :param bool qualifier: True を指定した場合はドライブ名を返します。

        .. note::
            Windows のみ。

    :param bool parent: True を指定した場合は path の親ディレクトリを返します。
    :return: パスの一部分。
    :rtype: str
    """
    if leaf:
        result = os.path.basename(path)
    elif qualifier:
        result_list = os.path.splitdrive(path)
        result = result_list[0]
    elif parent:
        result = os.path.dirname(path)

    return result
