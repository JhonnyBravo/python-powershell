# coding: utf-8
"""
item command
------------

Clear-Item
Clear-ItemProperty
Copy-Item
Copy-ItemProperty
Get-ChildItem
Get-ControlPanelItem
Get-Item
Get-ItemProperty
Get-ItemPropertyValue
Invoke-Item
Move-Item
Move-ItemProperty
New-Item
New-ItemProperty
Remove-Item
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
