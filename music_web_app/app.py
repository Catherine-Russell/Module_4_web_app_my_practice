import os
from flask import Flask, request
from lib.database_connection import get_flask_database_connection
from lib.album_repository import AlbumRepository
from lib.album import Album
from lib.artist_repository import ArtistRepository
from lib.artist import Artist


# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

# == Example Code Below ==

# GET /emoji
# Returns a emojiy face
# Try it:
#   ; curl http://127.0.0.1:5001/emoji
@app.route('/emoji', methods=['GET'])
def get_emoji():
    return ":)"

"""
create READ all albums in albums
GET /albums
no paramters - returns list of albums
"""
@app.route('/albums', methods=["GET"])
def get_all_albums():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    albums = repository.all()
    album_strings = [str(album) for album in albums]
    return "\n".join(album_strings)


"""
create a new album in albums
POST /albums
body parameters:
    title=Voyage
    release_year=2022
    artist_id=2
"""
@app.route('/albums', methods=['POST'])
def post_album():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    id = request.form['id']
    name = request.form['name']
    release_year = request.form['release_year']
    artist_id = request.form['artist_id']
    new_album = Album(id, name, release_year, artist_id)
    repository.create(new_album)
    return "Album added successfully"


"""
create READ all artists in artists
GET /artists
no paramters - returns list of artists
"""
@app.route('/artists', methods = ['GET'])
def get_all_artists():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    artists = repository.all()
    artists_names = [artist.name for artist in artists]
    return ", ".join(artists_names)


"""
create a new artist in artists
POST /artists
body parameters:
    id - none so db can fill it in
    name
    genre
"""
@app.route('/artists', methods = ['POST'])
def create_new_artist():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    id = request.form['id']
    name = request.form['name']
    genre = request.form['genre']
    new_artist = Artist(id, name, genre)
    repository.create(new_artist)
    return "Artist successfully added!"


# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.
from example_routes import apply_example_routes
apply_example_routes(app)

# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))

