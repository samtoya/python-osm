from sqlalchemy import Column, Integer, String, DateTime
from main import Base


class Country(Base):
    __tablename__ = 'countries'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    iso2 = Column(String(250))
    iso3 = Column(String(250))
    phonecode = Column(String(250))
    capital = Column(String(250))
    currency = Column(String(250))
    currency_symbol = Column(String(250))
    tld = Column(String(250))
    native = Column(String(250))
    region = Column(String(250))
    subregion = Column(String(250))
    timezones = Column(String(250))
    latitude = Column(String(250))
    longitude = Column(String(250))
    emoji = Column(String(250))
    emojiU = Column(String(250))
    created_at = Column(DateTime(250))
    updated_at = Column(DateTime(250))
    flag = Column(String(250))
    wikiDataId = Column(String(250))


class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    country_id = Column(String(250))
    country_code = Column(String(250))
    fips_code = Column(String(250))
    iso2 = Column(String(250))
    latitude = Column(String(250))
    longitude = Column(String(250))
    created_at = Column(DateTime(250))
    updated_at = Column(DateTime(250))
    flag = Column(Integer)
    wikiDataId = Column(String(250))


class City(Base):
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    state_id = Column(String(250))
    state_code = Column(String(250))
    country_id = Column(String(250))
    country_code = Column(String(250))
    latitude = Column(String(250))
    longitude = Column(String(250))
    flag = Column(Integer)
    wikiDataId = Column(String(250))
    created_at = Column(DateTime(250))
    updated_at = Column(DateTime(250))
