from api import db


class Channel(db.Model):
    channel_id = db.Column(db.Integer, primary_key=True)
    channel_name = db.Column(db.String(255))
    admin_id = db.Column(db.String(255))

    messages = db.relationship('Message', backref='channel', passive_deletes=True)

    def __init__(self, channel_name, admin_id):
        self.channel_name = channel_name
        self.admin_id = admin_id

    def __repr__(self):
        return f"Channel(channel_name={self.channel_name}, admin_id={self.admin_id})"


class Message(db.Model):
    message_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    channel_id = db.Column(db.Integer,
                           db.ForeignKey('channel.channel_id',
                                         ondelete="CASCADE"),
                           nullable=False)
    user_id = db.Column(db.String(255))
    sent_at = db.Column(db.DateTime)
    text = db.Column(db.String(255))

    def __init__(self, channel_id, user_id, sent_at, text):
        self.channel_id = channel_id
        self.user_id = user_id
        self.sent_at = sent_at
        self.text = text

    def __repr__(self):
        return f"Message(channel_id={self.channel_id}, user_id={self.user_id}, sent_at={self.sent_at}, text={self.text})"
