from . import db

class Game(db.Model):
    __tablename__ = 'game'
    id = db.Column(
        db.String(64),
        primary_key=True
    )
    move = db.Column(
        db.String(64),
        index=False,
        nullable=False
    )
    def __repr__(self):
        return '<Song {}>'.format(self.move)