from sqlalchemy import (
    create_engine, Column, Float, ForeignKey, Integer, String
)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# execute instructions from our localhost "chinook" db
db = create_engine("postgresql:///chinook")
base = declarative_base()

# create a class-based model for the "artist" table


class Artist(base):
    __tablename__ = "Artist"
    ArtistId = Column(Integer, primary_key=True)
    Name = Column(String)


# create a class-based model for the "album" table
class Album(base):
    __tablename__ = "Album"
    AlbumId = Column(Integer, primary_key=True)
    Title = Column(String)
    ArtistId = Column(Integer, ForeignKey("Artist.ArtistId"))


# create a class-based model for the "tracks" table
class Track(base):
    __tablename__ = "Track"
    TrackId = Column(Integer, primary_key=True)
    Name = Column(String)
    AlbumId = Column(Integer, ForeignKey("Album.AlbumId"))
    MediaTypeId = Column(Integer, primary_key=False)
    GenreId = Column(Integer, primary_key=False)
    Composer = Column(String)
    Milliseconds = Column(Integer, primary_key=False)
    Bytes = Column(Integer, primary_key=False)
    UnitPrice = Column(Float)


# instead of connectiong to the database directly, we create a session
# create a new instance if sessionmaker, and point it to our db
Session = sessionmaker(db)
# opens an actual session by calling the Session() subclass above
session = Session()

# create db using declarative subclass above
base.metadata.create_all(db)

# Query 1 - select all from the artists table
# artists = session.query(Artist)
# for artist in artists:
#     print(artist.ArtistId, artist.Name, sep=" | ")

# Query 2 - select only the name column from the artist table
# artists = session.query(Artist)
# for artist in artists:
#     print(artist.Name)

# Query 3 - selsct "Queen" from the artist table
# artist = session.query(Artist).filter_by(Name="Queen").first()
# print(artist.ArtistId, artist.Name, sep=" | ")

# Query 4 - select only the artist id of 51 from artist table
# artist = session.query(Artist).filter_by(ArtistId=51).first()
# print(artist.ArtistId, artist.Name, sep=" | ")

# Query 5 - select only the albums with artist id of 51 in album table
# albums = session.query(Album).filter_by(ArtistId=51)
# for album in albums:
#     print(album.AlbumId, album.Title, album.ArtistId, sep=" | ")

# Query 6 - select only the tracks by queen from the tracks table
tracks = session.query(Track).filter_by(Composer="Queen")
for track in tracks:
    print(
        track.TrackId,
        track.Name,
        track.AlbumId,
        track.MediaTypeId,
        track.GenreId,
        track.Composer,
        track.Milliseconds,
        track.Bytes,
        track.UnitPrice,
        sep=" | "
    )
