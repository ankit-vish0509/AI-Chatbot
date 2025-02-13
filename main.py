from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

app = Flask(__name__)
genai.configure(api_key="AIzaSyBjTm3Jm8_GRQdkuB8rOKHoPbFzZUAGlVY")  # Replace with your actual key
# model = genai.GenerativeModel("gemini-1.5-flash")
model = genai.GenerativeModel("gemini-2.0-flash-exp")

@app.route("/get", methods=["POST"])  # This route is specifically for AJAX requests
def get_bot_response():
    user_message = request.form.get("msg")  # Get the message from the AJAX request
    if user_message:
        try:
            prompt = user_message
            response = model.generate_content(prompt)
            bot_response = response.text
            return jsonify(bot_response)  # Return the response as JSON
        except Exception as e:
            return jsonify(f"An error occurred: {e}")  # Return error as JSON
    return jsonify("No message received")  # Handle cases with no message


@app.route("/", methods=["GET"])  # This route renders the main page
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True,port=5001)