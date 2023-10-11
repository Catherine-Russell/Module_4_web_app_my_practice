from lib.album_repository import AlbumRepository
from lib.album import Album

def test_get_all_records(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = AlbumRepository(db_connection)
    albums = repository.all()
    assert albums == [
        Album(1, 'Doolittle', 1989, 1),
        Album(2, 'Surfer Rosa', 1988, 1),
        Album(3, 'Waterloo', 1974, 2),
        Album(4, 'Super Trouper', 1980, 2),
        Album(5, 'Bossanova', 1990, 1),
        Album(6, 'Lover', 2019, 3),
        Album(7, 'Folklore', 2020, 3),
        Album(8, 'I Put a Spell on You', 1965, 4),
        Album(9, 'Baltimore', 1978, 4),
        Album(10, 'Here Comes the Sun', 1971, 4),
        Album(11, 'Fodder on My Wings', 1982, 4),
        Album(12, 'Ring Ring', 1973, 2)
    ]

def test_find_one_record(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = AlbumRepository(db_connection)
    album = repository.find(3)
    assert album == Album(3, 'Waterloo', 1974, 2)

def test_create(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = AlbumRepository(db_connection)
    assert repository.create(Album(13, 'Red', 2005, 3)) == None
    albums = repository.all()
    assert albums == [
        Album(1, 'Doolittle', 1989, 1),
        Album(2, 'Surfer Rosa', 1988, 1),
        Album(3, 'Waterloo', 1974, 2),
        Album(4, 'Super Trouper', 1980, 2),
        Album(5, 'Bossanova', 1990, 1),
        Album(6, 'Lover', 2019, 3),
        Album(7, 'Folklore', 2020, 3),
        Album(8, 'I Put a Spell on You', 1965, 4),
        Album(9, 'Baltimore', 1978, 4),
        Album(10, 'Here Comes the Sun', 1971, 4),
        Album(11, 'Fodder on My Wings', 1982, 4),
        Album(12, 'Ring Ring', 1973, 2),
        Album(13, 'Red', 2005, 3)
    ]

def test_delete(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = AlbumRepository(db_connection)
    repository.delete(5)
    albums = repository.all()
    assert albums == [
        Album(1, 'Doolittle', 1989, 1),
        Album(2, 'Surfer Rosa', 1988, 1),
        Album(3, 'Waterloo', 1974, 2),
        Album(4, 'Super Trouper', 1980, 2),
        Album(6, 'Lover', 2019, 3),
        Album(7, 'Folklore', 2020, 3),
        Album(8, 'I Put a Spell on You', 1965, 4),
        Album(9, 'Baltimore', 1978, 4),
        Album(10, 'Here Comes the Sun', 1971, 4),
        Album(11, 'Fodder on My Wings', 1982, 4),
        Album(12, 'Ring Ring', 1973, 2),
    ]

def test_find_album_and_artist_by_album(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = AlbumRepository(db_connection)
    result = repository.find_album_and_artist_by_album_id(1)
    assert result == {
            'title': 'Doolittle',
            'release_year':1989,
            'artist':'Pixies'
        }
