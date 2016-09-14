# coding: utf-8
"""
item command
------------

Clear-Item
Clear-ItemProperty
作成済み: Copy-Item
Copy-ItemProperty
Get-ChildItem
Get-ControlPanelItem
Get-Item
Get-ItemProperty
Get-ItemPropertyValue
Invoke-Item
Move-Item
Move-ItemProperty
作成済み: New-Item
New-ItemProperty
作成済み: Remove-Item
Remove-ItemProperty
Rename-Item
Rename-ItemProperty
Set-Item
Set-ItemProperty
Show-ControlPanelItem
Get-TestDriveItem
Get-DAEntryPointTableItem
New-DAEntryPointTableItem
Remove-DAEntryPointTableItem
Rename-DAEntryPointTableItem
Reset-DAEntryPointTableItem
Set-DAEntryPointTableItem
Start-WebItem
Stop-WebItem
Restart-WebItem
Get-WebItemState
"""
import os
import sys
import shutil


def new_item(path, item_type, value=""):
    if os.path.exists(path):
        print path + " は既に存在します。"
        sys.exit(1)

    if item_type == "file":
        if value:
            with open(path, 'wt') as file:
                file.write(value + "\n")
        else:
            open(path, "wb").close()
    elif item_type == "directory":
        os.makedirs(path)

    print path + " を作成しました。"
    sys.exit(0)


def remove_item(path, recurse=False):
    if not os.path.exists(path):
        print path + " は存在しません。"
        sys.exit(1)

    if os.path.isfile(path):
        os.remove(path)
    elif os.path.isdir(path) and recurse:
        shutil.rmtree(path)
    elif os.path.isdir(path) and not recurse:
        os.rmdir(path)

    print path + " を削除しました。"
    sys.exit(0)


def copy_item(path, destination):
    if not os.path.exists(path):
        print path + " は存在しません。"
        sys.exit(1)

    if os.path.isfile(path):
        shutil.copy(path, destination)
    elif os.path.isdir(path):
        shutil.copytree(path, destination)

    print path + " を " + destination + " へコピーしました。"
    sys.exit(0)
