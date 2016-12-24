# coding: utf8
import os
import sys
import re


def select_string(input_list, pattern, not_match=False):
    """
    input_list から pattern に合致する文字列を含む行を取得します。

    :param list input_list: 文字列を収めた配列。
    :param str pattern: pattern に合致する文字列を含む行を取得します。
    :param bool not_match: True を指定した場合は
        pattern に合致しない行を取得します。
    :return: 文字列の配列。
    :rtype: list
    """
    result = []

    for line in input_list:
        if not_match:
            if not re.search(pattern, line):
                result.append(line.rstrip("\r\n"))
        else:
            if re.search(pattern, line):
                result.append(line.rstrip("\r\n"))

    return result
