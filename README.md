# text_mining_content

# Getting setup

These directions are to, a certain extent, mac specific. Linux machines will be very similar. Windows machines will be close, but will differ here and there.

## 1. Copy stuff from this github repository

A first step is to copy the material from this repository to your own computer.
On a mac, I recommend that you do this in your home directory.

```
cd ~
git clone https://github.com/bsherin/LS_mining_course.git
```

If that doesn't seem to work, click on of the links on this page to simply
download the files.

When you're done, you should have a new folder named `LS_mining_course`.

## 2. Create your python virtual environment

Open a Terminal application and `cd` into the `LS_mining_course` folder you just created

```
cd LS_mining_course
```
Then use these commands to create the virtual environment.

```
virtualenv -p /usr/local/bin/python3 venv
source venv/bin/activate
pip install -r requirements.txt
```

## 3. Launch the jupyter notebook or jupyter lab

Steps 1 and 2 above you only have to do once. But step 3 you might need to do
whenever you start working.

First `cd` into the LS_mining_course folder

```
cd ~/LS_mining_course
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
