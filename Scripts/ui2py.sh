#!/bin/bash

uiFilename=$1
uiFilepath=GUI/designer
pyFilepath=GUI
pyFilePreffix=Ui

pyuic6 ${uiFilepath}/${uiFilename}.ui -o ${pyFilepath}/${pyFilePreffix}_${uiFilename}.py
