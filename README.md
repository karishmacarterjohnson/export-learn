# EXPORT-LEARN

A repo for the adies who want pdfs of their learn content
requirements:
```
python3
chrome 
```
# Setup

on your local machine:
`git clone https://github.com/karishmacarterjohnson/export-learn.git` 

change directory to the repo
`cd export-learn`
(varies by clone location)

in here, set up a virtual environment
`python3 -m venv venv`

Once set up activate the environment,
`source venv/bin/activate`

install requirements using
`pip install -r requirements.txt`

create an environment file in the 'export-learn' directory using
`touch .env`

within the .env file, include the following:
```
USERNAME=<yourlearnlogin>
PASSWORD=<yourlearnpassword>
HOME_PAGE=<learnhomepage>
```

HOME_PAGE will be something like: https://learn-2.galvanize.com/cohorts/####

save the .env file

now you can run it!

# Run

WARNING: The actual script will take some time to run (about 10 minutes per module in my experience)
While running, the automated script will launch a chrome browser. this will likely interfere with device usage. It is recommended that the following steps are completed at a time where the script can run uninterrupted

 To begin, run 
`python main.py`

Use command line responses to customize file downloads.

Files will be saved within the `ada-learn` folder.

should you need to restart the process,
delete all subfolders within `ada-learn` and rerun main.py
