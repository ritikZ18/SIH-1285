from flask import Flask, render_template, request
import openai


app = Flask(__name__)

# Set up OpenAI API credentials
openai.api_key = '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'


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
       
    ]
   
    )
    if completion.choices[0].message!=None:
        return completion.choices[0].message

    else :
        return 'Failed to Generate response!'
    


    

if __name__=='__main__':
    app.run()

#how to add this cod ein above code.  


#  {
#   "object": "list",
#   "data": [
#     {
#       "object": "fine_tuning.job.event",
#       "id": "ft-event-ddTJfwuMVpfLXseO0Am0Gqjm",
#       "created_at": 1692407401,
#       "level": "info",
#       "message": "Fine tuning job successfully completed",
#       "data": null,
#       "type": "message"
#     },
#     {
#       "object": "fine_tuning.job.event",
#       "id": "ft-event-tyiGuB72evQncpH87xe505Sv",
#       "created_at": 1692407400,
#       "level": "info",
#       "message": "New fine-tuned model created: ft:gpt-3.5-turbo:openai::7p4lURel",
#       "data": null,
#       "type": "message"
#     }
#   ],
#   "has_more": true 
# }