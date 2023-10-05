from flask import jsonify, request, Blueprint

from api.database import get_db_connection

channel_bp = Blueprint('channel', __name__)


@channel_bp.get("/api/channels")
def get_channels():
    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM channel;")
            channels = cursor.fetchall()

    list_of_channels = []
    for channel_id, channel_name, admin_id in channels:
        list_of_channels.append({
            "channel_id": channel_id,
            "channel_name": channel_name,
            "admin_id": admin_id
        })
    return jsonify(list_of_channels)


@channel_bp.get("/api/channels/<channel_id>")
def get_channel(channel_id):
    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM channel WHERE channel_id = %s;",
                           (channel_id,))
            channel_id, channel_name, admin_id = cursor.fetchone()

    return {"channel_id": channel_id,
            "channel_name": channel_name,
            "admin_id": admin_id}


@channel_bp.post("/api/channels")
def create_channel():
    data = request.get_json()

    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO channel (channel_name, admin_id) VALUES (%s, %s);",
                           (data["channel_name"], data["admin_id"]))

    return jsonify({'message': 'Channel created successfully'})


@channel_bp.delete("/api/channels/<channel_id>")
def delete_channel(channel_id):
    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM channel WHERE channel_id = %s;",
                           (channel_id,))

    return jsonify({'message': 'Channel deleted!'})
