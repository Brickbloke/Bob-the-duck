from flask import Flask, request, jsonify, render_template
import os
import google.generativeai as genai

app = Flask(__name__)

# Configure the API key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
)

history = []
#start of new ai gen code might cause trouble status---> unchecked
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.form['question']
    if user_input.lower() == "bye":
        return jsonify({"response": "Let’s race to a greener tomorrow!!! QUACK!! QUACK!!"})

    chat_session = model.start_chat(history=history)
    response = chat_session.send_message(user_input)
    model_response = response.text

    history.append({"role": "user", "parts": [user_input]})
    history.append({"role": "bot", "parts": [model_response]})

    return jsonify({"response": model_response})
#end of new ai gen code have to recheck -----> status unchecked
if __name__ == "__main__":
    app.run(debug=True)
