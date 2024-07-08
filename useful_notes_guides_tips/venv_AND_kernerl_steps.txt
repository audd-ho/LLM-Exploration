## Virtual Environment, Venv (Ctrl-Shift-V to see formatted preview!)
### Making a virtual environment, venv
```bash
python -m venv the-venv-name
```
- Normally can try to name it "xxx-venv", so whatever it is, then venv extended to it, so later for kernel if also have then just extend to "xxx-venv-kernel"
### Activating the virtual environment, venv
```bash
.the-venv-name/Scripts/activate
```
- After any command, (the-venv-name) will be seen there after the command and results, to indicate which environment the commands are acting in
### Deactivating the virtual environment, venv
```bash
deactivate # can be used from anywhere(any directory, no need to be in original directory where venv was made)
```
### Removing, deletinig virtual environment, venv
- can just delete the venv folder in the current directory with "the-venv-name" as the folder name
### Checking modules and the like (installing, uninstalling)
- No "--user" [and probably(?) "--global"] options for modules since its all in the venv, not user or global based
```bash
pip list # should be empty at the start, at most with pip
pip install xxx # modules, and can arguments with --upgrade or -U, idk if got difference
pip install xxx==yy.yy.yy # yy.yy.yy can specify version
pip install xxx>=yy.yy.yy,<zz.zz.zz # can even do ranges lik
pip uninstall xxx
```
### Saving libraries from pip for future use/portable use(on reinstall) into a txt file
```bash
pip freeze > xxx.txt # the txt file can be named anything like "requirements.txt" for exmaple!
```
- "pip list" will show a list of all libraries installed but this will write all the current libraries to the txt file, which can be used in the future to reinstall all these libraries again!
### Reinstalling saved libraries from a txt file
```bash
pip install -r xxx.txt # the txt file can be named anything like "requirements.txt" for exmaple!, but must follow the txt file within the directory of the venv or wherever its referencing to be accessed!, so must reference the correct txt file that contains the saved libraries in a txt file!
```


## Kernel 
### Installing module for jupyter and kernel
- From within the venv, so need activate it first!
```bash
pip install ipykernel ## pip install --user ipykernel ## can be used for outside venv, to install in user only, not globally on pc
```
### Installing the kernel
```bash
ipython kernel install --user --name=projectname # projectname can be different from venv name, just a name for the kernel, but in jupyter, the kernel name is venv name so idk why?
## the "--user" is so that the kernel folder/file is made in the user level only, not global? since the folder/file is not made at the current directory type! (?)
```
- Normally can try to name it with "xxx-venv-kernel" (so just extend kernel from the venv name above which has venv part of its name already?)
### Using the kernel
- For VScode, the window needs to be refreshed/reloaded for the kernel to be detected in VScode's Jupyter Notebook
- Within VScode, "Ctrl-Shift-P" to open "Command Pallete"
- Search for "Reload Window", and it should be "Developer: Reload Window", click on it (the Ctrl-R command cannot work because in "workbench.action.reloadWindow" in the Keyboard Shortcut, it is for when "isDevelopment" so idk how to work about it, so just manually go for "Command Pallete" then "Reload Window")
- Go to Jupyter Notebook tab/window and top right of it, can click the kernel
- -> Select Another Kernel...
#### THEN
- -> Jupyter Kernel...
- Select the wanted newly installed kernel, and it will be displaying the kernel name, this is different from below which is selecting python environment, venv!
####  OR  
- -> Python Environments...
- Select the wanted newly made venv, but it will be displaying the venv name, and not kernel name, at least for my instance in VScode as of when writing this!
- ^ if the above works then maybe no need to even make a kernel? at least for VScode?, but still need refresh/reload VScode i think?

### Kernel listing
```bash
jupyter kernelspec list # the kernel names and not the venv names will be shown and listed, so will see the "xxx-venv-kernel" name if using the normal naming mentioned above
```
### Removing/Deleting the Kernel
```bash
jupyter kernelspec uninstall unwanted-kernel # the name of unwanted kernel, not venv so will see the "xxx-venv-kernel" name if using the normal naming mentioned above
```


## Credits
### Virtual Environment, venv
- [Docs](https://docs.python.org/3/library/venv.html)
- [2nd Answer here](https://stackoverflow.com/questions/23842713/using-python-3-in-virtualenv)
- [Answer also, read through, and "Install the venv package and create a venv virtual environment"](https://stackoverflow.com/questions/70422866/how-to-create-a-venv-with-a-different-python-version)
- [Good reference as well, and requirements.txt part!](https://www.freecodecamp.org/news/how-to-setup-virtual-environments-in-python/)
- [pip version installation](https://stackoverflow.com/questions/5226311/installing-specific-package-version-with-pip)

### Kernel
- [Good readthrough](https://janakiev.com/blog/jupyter-virtual-envs/)
- [venv setup and kernel installation](https://anbasile.github.io/posts/2017-06-25-jupyter-venv/)
- [Good overall encompassing answer for installation and reminder to restart VScode!](https://stackoverflow.com/questions/58119823/jupyter-notebooks-in-visual-studio-code-does-not-use-the-active-virtual-environm)
- [Kernel removal](https://stackoverflow.com/questions/42635310/remove-the-kernel-on-a-jupyter-notebook)
- [Reload window, attempted workaround, but ended up with just manually Ctrl-Shift-P due to isDevelopment](https://stackoverflow.com/questions/59573038/when-isdevelopment-is-set-in-visual-studio-code)

### Markdown usage!
- [Markdown cheatsheet on github](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#links)
- [Highlight code based on language/type](https://stackoverflow.com/questions/20303826/how-to-highlight-bash-shell-commands-in-markdown)