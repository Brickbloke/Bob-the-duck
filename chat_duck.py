import os
import google.generativeai as genai

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

print("Quakers: what would you like to know today? Quack!!!")
while True:
    user_input = input("You: ")
    
    if user_input.lower() == "bye":
        print("Let’s race to a greener tomorrow!!! QUACK!! QUACK!!")
        break

    chat_session = model.start_chat(
        history=history
    )

    response = chat_session.send_message(user_input)
    model_response = response.text

    print(model_response)
    print()

    history.append({"role": "user", "parts": [user_input]})
    history.append({"role": "bot", "parts": [model_response]})

response = chat_session.send_message("INSERT_INPUT_HERE")

print(response.text)
