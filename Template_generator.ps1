#Short powershell script to generate a template .lnk file for use with genlnk.py
#source: https://stackoverflow.com/questions/31815286/creating-quoted-path-for-shortcut-with-arguments-in-powershell

#Modify line 9 with the location you want to output your template file
#Modify line 10 with the icon you want to use for your .lnk. NOTE: Consider whether whatever icon you select exists on the machine this is going to run on!
#Leave line 11 as is! Unless you want to call something besides powershell (or obfuscate the call to powershell), in which case you will need to modify genlnk.py as well.
#Leave line 12 as is! This will be changed by genlnk.py

$WshShell = New-Object -comObject WScript.Shell
$Shortcut = $WshShell.CreateShortcut("c:\users\ieuser\desktop\template.lnk")
$Shortcut.IconLocation = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
$Shortcut.TargetPath = 'C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe'
#Use ONE of the Shortcut.Arguments lines; if using '-w 1 -c...' to make powershell hidden, make sure you change genlnk.py as well!
$Shortcut.Arguments = '-c ""'
#$Shortcut.Arguments = '-w 1 -c ""' 
$Shortcut.WorkingDirectory = '%CD%'
$Shortcut.Save()
