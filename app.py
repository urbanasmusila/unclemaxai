import os
from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

OPENAI_API_KEY = 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
openai.api_key = OPENAI_API_KEY

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form.get('input')

    try:
        gpt_response = openai.Completion.create(
            engine="text-davinci-004",  # Replace this with the GPT-4 engine ID when available
            prompt=f"UncleMaxAI chatbot: {user_input}",
            temperature=0.7,
            max_tokens=100,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )

        chatbot_response = gpt_response.choices[0].text.strip()
        return jsonify(response=chatbot_response)

    except Exception as e:
        return jsonify(error=str(e))

if __name__ == '__main__':
    app.run(debug=True)
