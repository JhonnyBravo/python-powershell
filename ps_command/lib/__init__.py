# coding: utf-8

import subprocess


def invoke_command(command_list):
    """
    シェルコマンドを実行します。

    :param list command_list: 実行するコマンドを収めた配列。
    """
    subprocess.call(command_list)
