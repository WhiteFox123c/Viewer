@echo off

set uiFilename=$1
set uiFilepath=GUI/designer
set pyFilepath=GUI
set pyFilePreffix=Ui

start pyuic6 %uiFilepath%/%uiFilename%.ui -o %pyFilepath%/%pyFilePreffix%_%uiFilename%.py
