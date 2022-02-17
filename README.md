# Framework Python Selenium with Pytest and Allure reports


#Installation Steps:
- Clone this repo
  - Go to https://github.com/zippote/frameworkPython
  - Click Code
  - Select HTTPS and copy the following url https://github.com/zippote/frameworkPython.git

- Steps on your local:
  - Create a destination folder in your local >> ie: myFolderExample in the C drive
  - Open the cmd and move to that folder >> cd C:\myFolderExample
  - Type the following command: git clone https://github.com/zippote/frameworkPython.git
  - Hit enter and wait until the process is completed
  - Navigate to the project root folder cmd or IDE terminal
  - create new virtual env by running `py -m venv venvs`
  - venvs will be created under the root directory \venvs\
  - to activate venv run `.\venv\Scripts\activate`
  - run `pip install -r requirements.txt`


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
