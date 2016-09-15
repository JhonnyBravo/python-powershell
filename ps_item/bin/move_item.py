#!/usr/bin/python
# coding: utf-8

import argparse
import os
import sys
sys.path.insert(0, os.path.abspath('../..'))
from ps_item import lib


def main():
    parser = argparse.ArgumentParser(
        description="ファイル / ディレクトリの移動 / 名称変更を実行します。")
    parser.add_argument(
        "path",
        help="移動するファイル / ディレクトリのパス。")
    parser.add_argument(
        "destination",
        help="移動先のパス。")
    args = parser.parse_args()
    lib.move_item(args.path, args.destination)

if __name__ == "__main__":
    main()
