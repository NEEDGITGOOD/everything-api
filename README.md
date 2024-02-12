# everything-api

This application, developed with Flask, leverages the OpenAI GPT-4 API to create dynamic content tailored to the URL path specified in the request. I.e -> /html

## Usage/Installation 

1. Clone this repository:
````bash
git clone https://github.com/NEEDGITGOOD/everything-api
````
2. Create an OpenAI Key File called `openai.key` in the Root Directory.

3. Create a Virtual Python Environment:

For Windows, use:
````bash
.\.venv\Scripts\activate
````

4. Install the required packages:
````bash
pip install -r requirements.txt
````

5. Set the FLASK_APP Environmentalvariable: (Powershell)
````bash
$env:FLASK_APP = "main"
````

6. Now run the Flask application:
````bash
flask run
````
Just go on localhost:500/randomdirectory

