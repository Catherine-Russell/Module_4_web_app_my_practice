from lib.album import Album
"""
test - info correctly assigned
test - info looks pretty
test - eq
"""

def test_album_constructs():
    album = Album(1, "Doolittle", 1989, 1)
    assert album.id == 1
    assert album.title == "Doolittle"
    assert album.release_year == 1989
    assert album.artist_id == 1

def test_albums_format_niceley():
    album = Album(1, "Doolittle", 1989, 1)
    assert str(album) == "Album(1, Doolittle, 1989, 1)"

def test_albums_are_equal():
    album1 = Album(1, "title", 2000, 1)
    album2 = Album(1, "title", 2000, 1)
    assert album1 == album2