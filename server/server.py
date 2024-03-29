from flask import Flask, request
from flask_cors import cross_origin
import openai

openai.api_key = "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"

app = Flask(__name__)

@app.route("/ask")
@cross_origin()

def ask():
    completions = openai.Completion.create(
        engine="text-davinci-003", 
        prompt=request.args['q'], 
        max_tokens=1024, 
        n=1,
        stop=None,
        temperature=0.7)

    message = completions.choices[0].text
    return {"answers" : message}



if __name__ == "__main__":
    app.run(debug=True)
    

# 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