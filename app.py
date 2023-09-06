import urllib.request, json
from flask import Flask, render_template, request   # import flask framework
app = Flask(__name__)                               # create an app instance

@app.route("/")                                     # use the home url
def hello():                                        # method called hello
    # We need to add the URL we will be using to fetch information from.
    # Sometimes this means also sending some data like a key, but not for this one
    url = "https://xkcd.com/info.0.json"
    response = urllib.request.urlopen(url)
    # Once we have the response we need to extract the data we want.
    data = response.read()
    dict = json.loads(data)             
    return render_template("index.html", datum=dict) #return template

@app.route("/about")
def about():
    name = request.args.get('name') if request.args.get('name') else "Maria" 
    return render_template("about.html", aboutName=name)

if __name__ == "__main__":                          # when running python app.py
    app.run(debug=True)                             # run the flask app