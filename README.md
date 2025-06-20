# Sporty-WEB-test
Sporty - Web test automation challenge
This project is created as a solution for the Sporty test about WEB automation with Selenium in Python.  
It uses https://m.twitch.tv/ app for showcase.


## Test cases:

### Happy path
1. Open https://m.twitch.tv/"
2. Wait page loaded and browse StarCraft II
3. Wait until it is found and click on it
4. Wait until page with search results is open and scroll down twice
5. Click on one of the streams
6. Wait until video starts playing and take screenshot


## Run tests locally
If you have python3 installed:  
`python3 -m venv venv`  
Then activate venv (this works on mac and linux):  
`source venv/bin/activate`  
Then install requirements:  
`pip install -r requirements.txt`  
And start tests with:  
`python3 -m pytest -o log_cli=true -o log_cli_level=INFO -v tests/ --html=report.html --self-contained-html`  
Start report with:   
`open report.html`  

## Run tests through the github action
Click on Actions and just start tests  
Once tests are executed, there will be report.html and screenshots provided to review test results


