@echo off

set uiFilename=%1
set uiFilepath=gui\ui
set pyFilepath=gui\templates
set pyFilePreffix=Ui

start pyuic5 %uiFilepath%\%uiFilename%.ui -o %pyFilepath%\%pyFilePreffix%_%uiFilename%.py
