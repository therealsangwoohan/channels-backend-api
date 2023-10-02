from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from config import DATABASE_URI

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
db = SQLAlchemy(app)
app.app_context().push()

from api.routes.channel import channel_bp
from api.routes.message import message_bp

app.register_blueprint(channel_bp)
app.register_blueprint(message_bp)
