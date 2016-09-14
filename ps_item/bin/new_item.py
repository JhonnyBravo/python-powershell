#!/usr/bin/python
# coding: utf-8

import argparse
import os
import sys
sys.path.insert(0, os.path.abspath('../..'))
from ps_item import lib


def main():
    parser = argparse.ArgumentParser(
        description="ファイル / ディレクトリを新規作成します。")
    parser.add_argument(
        "path",
        help="作成するファイル / ディレクトリのパス。")
    parser.add_argument(
        "--item-type",
        choices=["file", "directory"],
        default="file",
        help="""
                * file: ファイルを作成します。
                * directory: ディレクトリを作成します。
                """)
    parser.add_argument(
        "--value",
        default="",
        help="ファイルへ書込む値。")
    args = parser.parse_args()
    lib.new_item(args.path, args.item_type, args.value)

if __name__ == "__main__":
    main()
