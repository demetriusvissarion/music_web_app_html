## Exercise

Create a new project `music_web_app_html`
# Install dependencies and set up the virtual environment
; pipenv install

# Activate the virtual environment
; pipenv shell

# Install the virtual browser we will use for testing
; playwright install
# If you have problems with the above, contact your coach

# Create a test and development database
; createdb YOUR_PROJECT_NAME
; createdb YOUR_PROJECT_NAME_test

# Open lib/database_connection.py and change the database names
; open lib/database_connection.py

# Seed the development database (ensure you have run `pipenv shell` first)
; python seed_dev_database.py

# Run the tests (with extra logging)
; pytest -sv

# Run the app
; python app.py
# Now visit http://localhost:5001/emoji in your browser

You can copy over your albums-related code from the previous challenges if you want
to, rather than starting over from scratch. You'll probably want these files
(although your chosen filenames might differ!):

* From `lib`: `album.py`, `album_repository.py`, `artist.py`, `artist_repository.py`
* From `tests`: `test_album.py`, `test_album_repository.py`, `test_artist.py`,
  `test_artist_repository.py`
* Optionally copy the album- and artist-related routes from your previous
  `app.py` challenge (plus repository class imports), into the new `app.py`
  file from the new starter project, noting *you will need to change at least
  some of the routes*
* Copy your related seed file over too, into `seeds`; make sure to seed your new
  databases
* Finally, check your original route(s) work in the new project e.g. check `GET
  /albums` by using a browser

Test-drive a `GET /albums` route that connects with an `AlbumRepository` and the
database to return a result like this:

```html
<!-- GET /albums -->

<html>
  <head></head>
  <body>
    <h1>Albums</h1>

    <div>
      Title: Doolittle
      Released: 1989
    </div>

    <div>
      Title: Surfer Rosa
      Released: 1988
    </div>

    <!-- ... -->
  </body>
</html>
```

_(Don't forget to run the app using `python app.py`)._

Use your web browser to access the page and check that it works in the browser
too.

<details>
  <summary>:speech_balloon: I want a bit more challenge.</summary>

  ---

  The above HTML document isn't very easy for a human to read. In the
  web-browser the Title and Release Date are all on one line. Improve this
  formatting using HTML.

  Finally, ensure the HTML validates using an online HTML validator.

  ---

</details>

Issues:
1. db_connection.seed("seeds/music_web_app_html.sql") doesn't work for:
tests/test_app.py::test_get_all_records[chromium] FAILED
tests/test_app.py::test_get_all_artists_string FAILED
tests/test_app.py::test_post_new_artist FAILED

2. 







## Challenge

In your project `music_web_app_html`.

Test-drive and implement a route that returns the HTML content for a single
album. It should work like this:

```html
<!-- Example for GET /albums/1 -->

<html>
  <head></head>
  <body>
    <h1>Doolittle</h1>
    <p>
      Release year: 1989
      Artist: Pixies
    </p>
  </body>
</html>

<!-- Example for GET /albums/2 -->

<html>
  <head></head>
  <body>
    <h1>Surfer Rosa</h1>
    <p>
      Release year: 1988
      Artist: Pixies
    </p>
  </body>
</html>
```
