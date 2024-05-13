from flask import Flask, render_template, request
import openai
import config

openai.api_key = config.API_KEY

app = Flask(__name__)

@app.route("/")
def index():
    #return "Hello World"
    return render_template('index.html')

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
        {
            "role": "system",
            "content": "You are a customer service assistant designed to provide helpful, accurate, and friendly support. Answer the users' questions, assist with issues, offer solutions or suggestions, and ensure customer satisfaction. Be polite, professional, and adhere to the company's policies."
        },
	    {
		    "role": "user",
		    "content": userText
	    }
	    ],
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=1,
    )
    answer = response.choices[0].message.content
    return str(answer)

"""
def get_bot_response():
    userText = request.args.get('msg')
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Adjusted to use a more advanced model for improved performance.
        messages=[
            {
                "role": "system",
                "content": "You are a customer service assistant designed to provide helpful, accurate, and friendly support. Answer the users' questions, assist with issues, offer solutions or suggestions, and ensure customer satisfaction. Be polite, professional, and adhere to the company's policies."
            },
            {
                "role": "user",
                "content": userText
            }
        ],
        max_tokens=1024,
        temperature=0.7,  # Adjusted for more predictable, concise responses.
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None  # Consider setting a stop sequence if there's a natural end to responses.
    )
    answer = response.choices[0].message['content']  # Adjusted to match the correct attribute access.
    return str(answer)"""



if __name__ == "__main__":
    app.run()