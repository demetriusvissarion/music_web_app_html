## Exercise

Test-drive and implement the following change:

The page returned by `GET /albums` should contain a link for each album listed. It should link to `/albums/<id>`, where `<id>` is the corresponding album's id. That page should then show information about the specific album.

Run the server and make sure you can navigate, using your browser, from the albums list page to the single album page.





## Challenge

This is a process feedback challenge. That means you should record yourself doing it and
submit that recording to your coach for feedback. 

Test-drive and implement the following changes to the `music_web_app_html` project:

1. Add a route `GET /artists/<id>` which returns an HTML page showing details for a single artist.


2. Add a route `GET /artists` which returns an HTML page with the list of artists. This page should contain a link for each artist listed, linking to `/artists/<id>` where `<id>` needs to be the corresponding artist id.