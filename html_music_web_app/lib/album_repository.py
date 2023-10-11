from lib.album import Album


class AlbumRepository:
    def __init__(self, connection):
        self._connection = connection
    
    def all(self):
        rows = self._connection.execute("SELECT * FROM albums")
        albums = []
        for row in rows:
            item = Album(row["id"], row['title'], row['release_year'], row['artist_id'])
            albums.append(item)
        return albums
    
    def find(self, album_id):
        rows = self._connection.execute("SELECT * FROM albums WHERE id = %s", [album_id])
        row = rows[0]
        album = Album(row['id'], row['title'], row['release_year'], row['artist_id'])
        return album
    
    def create(self, album):
        self._connection.execute("INSERT INTO albums (title, release_year, artist_id) VALUES (%s, %s, %s)", [album.title, album.release_year, album.artist_id])
        return None
    
    def delete(self, album_id):
        self._connection.execute("DELETE FROM albums WHERE id = %s", [album_id])
        return None
    
    def find_album_and_artist_by_album_id(self, album_id):
        row = self._connection.execute("SELECT albums.id, title, release_year, artist_id, name from albums JOIN artists ON albums.artist_id = artists.id WHERE albums.id = %s", [album_id])
        album_info = {
            'title': row[0]['title'],
            'release_year':row[0]['release_year'],
            'artist':row[0]['name']
        }
        return album_info