from flask import Flask, render_template

app = Flask(__name__) # name for the Flask app

# defining a route. 
@app.route("/", methods=['GET'])
def home():
   return render_template('index.html')

@app.route("/signs/")
def showSigns():
    """
    This method is will show all the signs that are there. 
    """
    return render_template('signs.html')

@app.route("/signs/aries/")
def aries():
    return "hello aries"

@app.route("/signs/leo")
def leo():
    return "hello Leo"

@app.route("/signs/cancer")
def cancer():
    return "hello Cancer"

@app.route("/signs/pisces")
def pisces():
    return 'Hello Pisces'

@app.route("/signs/scorpio")
def scorpio():
    return "Hello Scorpio"

@app.route("/signs/taurus")
def taurus():
    return "Hello Taurus"

@app.route("/signs/sagittarius")
def sagittarius():
    return "Hello Sagittaius"


@app.route("/signs/gemini")
def gemini():
    return "Hello Gemini"

@app.route("/signs/virgo")
def virgo():
    return "Hello Virgo"

@app.route("/signs/libra")
def libra():
    return "Hello Libra"

@app.route("/signs/capricorn")
def capricorn():
    return "Hello Capricorn"

@app.route("/signs/aquarius")
def aquarius():
    return "Hello Aquarius"

if __name__ == "__main__":
   # running the server. 
   app.run(debug = True)  # to allow for debugging and auto-reload

