#!/usr/bin/python
# coding: utf-8

import argparse
import os
import sys
sys.path.insert(0, os.path.abspath('../..'))
from ps_command import lib


def main():
    parser = argparse.ArgumentParser(
        description="シェルコマンドを Python 経由で実行します。")
    parser.add_argument(
        "command",
        help="実行するコマンド。")
    parser.add_argument(
        "args_list",
        nargs="*",
        help="コマンドへ渡す引数。")
    args = parser.parse_args()

    join_args = " ".join(args.args_list)
    command = args.command + " " + join_args

    lib.invoke_command(command.split())

if __name__ == "__main__":
    main()
