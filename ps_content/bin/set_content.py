#!/usr/bin/python
# coding: utf-8

import argparse
import os
import sys
sys.path.insert(0, os.path.abspath('../..'))
from ps_content import lib


def main():
    parser = argparse.ArgumentParser(
        description="ファイルへ値を書込みます。")
    parser.add_argument(
        "path",
        help="""
            値を書込むファイルのパス。
            ファイルが存在しない場合はファイルを新規作成し、
            既に存在する場合は内容を上書きします。
            """)
    parser.add_argument(
        "value",
        help="ファイルへ書込む値。")
    args = parser.parse_args()
    lib.write_content(args.path, args.value, False)

if __name__ == "__main__":
    main()
