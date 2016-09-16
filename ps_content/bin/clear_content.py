#!/usr/bin/python
# coding: utf-8

import argparse
import os
import sys
sys.path.insert(0, os.path.abspath('../..'))
from ps_content import lib


def main():
    parser = argparse.ArgumentParser(
        description="ファイルの内容を削除します。")
    parser.add_argument(
        "path",
        help="ファイルのパス。")
    args = parser.parse_args()
    lib.clear_content(args.path)

if __name__ == "__main__":
    main()
