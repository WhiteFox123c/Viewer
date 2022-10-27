Set WshShell = CreateObject("WScript.Shell") 

WshShell.Run ".\venv\Scripts\pythonw.exe main.py", 0, False

Set WshShell = Nothing
