import os
from flask import Flask, request

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

# == Example Code Below ==

# GET /emoji
# Returns a emojiy face
# Try it:
#   ; curl http://127.0.0.1:5001/emoji
@app.route('/emoji', methods=['GET'])
def get_emoji():
    return ":)"

# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.
from example_routes import apply_example_routes
apply_example_routes(app)

# == End Example Code ==

@app.route('/hello', methods=['GET'])
def hello():
    name = request.args['name'] # The value is 'David'
    return f"Hello {name}!"

@app.route('/goodbye', methods=['POST'])
def goodbye():
    name = request.form['name']
    return f"Goodbye, {name}!"

@app.route('/introduction', methods = ['POST'])
def introduction():
    name1 = request.form['name']
    name2 = request.form['meet']
    return f"Hi {name1}! I'd like to introduce you to {name2}"

@app.route('/submit', methods = ['POST'])
def send_a_message():
    name = request.form['name']
    message = request.form['message']
    return f'Thanks {name}, you sent this message: "{message}"'

@app.route('/wave', methods = ['GET'])
def wave_at_person():
    name = request.args['name']
    return f"I am waving at {name}"

@app.route('/count_vowels', methods = ['POST'])
def count_vowels_in_string():
    text = request.form['text']
    vowel_count = 0
    for char in text:
        if char in 'aeiou':
            vowel_count += 1
    return f'There are {vowel_count} vowels in "{text}"'

@app.route('/sort-names', methods = ['POST'])
def sort_names_in_alphabetical_order():
    names = request.form['names']
    names_in_list = names.split(',')
    names_in_list.sort()
    return ','.join(names_in_list)

@app.route('/add_names', methods = ['GET'])
def add_names_to_predefined_names():
    predefined_names = ['Julia', 'Alice', 'Karim',]
    new_names = request.args['names']
    predefined_names.extend(new_names.split(','))
    return (', '.join(predefined_names)).title()



# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))

