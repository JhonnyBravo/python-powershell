# coding: utf8
import os
import sys
import re


def select_string(input_list, pattern, not_match=False):
    result = []

    for line in input_list:
        if not_match:
            if not re.search(pattern, line):
                result.append(line.rstrip("\r\n"))
        else:
            if re.search(pattern, line):
                result.append(line.rstrip("\r\n"))

    return result
