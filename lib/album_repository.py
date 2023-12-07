from lib.album import Album

class AlbumRepository:
    def __init__(self, connection=None):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * from albums')
        albums = []
        for row in rows:
            item = Album(row["album_id"], row["title"], row["release_year"], row["artist_id"])
            albums.append(item)
        return albums

    def create(self, album):
        rows = self._connection.execute('INSERT INTO albums (title, release_year, artist_id) VALUES (%s, %s, %s) RETURNING album_id', [album.title, album.release_year, album.artist_id])
        row = rows[0]
        album.album_id = row["album_id"]
        return album
    
    def find(self, album_id):
        raw_data = self._connection.execute('SELECT * from albums WHERE album_id = %s', [album_id])
        data = raw_data[0]
        return Album(data["album_id"], data["title"], data["release_year"], data["artist_id"])
    

    # Delete an album by their id
    def delete(self, album_id):
        self._connection.execute(
            'DELETE FROM albums WHERE album_id = %s', [album_id])
        return None