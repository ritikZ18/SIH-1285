from flask import Flask, render_template, request, jsonify  # Import jsonify
import openai

app = Flask(__name__)

# Set up OpenAI API credentials
openai.api_key = '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'

# ... (other routes and code) ...

# Define the default route to return the index.html file
@app.route("/")
def index():
    return render_template("index.html")

# Define the /api route to handle POST requests
@app.route("/api", methods=["POST"])
def api():
    # Get the message from the POST request
    message = request.json.get("message")
    # Send the message to OpenAI's API and receive the response
    
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": message},
            "temperature": 0.7,
            "n_epochs": 5,  # Fix the typo here
        ]
    )
    if completion.choices[0].message is not None:
        return completion.choices[0].message
    else:
        return 'Failed to Generate response!'

# Define a new route to handle the JSON data
@app.route("/fine-tuning-events", methods=["GET"])
def fine_tuning_events():
    # Define the JSON data
    fine_tuning_data = {
        "object": "list",
        "data": [
            {
                "object": "fine_tuning.job.event",
                "id": "ft-event-ddTJfwuMVpfLXseO0Am0Gqjm",
                "created_at": 1692407401,
                "level": "info",
                "message": "Fine tuning job successfully completed",
                "data": None,
                "type": "message"
            },
            {
                "object": "fine_tuning.job.event",
                "id": "ft-event-tyiGuB72evQncpH87xe505Sv",
                "created_at": 1692407400,
                "level": "info",
                "message": "New fine-tuned model created: ft:gpt-3.5-turbo:openai::7p4lURel",
                "data": None,
                "type": "message"
            }
        ],
        "has_more": True
    }
    
    # Return the JSON data as a response
    return jsonify(fine_tuning_data)

if __name__ == '__main__':
    app.run()
