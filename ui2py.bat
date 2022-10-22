@echo off

set uiFilename=%1
set uiFilepath=gui\ui
set pyFilepath=gui\templates

start pyuic5 %uiFilepath%\%uiFilename%.ui -o %pyFilepath%\Ui_%uiFilename%.py
