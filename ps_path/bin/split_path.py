#!/usr/bin/python
# coding: utf-8

import argparse
import os
import sys
sys.path.insert(0, os.path.abspath('../..'))
from ps_path import lib


def main():
    parser = argparse.ArgumentParser(
        description="パスを分割して返します。")
    parser.add_argument(
        "path",
        help="分割するパス。")
    parser.add_argument(
        "--leaf",
        action="store_true",
        default=False,
        help="パスの末尾を返します。")
    parser.add_argument(
        "--qualifier",
        action="store_true",
        default=False,
        help="パスのドライブ名を返します。")
    parser.add_argument(
        "--parent",
        action="store_true",
        default=False,
        help="パスの親ディレクトリを返します。")
    args = parser.parse_args()

    if not args.leaf and not args.qualifier:
        args.parent = True

    result = lib.split_path(args.path, args.leaf, args.qualifier, args.parent)

    print(result)
    sys.exit(0)

if __name__ == "__main__":
    main()
