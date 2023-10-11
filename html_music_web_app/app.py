import os
from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection
from lib.artist_repository import ArtistRepository
from lib.album_repository import AlbumRepository
from lib.album import Album
from lib.artist import Artist

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==


# == Example Code Below ==

# GET /emoji
# Returns a smiley face in HTML
# Try it:
#   ; open http://localhost:5001/emoji
@app.route('/emoji', methods=['GET'])
def get_emoji():
    # We use `render_template` to send the user the file `emoji.html`
    # But first, it gets processed to look for placeholders like {{ emoji }}
    # These placeholders are replaced with the values we pass in as arguments
    return render_template('emoji.html', emoji=':)')

# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.
from example_routes import apply_example_routes
apply_example_routes(app)

# == End Example Code ==

# ========= COPIED FROM MUSIC_WEB_APP ========= #

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
    return render_template("albums/index_albums.html", album_list=albums)

"""
GET /albums/id_number
retrieves album info for that one thing - 
    large header for album name then smaller for releaseyear and artist
/albums/<int=id>
    """

@app.route('/albums/<int:id>')
def get_album_info_by_id(id):
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    album_info = repository.find_album_and_artist_by_album_id(id)
    return render_template("albums/get_single_album.html",id=id, album_info=album_info)






# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
