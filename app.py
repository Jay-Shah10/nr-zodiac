from flask import Flask, render_template
import logging
from newrelic.agent import NewRelicContextFormatter

app = Flask(__name__) # name for the Flask app

#Instantiate a new log handler.
handler = logging.StreamHandler()

#Instantiate the log formatter and add it to the log handler
formatter = NewRelicContextFormatter()
handler.setFormatter(formatter)

# Get the root logger and add the handler to ti. 
root_logger = logging.getLogger()
root_logger.addHandler(handler)

logger = logging.getLogger(__name__)

# ++++++++++++Navbar stuff +++++++++
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

@app.route("/test_error")
def testError():
    logger.info("This is a test log info level.")
    logger.debug("This is a test debug log.")
    raise Exception("This is a test Error")
# ++++++++++++++++++++++++++++++++


@app.route("/signs/aries/")
def aries():
    return render_template('aries.html')

@app.route("/signs/leo")
def leo():
    return render_template('leo.html')

@app.route("/signs/cancer")
def cancer():
    return render_template('cancer.html')

@app.route("/signs/pisces")
def pisces():
    return render_template('pisces.html')

@app.route("/signs/scorpio")
def scorpio():
    return render_template('scorpio.html')

@app.route("/signs/taurus")
def taurus():
    return render_template('taurus.html')

@app.route("/signs/sagittarius")
def sagittarius():
    return render_template('sagittarius.html')


@app.route("/signs/gemini")
def gemini():
    return render_template('gemini.html')

@app.route("/signs/virgo")
def virgo():
    return render_template('virgo.html')

@app.route("/signs/libra")
def libra():
    return render_template('libra.html')

@app.route("/signs/capricorn")
def capricorn():
    return render_template('capricorn.html')

@app.route("/signs/aquarius")
def aquarius():
    return render_template('aquarius.html')

if __name__ == "__main__":
   # running the server.
   app.run(host='0.0.0.0', debug = True)  # to allow for debugging and auto-reload

