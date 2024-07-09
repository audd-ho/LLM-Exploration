import sys
print(sys.executable)

# "which python" also works in git bash!

##
'''
can select default(for newly spawned terminals and etc) and for terminals within VScode with
-> "Ctrl-Shift-P" for Command Palette
-> Select "Python: Select Interpreter"
-> Choose the one you want, generally is use global default one!
-> will only change WITHIN a terminal when you activate and use a venv, then the "python" within that terminal will correspond to the venv's python executable

<- Python on the left side bar, shows the "Workspace Environments"
<- below also has "Global Environments", which has the "Global" and "Venv", virtual environment one!
'''

## this python is referring to the one called from the command line in terminal, in VScode's terminals
## so when do "python xxx.py", in the VScode terminal, it will be based off this python of the terminal
## within VScode, this also overrides the PATH where the globally installed Python is at the top of PATH!!

## venv can override this, but for that specific terminal where it is activated only!!!, even if spawn more terminals afterwards or kill the venv terminal without deactivating, its all local to that terminal, so others are based off the default env and default python executable and its/that env!