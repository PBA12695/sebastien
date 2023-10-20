# Photo random picker GUI application

#First, you need to autogenerate resource_rc.py
pyrcc5 resource.qrc -o resource_rc.py

#Then, you need to generate the exe file with command
pyinstaller --onefile main.py


