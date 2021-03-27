# Getting setup

These directions are to, a certain extent, mac specific. Linux machines will be very similar. Windows machines will be close, but will differ here and there.

## 1. Copy stuff from this github repository

A first step is to copy the material from this repository to your own computer.
On a mac, I recommend that you do this in your home directory. (`cd` means "change directory")

```
cd ~  # won't work
git clone https://github.com/bsherin/text_mining_2021.git
```

When you're done, you should have a new folder named `text_mining_2021`.

## 2. Create your python virtual environment

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

On Windows
```
python3 -m venv venv
venv\Scripts\activate.bat # cmd.exe
venv\Scripts\Activate.ps1 # PowerShell
pip install -r requirements.txt
```

## 3. Grab the other files from this page

Go to the top of this page, click on the big green "Code" button and
then click "Download ZIP".

You'll end up with a folder of files. Take the files out of that folder
and drag them into the `text_mining_2021` folder.

## 4. Launch the jupyter notebook or jupyter lab

Steps 1 and 2 above you only have to do once. But step 4 you might need to do
whenever you start working.

Go back into your terminal. First `cd` into the text_mining_2021 folder

```
cd ~/text_mining_2021
```

Then activate the python virtual environment you created above

```
source venv/bin/activate
```

Finally, start the jupyter notebook

```
jupyter notebook
```

Or the jupyter lab

```
jupyter lab
```

# To launch in binder:

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/bsherin/text_mining_2021/main?urlpath=git-pull%3Frepo%3Dhttps%253A%252F%252Fgithub.com%252Fbsherin%252Ftext_mining_content%26urlpath%3Dlab%252Ftree%252Ftext_mining_content%252F%26branch%3Dmain)
