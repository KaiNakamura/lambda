from dotenv import load_dotenv
load_dotenv()
from flask import Flask
from . import playground

app = Flask(__name__)
app.register_blueprint(playground.playground)

from . import views