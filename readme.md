## Sample Flask Web Application 

This is a very simple Python Flask application used for basic testing of public cloud services. Some deployment options are described in this blog post:  https://ws-dl.blogspot.com/2023/07/2023-07-07-deploying-aws-serverless.html

## To run locally:

1. Install dependencies
  * pip install -r requirements.txt 
2. Start application
  * python .\application.py 
3. View application in a web browser
  * http://127.0.0.1:5000

## To create a docker image:

1. Run the docker build command
  * docker build -t sample-app .
