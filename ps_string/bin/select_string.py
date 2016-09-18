#!/usr/bin/python
# coding: utf-8

import argparse
import os
import sys,fileinput
sys.path.insert(0, os.path.abspath('../..'))
from ps_string import lib


def main():
    parser = argparse.ArgumentParser(
        description="""
            ファイルの内容またはパイプから受取った入力文字列から
            パターンに合致する文字列を抽出します。
            """)
    parser.add_argument(
        "--path",
        default="-",
        help="ファイルのパス。")
    parser.add_argument(
        "pattern",
        help="検索する文字列パターン。")
    args = parser.parse_args()
    input_list=fileinput.input(args.path)
    result = lib.select_string(input_list,args.pattern)

    if len(result) > 0:
        for i in result:
            print i

if __name__ == "__main__":
    main()
