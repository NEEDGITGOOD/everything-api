from flask import Flask, request
import os
import openai
import json

# Initialize Flask app
app = Flask(__name__)

# Load OpenAI API key from a file
with open('./openai.key') as f:
    openai.api_key = f.read().strip()

BASE_PROMPT = """Create a response document with content that matches the following URL path: 
    `{{URL_PATH}}`

The first line is the Content-Type of the response.
The following lines are the returned data.
In case of an HTML response, add relative href links to related topics.
{{OPTIONAL_DATA}}

Content-Type:
"""

@app.route("/", methods=['POST', 'GET'])
@app.route("/<path:path>", methods=['POST', 'GET'])
def catch_all(path=""):
    # Prepare the prompt with the actual URL path and any optional data
    if request.method == 'POST' and request.form:
        optional_data = f"form data: {json.dumps(request.form)}"
    else:
        optional_data = ""
    
    prompt = BASE_PROMPT.replace("{{URL_PATH}}", path).replace("{{OPTIONAL_DATA}}", optional_data)

    # Make API call to OpenAI
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Set Model
        messages=[
            {"role": "system", "content": prompt}
        ]
    )

    # Correctly access the AI-generated data from the response
    # Ensure 'ai_data' contains a string of the AI-generated response
    if 'choices' in response and len(response['choices']) > 0:
        ai_data = response['choices'][0]['message']['content'] if 'content' in response['choices'][0]['message'] else ""
    else:
        ai_data = ""

    # Process ai_data assuming it is correctly retrieved as a string
    content_type = "text/plain"  # Default content type
    response_data = ai_data
    if ai_data:
        lines = ai_data.splitlines()
        if lines:
            content_type = lines[0]
            response_data = "\n".join(lines[1:])

    return response_data, 200, {'Content-Type': content_type}

# This line is for local development and debugging
if __name__ == "__main__":
    app.run(debug=True)
