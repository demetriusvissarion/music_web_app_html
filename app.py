import os
from flask import Flask, request, render_template, redirect, url_for
from lib.database_connection import get_flask_database_connection
from lib.album import Album
from lib.album_repository import AlbumRepository
from lib.artist import Artist
from lib.artist_repository import ArtistRepository

# Create a new Flask app
app = Flask(__name__)

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

# == Your Routes Here ==

@app.route('/')
def get_homepage():
    return render_template('homepage.html')


# POST /albums
# Creates a new album
@app.route('/albums', methods=['POST'])
def create_album():
    # Set up the database connection and repository
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)

    # Get the fields from the request form
    title = request.form['title']
    release_year = request.form['release_year']
    artist_id = request.form['artist_id']

    # Create a album object
    album = Album(None, title, release_year, artist_id)

    # Check for validity and if not valid, show the form again with errors
    if not album.is_valid():
        return render_template('albums/new.html', album=album, errors=album.generate_errors()), 400

    # Save the album to the database
    album = repository.create(album)

    # Redirect to the album's show route to the user can see it
    return redirect(f"/albums/{album.album_id}")



@app.route('/albums/', methods=['GET'])
def get_all_records():
    connection = get_flask_database_connection(app)
    album_repository = AlbumRepository(connection)
    albums = album_repository.all()
    return render_template('albums/index.html', albums=albums)


# GET /albums/new
# Returns a form to create a new album
@app.route('/albums/new', methods=['GET'])
def get_new_album():
    return render_template('albums/new.html')


@app.route('/albums/<int:album_id>', methods=['GET'])
def get_album_by_id(album_id):
    connection = get_flask_database_connection(app)
    album_repository = AlbumRepository(connection)
    album = album_repository.find(album_id)
    return render_template('albums/show.html', album=album)


# Request:
# GET /artists
#   With body parameter: 
@app.route('/artists/', methods=['GET'])
def get_all_artists():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    artists = repository.all() # Get all artists
    return render_template('artists/index.html', artists=artists)


@app.route('/artists/<int:artist_id>', methods=['GET'])
def get_artist_by_id(artist_id):
    connection = get_flask_database_connection(app)
    artist_repository = ArtistRepository(connection)
    artist = artist_repository.find(artist_id)
    return render_template('artists/show.html', artist=artist)


# Request:
# POST /artists
#   With body parameter: artist_name=Queen, genre=Rock
# @app.route('/artists', methods=['POST'])
# def post_new_artist():
#     connection = get_flask_database_connection(app)
#     repository = ArtistRepository(connection)
#     artist_name = request.form['artist_name'] 
#     genre = request.form['genre'] 
#     artist = Artist(None, artist_name, genre)
#     repository.create(artist) 
#     return '', 200
@app.route('/artists', methods=['POST'])
def create_artist():
    # Set up the database connection and repository
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)

    # Get the fields from the request form
    artist_name = request.form['artist_name']
    genre = request.form['genre']

    # Create a artist object
    artist = Artist(None, artist_name, genre)

    # Check for validity and if not valid, show the form again with errors
    if not artist.is_valid():
        return render_template('artists/new.html', artist=artist, errors=artist.generate_errors()), 400

    # Save the artist to the database
    artist = repository.create(artist)

    # Redirect to the artist's show route to the user can see it
    return redirect(f"/artists/{artist.artist_id}")


# GET /artists/new
# Returns a form to create a new artist
@app.route('/artists/new', methods=['GET'])
def get_new_artist():
    return render_template('artists/new.html')


# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
