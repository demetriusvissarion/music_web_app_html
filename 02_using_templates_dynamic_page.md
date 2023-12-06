## Exercise

Create a new project `music_web_app_html` using [the new HTML starter for this
phase](https://github.com/makersacademy/web-applications-in-python-project-starter-html).

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

[Example solution](https://www.youtube.com/watch?v=1GcIg1lDTC4&t=0s)

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
