from flask import Blueprint, jsonify, request

from api import db
from api.models import Message

message_bp = Blueprint('message', __name__)


@message_bp.get("/api/messages")
def get_messages():
    channel_id = request.args.get("channel_id")
    messages = Message.query.filter_by(channel_id=channel_id).all()
    list_of_messages = []
    for message in messages:
        list_of_messages.append({
            "message_id": message.message_id,
            "user_id": message.user_id,
            "text": message.text,
        })
    return jsonify(list_of_messages)


@message_bp.delete("/api/messages")
def delete_channels():
    db.session.query(Message).delete()
    db.session.commit()
    return jsonify({"message": "Every messages have been deleted."})
