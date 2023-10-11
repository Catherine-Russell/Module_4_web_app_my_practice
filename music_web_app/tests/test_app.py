# Tests for your routes go here


# === Example Code Below ===

"""
GET /emoji
"""
def test_get_emoji(web_client):
    response = web_client.get("/emoji")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == ":)"

def test_get_all_albums(web_client, db_connection):
    db_connection.seed('seeds/music_library.sql')
    response = web_client.get('/albums')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == ""\
        "Album(1, Doolittle, 1989, 1)\n" \
        "Album(2, Surfer Rosa, 1988, 1)\n" \
        "Album(3, Waterloo, 1974, 2)\n" \
        "Album(4, Super Trouper, 1980, 2)\n" \
        "Album(5, Bossanova, 1990, 1)\n" \
        "Album(6, Lover, 2019, 3)\n" \
        "Album(7, Folklore, 2020, 3)\n" \
        "Album(8, I Put a Spell on You, 1965, 4)\n" \
        "Album(9, Baltimore, 1978, 4)\n" \
        "Album(10, Here Comes the Sun, 1971, 4)\n" \
        "Album(11, Fodder on My Wings, 1982, 4)\n" \
        "Album(12, Ring Ring, 1973, 2)"
    
def test_post_albums(web_client, db_connection):
    db_connection.seed('seeds/music_library.sql')
    response = web_client.post('/albums', data={
        'id':'None',
        'name':'OK Computer',
        'release_year':'1997',
        'artist_id':'1'
        })
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Album added successfully"
    response = web_client.get('/albums')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == ""\
        "Album(1, Doolittle, 1989, 1)\n" \
        "Album(2, Surfer Rosa, 1988, 1)\n" \
        "Album(3, Waterloo, 1974, 2)\n" \
        "Album(4, Super Trouper, 1980, 2)\n" \
        "Album(5, Bossanova, 1990, 1)\n" \
        "Album(6, Lover, 2019, 3)\n" \
        "Album(7, Folklore, 2020, 3)\n" \
        "Album(8, I Put a Spell on You, 1965, 4)\n" \
        "Album(9, Baltimore, 1978, 4)\n" \
        "Album(10, Here Comes the Sun, 1971, 4)\n" \
        "Album(11, Fodder on My Wings, 1982, 4)\n" \
        "Album(12, Ring Ring, 1973, 2)\n" \
        "Album(13, OK Computer, 1997, 1)" \
        
def test_get_all_artists(web_client, db_connection):
    db_connection.seed('seeds/music_library.sql')
    response = web_client.get('/artists')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Pixies, ABBA, Taylor Swift, Nina Simone"

def test_post_artist(web_client, db_connection):
    db_connection.seed('seeds/music_library.sql')
    response = web_client.post('/artists', data={
        'id':'None',
        'name':'Radiohead',
        'genre':'rock'
        })
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Artist successfully added!"
    
    response = web_client.get('/artists')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Pixies, ABBA, Taylor Swift, Nina Simone, Radiohead"



# === End Example Code ===
