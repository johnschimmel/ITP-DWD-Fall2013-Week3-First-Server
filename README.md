## Getting a simple server running on Heroku


### Quick start with Heroku:
* Sign up for Heroku [https://api.heroku.com/signup](https://api.heroku.com/signup)
* Download and install Heroku Toolbelt [https://toolbelt.heroku.com/](https://toolbelt.heroku.com/)

-----------

### Getting the web server to run locally on your computer
Download example web server and Heroku files (get the ZIP) [https://github.com/johnschimmel/ITP-DWD-Fall2013-Week3-First-Server](https://github.com/johnschimmel/ITP-DWD-Fall2013-Week3-First-Server)


#### Set up local code environment with Virtualenv

* Put the Heroku simple server code in a directory 
* With Terminal, navigate to the code directory

Python can help organize your code modules, keeping them separate from existing Python modules with Virtualenv (virtual environment). We installed Virtualenv on week 1 with the command,

	easy_install virtualenv

We also install PIP

	easy_install pip

Virtualenv will organize all your modules and even download new requested packages and updates. When activated, Virtualenv will supply the modules needed for an application.

#### Create a virtual environment

Inside your code directory, run the command

	virtualenv venv

We are telling Virtualenv to create a new directory called **venv** to manage our packages.


#### Turn on the Virtualenv

Once created we need to turn on the virtual environment, telling the computer to use the venv as a source for all packages.

	. venv/bin/activate

The '.' is an execution command, saying "Hey, run the 'activate' program inside /venv/bin directory".

#### Install Requirements with PIP

There is a file **requirements.txt** that lists all the packages we need to run the web server. Earlier we imported Flask manually but now we will import Flask via PIP's alternative method.

requirements.txt

	Flask==0.10

Currently there is only one package requested, Flask version 0.9.

To install the required packages run the command, 

	pip install -r requirements.txt

PIP installs all requested requirements and it also downloads all of their dependencies (werkzeug and jinja2).


#### Run web server locally

With all the requirements installed let's turn on the server,

	python app.py

Stop the server with **CTRL+C** inside the Terminal window.


Alternatively, we can use a new command to turn on the server. The Heroku Toolbelt installed Foreman, a helper utility for running applications. Run the command,

	foreman start


Foreman is the command we will be using for the rest of the semester. Foreman uses the file **Procfile** to know what to turn on. There is a single line inside **Procfile**,

	web: python app.py

The **Procfile** will be pushed to Heroku, it tells Heroku where are main web server script is located, app.py. It also declares we're using Python.



----------

### Getting Going with GIT

In Terminal, navigate to your code folder. Let's initialize this folder as a Git repository. This will enable us to keep track of all code changes and allow us to eventually PUSH code to Heroku.

Before we set up the Git repo, let's look inside the .gitignore file. This file will tell Git to ignore certain files and folders. These could be files that are not required for your code history or they might include private and sensitive information like passwords.

#### .gitignore

	.DS_Store
	venv
	*.pyc

We will ignore the **venv** folder (coming up soon) and any compiled Python files **(*.pyc)**. Also OS X likes to create a **.DS_Store** file to manange its directories, let's ignore this too.

#### Initialize directory as GIT repository

You only need to do this once per directory. Inside the code directory using Terminal run the command

	git init

This creates a hidden **.git** directory to manage all changes with your code


#### Adding files to GIT

First time you intialize and for each new file you add to your repository you must add the file to the Git repo. Run this command

	git add .

The '**.**' is a wildcard and adds all files and folders (excluding those listed inside the .gitignore file).

#### Commit your code

To create a snapshot in time of your code, run the following command,

	git commit -am "This is my update, I added some files."


----------

### Push to Heroku

With your code committed you're ready to use Heroku

#### Verify you are logged into Heroku

	heroku login

Log in with your email and password used when registering at [https://api.heroku.com/signup](https://api.heroku.com/signup)


#### Create a new Heroku app

	heroku create

Heroku will respond with a crazy looking domain name. Heroku also added a new GIT remote path to you Heroku repository. Look at your GIT remote paths run the command, 

	git remote -v

#### Push your code to Heroku

Ready? Deploy your new server on Heroku by **push**ing your code to Heroku. This is uploading all code and commit history to Heroku.

	git push heroku master

Heroku will install all Python dependencies (requirements.txt) and turn on your web server using the Procfile provided.

#### Open and view your server

	heroku open