#!/usr/bin/python
# coding: utf-8

import argparse
import os
import sys
sys.path.insert(0, os.path.abspath('../..'))
from ps_item import lib


def main():
    parser = argparse.ArgumentParser(
        description="ファイル / ディレクトリをコピーします。")
    parser.add_argument(
        "path",
        help="コピーするファイル / ディレクトリのパス。")
    parser.add_argument(
        "destination",
        help="コピー先のパス。")
    args = parser.parse_args()
    lib.copy_item(args.path, args.destination)

if __name__ == "__main__":
    main()
