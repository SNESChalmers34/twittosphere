from twittosphere.db import Base

from sqlalchemy import Column, Integer, Unicode, UnicodeText
from sqlalchemy import ForeignKey, Boolean, DateTime, Float
from sqlalchemy.orm import relationship


# Put your models here
class Project(Base):
    __tablename__ = 'projects'
    id = Column(Integer, primary_key=True)
    name = Column(Unicode(50))
    description = Column(UnicodeText)
    searches = relationship('Search')
    credentials = relationship('Credential')


class Credential(Base):
    __tablename__ = 'credentials'
    id = Column(Integer, primary_key=True)
    name = Column(Unicode(50))
    api_type_id = Column(Integer, ForeignKey('apitypes.id'))
    api_type = relationship("APIType")
    consumer_key = Column(Unicode(100))
    consumer_secret = Column(Unicode(100))
    access_token = Column(Unicode(100))
    access_secret = Column(Unicode(100))
    project_id = Column(Integer, ForeignKey('projects.id'))


class APIType(Base):
    __tablename__ = 'apitypes'
    id = Column(Integer, primary_key=True)
    name = Column(Unicode(50))


class SearchGeolocation(Base):
    __tablename__ = 'search_geo'
    id = Column(Integer, primary_key=True)
    lattitude = Column(Float)
    longitude = Column(Float)
    search_id = Column(Integer, ForeignKey('searches.id'))


class SearchQuery(Base):
    __tablename__ = 'search_query'
    id = Column(Integer, primary_key=True)
    param = Column(Unicode(200))
    value = Column(Unicode(200))
    search_id = Column(Integer, ForeignKey('searches.id'))


class Search(Base):
    __tablename__ = 'searches'
    id = Column(Integer, primary_key=True)
    name = Column(Unicode(50))
    description = Column(UnicodeText)
    date_created = Column(DateTime)
    project_id = Column(Integer, ForeignKey('projects.id'))
    geolocations = relationship(SearchGeolocation)
    search_queries = relationship(SearchQuery)
    active = Column(Boolean)
