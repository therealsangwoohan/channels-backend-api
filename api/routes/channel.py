from flask import jsonify, request, Blueprint

from api import db
from api.models import Channel

channel_bp = Blueprint('channel', __name__)


@channel_bp.get("/api/channels")
def get_channels():
    channels = Channel.query.all()
    list_of_channels = []
    for channel in channels:
        list_of_channels.append({
            "channel_id": channel.channel_id,
            "channel_name": channel.channel_name,
            "admin_id": channel.admin_id
        })
    return jsonify(list_of_channels)


@channel_bp.get("/api/channels/<channel_id>")
def get_channel(channel_id):
    channel = Channel.query.get(channel_id)
    return {"channel_id": channel.channel_id,
            "channel_name": channel.channel_name,
            "admin_id": channel.admin_id}


@channel_bp.post("/api/channels")
def create_channel():
    data = request.get_json()
    channel = Channel(channel_name=data["channel_name"],
                      admin_id=data["admin_id"])
    db.session.add(channel)
    db.session.commit()
    print(channel.channel_id)
    return jsonify({'message': 'Channel created successfully'})


@channel_bp.delete("/api/channels/<channel_id>")
def delete_channel(channel_id):
    channel = Channel.query.filter_by(channel_id=channel_id).one()
    db.session.delete(channel)
    db.session.commit()
    return jsonify({'message': 'Channel deleted!'})
