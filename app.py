from flask import render_template ,url_for,flash,redirect,request
from flask import Flask, render_template_string, request
from output import output
import os
import openai
import os
import sys
import random
import numpy as np
import pickle
import json
from gtts import gTTS  
from playsound import playsound
import pygame
from flask import Flask, render_template, request
#from flask_ngrok import run_with_ngrok
import nltk
from keras.models import load_model
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
from flask import Flask, render_template_string, request
from musicplayy import myappplay

app = Flask(__name__)

@app.route('/',methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/about',methods=['GET'])
def about():
    return render_template('about.html')

@app.route('/',methods=['POST','GET'])
def predict():
    imagefile=request.files['imagefile']
    image_path=os.path.join(app.root_path,'static\\images\\demo_imgs',imagefile.filename)
    imagefile.save(image_path)
    img="/images/demo_imgs/"+imagefile.filename
    title,ingredients,recipe = output(image_path)
    return render_template('predict.html',title=title,ingredients=ingredients,recipe=recipe,img=img)

@app.route('/<samplefoodname>')
def predictsample(samplefoodname):
    imagefile=os.path.join(app.root_path,'static\\images',str(samplefoodname)+".jpg")
    img="/images/"+str(samplefoodname)+".jpg"
    title,ingredients,recipe = output(imagefile)
    return render_template('predict.html',title=title,ingredients=ingredients,recipe=recipe,img=img)


openai.api_key = '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'

def generate_tutorial(components):

  response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{
      "role": "system",
      "content": "You are a helpful assistant"
    }, {
      "role":
      "user",
      "content":
      f"Suggest a recipe using the items listed as available. Make sure you have a nice name for this recipe listed at the start. Also, include a funny version of the name of the recipe on the following line. Then share the recipe in a step-by-step manner. In the end, write a fun fact about the recipe or any of the items used in the recipe. Here are the items available: {components}, Haldi, Chilly Powder, Tomato Ketchup, Water, Garam Masala, Oil"
    }])

  return response['choices'][0]['message']['content']


def generate_tutorial(components):

  response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{
      "role": "system",
      "content": "You are a helpful assistant"
    }, {
      "role":
      "user",
      "content":
      f"Suggest a recipe using the items listed as available. Make sure you have a nice name for this recipe listed at the start. Also, include a funny version of the name of the recipe on the following line. Then share the recipe in a step-by-step manner. In the end, write a fun fact about the recipe or any of the items used in the recipe. Here are the items available: {components}, Haldi, Chilly Powder, Tomato Ketchup, Water, Garam Masala, Oil"
    }])
  
  dataa=response['choices'][0]['message']['content']
  text_val=dataa
  language = 'en'  
  obj = gTTS(text=text_val, lang=language, slow=False)  
  obj.save("exam.mp3") 
  return response['choices'][0]['message']['content']


# Create a Flask web application object named app and define a route for the root URL that responds to GET and POST requests



@app.route('/home1', methods=['GET', 'POST'])
# This code defines a function that generates a tutorial based on user input obtained through a POST request.
def home1():

  output = ""

  if request.method == 'POST':

    components = request.form['components']

    output = generate_tutorial(components)

  return render_template_string('''

 <!DOCTYPE html>

 <html>

 <head>

  <title>Infinite Project Generator</title>
  <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0,shrink-to-fit=no">

    <!-- CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <link rel="stylesheet" href="{{ url_for('static',filename='css/style.css') }}">
    
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css"/>

    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">

  <script>

  async function generateTutorial() {

   const components = document.querySelector('#components').value;

   const output = document.querySelector('#output');

   output.textContent = 'Cooking a recipe for you...';

   const response = await fetch('/generate', {

    method: 'POST',

    body: new FormData(document.querySelector('#tutorial-form'))

   });

   const newOutput = await response.text();

   output.textContent = newOutput;

  }

  function copyToClipboard() {

   const output = document.querySelector('#output');

   const textarea = document.createElement('textarea');

   textarea.value = output.textContent;

   document.body.appendChild(textarea);

   textarea.select();

   document.execCommand('copy');

   document.body.removeChild(textarea);

   alert('Copied to clipboard');

  }

  </script>

 </head>

 <body>
  <!-- Navigation Bar -->
    <div id="Section-1">
        <nav class="navbar navbar-expand-lg navbar-light bg-grey">
            <a class="navbar-brand mr-auto" href="{{url_for('home')}}" style="font-family: 'Times New Roman', Times, serif;">
                
                RG</a>
            <a href="{{url_for('home')}}" class="w-100 text-center text-dark">RECIPE GENERATION FROM FOOD IMAGE AND INGREDIENTS</a>
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse " id="navbarNavDropdown">
            <ul class="navbar-nav ml-auto">
                <li class="nav-item active">
                <a class="nav-link" href="{{url_for('home')}}">Images <span class="sr-only">(current)</span></a>
                </li>
                <li class="nav-item active">
                    <a class="nav-link" href="{{url_for('home1')}}">Ingredients <span class="sr-only">(current)</span></a>
                    </li>
                
            </ul>
            </div>
        </nav>
    </div>

  <div class="container">

   

   <form id="tutorial-form" onsubmit="event.preventDefault(); generateTutorial();" class="mb-3">

    <div class="mb-3">

     <label for="components" class="form-label">Ingredients / Items:</label>

     <input type="text" class="form-control" id="components" name="components" placeholder="Enter the list of Ingredients or items you have e.g. Bread, jam, potato etc. " required>

    </div>

    <button type="submit" class="btn btn-primary">Submit</button>

   </form>

   <div class="card">

    <div class="card-header d-flex justify-content-between align-items-center">

     Output:

     <button class="btn btn-secondary btn-sm" onclick="copyToClipboard()">Copy</button>

    </div>

    <div class="card-body">

     <pre id="output" class="mb-0" style="white-space: pre-wrap;">{{ output }}</pre>
      <li class="btn btn-primary">
                    <a class="nav-link" href="{{url_for('playsoundd')}}">click here for audio <span class="sr-only">(current)</span></a>
                    </li>

    </div>

   </div>

  </div>

 </body>

 </html>

 ''',
                                output=output)


# This code defines a route for the URL "/generate" that only accepts POST requests.
@app.route('/playsoundd')
def playsoundd(): 
    myappplay("exam.mp3")
    return render_template("home1.html")
@app.route('/generate', methods=['POST'])
# This code defines a function 'generate' that takes a POST request containing a 'components' field and returns the result of calling the 'generate_tutorial' function with the provided components as input.
def generate():

  components = request.form['components']

  return generate_tutorial(components)

# chat initialization
model = load_model("chatbot_model.h5")
intents = json.loads(open("food_quires.json").read())
words = pickle.load(open("words.pkl", "rb"))
classes = pickle.load(open("classes.pkl", "rb"))


@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/get", methods=["POST"])
def chatbot_response():
    msg = request.form["msg"]
    if msg.startswith('my name is'):
        name = msg[11:]
        ints = predict_class(msg, model)
        res1 = getResponse(ints, intents)
        res =res1.replace("{n}",name)
    elif msg.startswith('hi my name is'):
        name = msg[14:]
        ints = predict_class(msg, model)
        res1 = getResponse(ints, intents)
        res =res1.replace("{n}",name)
    else:
        ints = predict_class(msg, model)
        res = getResponse(ints, intents)
    return res


# chat functionalities
def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words


# return bag of words array: 0 or 1 for each word in the bag that exists in the sentence
def bow(sentence, words, show_details=True):
    # tokenize the pattern
    sentence_words = clean_up_sentence(sentence)
    # bag of words - matrix of N words, vocabulary matrix
    bag = [0] * len(words)
    for s in sentence_words:
        for i, w in enumerate(words):
            if w == s:
                # assign 1 if current word is in the vocabulary position
                bag[i] = 1
                if show_details:
                    print("found in bag: %s" % w)
    return np.array(bag)


def predict_class(sentence, model):
    # filter out predictions below a threshold
    p = bow(sentence, words, show_details=False)
    res = model.predict(np.array([p]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
    # sort by strength of probability
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
    return return_list


def getResponse(ints, intents_json):
    tag = ints[0]["intent"]
    list_of_intents = intents_json["intents"]
    for i in list_of_intents:
        if i["tag"] == tag:
            result = random.choice(i["responses"])
            break
    return result



if __name__ == '__main__':

  app.run(host='127.0.0.1', port=5000, debug=True)
