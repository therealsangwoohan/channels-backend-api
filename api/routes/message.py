from flask import Blueprint, jsonify, request

from api.database import get_db_connection

message_bp = Blueprint('message', __name__)


@message_bp.get("/api/messages")
def get_messages():
    channel_id = request.args.get("channel_id")

    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM message WHERE channel_id = %s;",
                           (channel_id,))
            messages = cursor.fetchall()

    list_of_messages = []
    for message_id, channel_id, user_id, sent_at, text in messages:
        list_of_messages.append({
            "message_id": message_id,
            "user_id": user_id,
            "text": text,
        })
    return jsonify(list_of_messages)
