# lnk_generator
These are some small scripts I made as part of larger research. They facilitate automating the generation of Windows shortcut files from a Linux machine.

Simply edit a few variables in Template_generator.ps1 and then run on a windows machine to produce a template.lnk file (or use the one I have included).

Copy template.lnk to your Linux machine, edit genlnk.py with the command you want to stuff into your .lnk file, and then call genlnk.py

Usage: Python3 genlnk.py template.lnk

You can take a peek under the hood of template.lnk as well as your generated clickme.lnk by using the xxd command:

xxd clickme.lnk
