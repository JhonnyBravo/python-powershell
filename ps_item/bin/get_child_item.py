#!/usr/bin/python
# coding: utf-8

import argparse
import os
import sys
sys.path.insert(0, os.path.abspath('../..'))
from ps_item import lib


def main():
    parser = argparse.ArgumentParser(
        description="ファイル / ディレクトリの一覧を表示します。")
    parser.add_argument(
        "--path",
        help="一覧を取得するディレクトリのパス。",
        default=".")
    parser.add_argument(
        "--recurse",
        action="store_true",
        default=False,
        help="一覧を再起的に取得します。")
    args = parser.parse_args()
    result=lib.get_child_item(args.path, args.recurse)

    if len(result)>0:
        print ""

        for i in result:
            if os.path.isdir(i):
                print "\nディレクトリ: "+i+"\n"
            else:
                print i

        sys.exit(0)

if __name__ == "__main__":
    main()
