#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

# from sqlalchemy.dialects.postgresql import JSON
from flask import Flask 
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# import dateutil.parser
# import babel
from shared_settings import db, app
from datetime import datetime

moment = Moment(app)
migrate = Migrate(app, db)


#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#

class Show(db.Model):
  __tablename__ = 'show'
  venue_id = db.Column('venue_id', db.Integer, db.ForeignKey('venue.id'), primary_key=True) 
  artist_id = db.Column('artist_id', db.Integer, db.ForeignKey('artist.id'), primary_key=True)
  start_time = db.Column('start_time', db.DateTime, primary_key=True, default=datetime.utcnow)
  
class Venue(db.Model):
    __tablename__ = 'venue'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    genres = db.Column(db.ARRAY(db.String()), nullable=False)
    city = db.Column(db.String(120), nullable=False)
    state = db.Column(db.String(120), nullable=False)
    address = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(120),nullable=True)
    website_link = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    seeking_talent = db.Column(db.String(1))
    seeking_description = db.Column(db.String(1000))
    shows = db.relationship('Show', backref='venue', lazy=True) 
      
    def __repr__(self):
      object_content = (
        f'<Venue {self.id} {self.name} {self.phone} '
        f'{self.city} {self.state} {self.address} '
        f'{self.website_link} '
        f'{self.facebook_link} '
        f'{self.seeking_talent} '
        f'{self.seeking_description}>'
      )
      return object_content 

class Artist(db.Model):
    __tablename__ = 'artist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    city = db.Column(db.String(120), nullable=False)
    state = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(120), nullable=True)
    website_link = db.Column(db.String(120))
    genres = db.Column(db.ARRAY(db.String(120)), nullable=False)
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    seeking_venue = db.Column(db.String(1))
    seeking_description = db.Column(db.String(1000))
    shows = db.relationship('Show', backref='artist', lazy=True)

    def __repr__(self):
      object_content = (
        f'<Artist {self.id} {self.name} {self.phone}'
        f'{self.city} {self.state}'
        f'{self.website}'
        f'{self.facebook_link}'
        f'{self.seeking_venue}'
        f'{self.seeking_description}>'
      )
      return object_content 
