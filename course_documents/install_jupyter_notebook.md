# Installing Jupyter Lab

This can be an iffy process, but you should only have to do it once.

These directions are to, a certain extent, mac specific. I'll try to point out
Windows differences as best as I can.

### 1. Copy stuff from this github repository

A first step is to copy the material from this repository to your own computer.
On a mac, I recommend that you do this in your home directory. (`cd` means "change directory")

```
cd ~  # won't work
git clone https://github.com/bsherin/text_mining_2021.git
```

When you're done, you should have a new folder named `text_mining_2021`.

### 2. Create your python virtual environment

Open a Terminal application and `cd` into the `text_mining_2021` folder you just created

```
cd text_mining_2021
```
Then use these commands to create the virtual environment.

```
virtualenv -p /usr/local/bin/python3 venv
source venv/bin/activate
pip install -r requirements.txt
```

On Windows:
```
python3 -m venv venv
# just one of the next two lines
venv\Scripts\activate.bat # if you're using cmd.exe
venv\Scripts\Activate.ps1 # if you're using PowerShell
# then this
pip install -r requirements.txt
```

# Grab weekly files

Each week there will be some new files for you to add to your environment.
Generally these will be some new notebooks or data corpora.
This is just a matter of dragging and dropping.

Go to the top of this page, click on the big green "Code" button and
then click "Download ZIP".

You'll end up with a folder of files. Take the files out of that folder
and drag them into the `text_mining_2021` folder.

# Launch the jupyter notebook or jupyter lab

Go back into your terminal. First `cd` into the text_mining_2021 folder

```
cd ~/text_mining_2021
```

Then activate the python virtual environment you created above

```
source venv/bin/activate  # or the Windows version from above
```

Finally, start the jupyter notebook

```
jupyter notebook
```

Or the jupyter lab

```
jupyter lab
```

A browser window should magically open with the jupyter lab or notebook.
You need to keep the terminal window open.

If the jupyter lab has already been started on your machine and you closed
the browser window you might be able get to it again
by entering `http://localhost:8888/lab` in your browser.
