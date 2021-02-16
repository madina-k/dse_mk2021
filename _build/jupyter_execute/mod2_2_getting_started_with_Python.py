# Getting started with Python (10 min)
## Intro to Python

<div class="alert alert-success">
<a href="https://www.python.org/" class="alert-link">Python</a> is a popular programming language for data science.
</div>

This tutorial uses Python and assumes that you have at least some familiarity with it.

Python is one of the most popular programming languages for a number of reasons:
- It’s open-source
- It has a large standard library and a massive (and growing!) ecosystem of packages (collections of code), including those used for scientific computing
- It’s user-friendly
- It has a large and active online community for knowledge-sharing and trouble-shooting when you get stuck
- It’s a general-purpose language...this is helpful for data science work, which often covers a wide range of tasks

<div class="alert alert-success">
If you are completely new to programming, you’ll first want to get started with <a href="https://wiki.python.org/moin/BeginnersGuide/NonProgrammers" class="alert-link"> this Beginner's Guide for Non-Programmers.</a>
</div>

<div class="alert alert-success">
If you are a programmer who is new to Python, <a href="https://wiki.python.org/moin/BeginnersGuide/Programmers" class="alert-link">this Beginner's Guide for Programmers</a> may help.
</div>

<div class="alert alert-success">
<a href="https://github.com/openlists/PythonResources" class="alert-link">Here’s another large list of resources for Python</a> assembled by that community we talked about.
</div>

There are many ways to install and manage Python, in fact most Linux and UNIX-based computers already have it as a system install.

This tutorial requires Python 3.7 or greater.

**We highly recommend you install Python with `pyenv` and use a virtual environment for this tutorial.** Even if you already have Python on your computer, using `pyenv` and a virtual environment will ensure you can install and manage the packages we’ll be using easily and it won’t interfere with the Python installation you already have.

## Package management
We mentioned that large and growing ecosystem of Python packages, which really makes this a powerful language. Thanks to these open-source packages, many tasks we’ll conduct in this tutorial will use code already written for the task, so you don’t have to write out the source code from scratch.

However, these packages often depend on each other in various ways and are updated frequently. If you didn’t have a way to manage packages and dependencies, things might break and it becomes a frustrating experience. Fortunately,there are package managers available for this.

### pip

If you’ve used Python, you’re familiar with pip.

<div class="alert alert-success">
    <b>pip</b> is the recommended utility for installing Python packages contained in the Python Package Index (PyPI), a repository containing packages people have written in Python.
</div>

## Installing Python with pyenv

<div class="alert alert-success">
    <b>pyenv</b> is a Python version manager. It allows you to manage multiple versions of Python.
</div>

### Installing for UNIX-based systems (MacOS or Linux)
Use this package and installation instructions:
https://github.com/pyenv/pyenv

<div class="alert alert-success">
    <a href="https://brew.sh/">Homebrew</a> is a software package manager for MacOS and Linux and is incredibly useful for managing open source software (not just Python!). You can use Homebrew to install `pyenv` (as well as Python and any number of libraries). 
</div>

### Installing for Windows
Use this package and installation instructions:
https://github.com/pyenv-win/pyenv-win

### Python 3.7
The `pyenv` instructions should guide you to installing it and a (or several) Python versions. Don't worry if you get stuck, this can be tricky for beginners, but understanding the software you have "under the hood" is a big part of programming for data science. You may not have to build these tools, but it helps to understand them!

If you have successfully installed `pyenv`, then when you enter the prompt in your Command Line Interface (terminal), you'll see the location of your Python version within the `.pyenv` directory. 

```
<CLI prompt>$ which python
<your root path here>/.pyenv/shims/python
```

You can also see the version of Python you're using:
```
<CLI prompt>$ python -V
Python 3.8.6
```
If you see this, you know you have Python version X (whatever the readout says) on your system.

<div class="alert alert-success">
    <a href="https://realpython.com/intro-to-pyenv/">This</a> is an excellent tutorial for installing and understanding pyenv.
</div>



## Virtual environments (optional, but highly recommended)
As you dig into programming, you will realize different projects need different versions and configurations of software, contained within an “environment.” It makes life a lot easier to create specific “virtual environments” on your computer that contain all the code you need for a project without interfering with other projects. 

You don’t need to set up a virtual environment for this tutorial. But it's quite highly recommended, especially if you are working on multiple projects. 

<div class="alert alert-success">
    <a href="https://realpython.com/intro-to-pyenv/">This</a> tutorial mentioned above about pyenv also describes setting up Python virtual environments.
</div>

### Pyenv virtual env example

If you followed the instructions of that tutorial to install `pyenv` and the `pyenv virtualenv` command then you can set up a virtual environment for this project.

For example, open a terminal (CLI) window and navigate to the location you want to have this tutorial project on your computer, perhaps in a new folder (e.g. /home/<username>/projects/onltutorial, etc.)
    
Then enter the following, replacting "3.8.2" with your Python version as installed with `pyenv` and "onl" with whatever you name your environment:
```
<prompt>$ pyenv virtualenv 3.8.2 onl
```

Now you can activate your env:
```
<prompt>$ pyenv activate onl
```
    
And you can deactivate an active environment:
```
<prompt>$ pyenv deactivate
``` 

When you're in your active environment, you can see that you are using the Python package (and libraries) within your environment. Within your environment, type `which python` and you will see it's located in your virtual env.

From a notebook (like this), you can also enter CLI prompts using the bang symbol, like this:

!which python

### Dependencies
As noted, we'll be using Python open source libraries (which will be "dependencies" that we need to run our analysis and code). There are different ways to manage dependencies and it is an important part of programming with open source programs (anything, really). A simple way to track your dependencies is with a `requirements.txt` file.

We have such a file for this Github repo, but for transparency and simplicity sake, we will note every library (dependency) you need to install for each notebook (just know that you only have to install each library to your environment once).

### IMPORTANT!
In order to use this notebook or any notebook, you'll need the `jupyter` library installed. If you're using a `requirements.txt` file, be sure to add it. Or you can install directly in your command line.

When in your active environment, use `pip`:
```
<prompt>$ pip install jupyter
```

### Development environments

There are many ways to write, edit and execute Python scripts. Programmers will often use an Integrated Development Environment (IDE), such as PyCharm, which is a popular IDE for Python. There are a lot of advantages to using IDEs, especially if you’re building more complicated software applications; however, for this tutorial, we’ll be executing fairly simple routines and can do this from Jupyter notebooks. In fact, this tutorial is contained in Jupyter notebooks!