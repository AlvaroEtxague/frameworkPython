# Framework Python Selenium with Pytest and Allure reports


#Installation Steps:
## From Github
- Clone this repo
  - Go to https://github.com/zippote/frameworkPython
  - Click Code
  - Select HTTPS and copy the following url https://github.com/zippote/frameworkPython.git

- Steps on your local:
  - Create a destination folder in your local >> ie: myFolderExample in the C drive
  - Open cmd and move to that folder >> cd C:\myFolderExample
  - Type the following command: git clone https://github.com/zippote/frameworkPython.git
  - Hit enter and wait until the process is completed
  - Navigate to the project root folder cmd or IDE terminal
  - Create new virtual env by running `py -m venv venv`
  - venv will be created under the root directory \venv\
  - To activate venv run `venv\Scripts\activate`
  - Run `pip install -r requirements.txt`

## From ZIP
  - Go to https://github.com/zippote/frameworkPython
  - Click Code
  - Select download zip
  - Extract the file to a folder of your choice, for example: C:\myFolder\automationUIFramework
  - Open the repo with Pycharm or VS code (or any other IDE)

- Steps on your local:
  - Navigate to the project root folder cmd or IDE terminal, for example: C:\myFolder\automationUIFramework
  - Create a new virtual env by running `py -m venv venv`
  - venv will be created under the root directory \venv\
  - To activate venv run `venv\Scripts\activate`
  - Run `pip install -r requirements.txt`


#RUNNING TESTS WITH PYTEST
##Run tests in parallel
`pytest -v -s -nauto`

##Run tests individually
`pytest -v -s`

##Run tests individually and add them to report
`pytest -v -s --alluredir=reports`

##Run tests in parallel and add them to report
`pytest -v -s -nauto --alluredir=reports`

##To view allure report
1. Open cmd
2. `cd C:\path-to-repo-root\`
3. `allure serve reports`
