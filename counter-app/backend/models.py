from flask_sqlalchemy import SQLAlchemy
#import db

db = SQLAlchemy()
class Dataset(db.Model):
    id=db.Column("id",db.Integer, primary_key=True)
    img=db.Column(db.text, unique=True, nullable=False)
    hue=db.Column(db.Float)
    sat=db.Column(db.Float)
    val=db.Column(db.Float)
    contrast=db.Column(db.Float)
    homogeneity=db.Column(db.Float)
    entropy=db.Column(db.Float)

    def __init__ (self, img, hue, sat, val, contrast, homogeneity, entropy):
        self.img=img
        self.hue=hue
        self.sat=sat
        self.val=val
        self.contrast=contrast
        self.homogeneity=homogeneity
        self.entropy=entropy