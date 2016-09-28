#!/usr/bin/python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

try:
    long_description = open("README.md").read()
except Exception:
    long_description = ""

setup(
    name="python-powershell",
    version="1.2",
    description="PowerShell Commands for Python.",
    author="Jhonny Bravo",
    author_email="sanfranceshika5@gmail.com",
    url="https://github.com/JhonnyBravo/python-powershell.git",
    packages=find_packages(),
    install_requires=[],
    dependency_links=[],
    entry_points={
        "console_scripts": [
            "add_content=ps_content.bin.add_content:main",
            "clear_content=ps_content.bin.clear_content:main",
            "get_content=ps_content.bin.get_content:main",
            "set_content=ps_content.bin.set_content:main",
            "copy_item=ps_item.bin.copy_item:main",
            "get_child_item=ps_item.bin.get_child_item:main",
            "move_item=ps_item.bin.move_item:main",
            "new_item=ps_item.bin.new_item:main",
            "remove_item=ps_item.bin.remove_item:main",
            "split_path=ps_path.bin.split_path:main",
            "test_path=ps_path.bin.test_path:main",
            "select_string=ps_string.bin.select_string:main",
            "invoke_command=ps_command.bin.invoke_command:main"
        ]
    },
    long_description=long_description,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
    ]
)
