#!/usr/bin/python
# coding: utf-8

import argparse
import os
import sys
sys.path.insert(0, os.path.abspath('../..'))
from ps_path import lib


def main():
    parser = argparse.ArgumentParser(
        description="""
            ファイル / ディレクトリが存在するかどうかを真偽値で返します。
            """)
    parser.add_argument(
        "path",
        help="存在を確認するパス。")
    parser.add_argument(
        "--path-type",
        choices=["any", "leaf", "container"],
        default="any",
        help="""
            * leaf: 指定したパスが存在し、
              かつファイルである場合に True を返します。

            * container: 指定したパスが存在し、
              かつディレクトリである場合に True を返します。

            * any: 指定したパスが存在する場合に True を返します。
              パスがファイルであるかディレクトリであるかは問いません。
            """)
    args = parser.parse_args()
    result = lib.test_path(args.path, args.path_type)

    if result:
        print result
        sys.exit(0)
    if not result:
        print result
        sys.exit(1)

if __name__ == "__main__":
    main()
