#!/usr/bin/python
# coding: utf-8

import argparse
import os
import sys
sys.path.insert(0, os.path.abspath('../..'))
from ps_item import lib


def main():
    parser = argparse.ArgumentParser(
        description="ファイル / ディレクトリを削除します。")
    parser.add_argument(
        "path",
        help="削除するファイル / ディレクトリのパス。")
    parser.add_argument(
        "--recurse",
        action="store_true",
        default=False,
        help="ディレクトリを再起的に削除します。")
    args = parser.parse_args()
    lib.remove_item(args.path, args.recurse)

if __name__ == "__main__":
    main()
