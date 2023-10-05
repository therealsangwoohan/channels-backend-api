from flask import Flask
from flask_cors import CORS
from api.routes.channel import channel_bp
from api.routes.message import message_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(channel_bp)
app.register_blueprint(message_bp)
