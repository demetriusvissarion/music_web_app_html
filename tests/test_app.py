from playwright.sync_api import Page, expect
from bs4 import BeautifulSoup


# Tests for your routes go here

# === Example Code Below ===

"""
GET /emoji
"""
def test_get_emoji(web_client):
    response = web_client.get("/emoji")
    assert response.status_code == 200

    soup = BeautifulSoup(response.data, 'html.parser')
    content = soup.find('strong').get_text()

    assert content == ":)"

# === End Example Code ===


# """
# When: I make a POST request to /albums
# Then: I should get a 200 response
# """
# def test_post_create_album(db_connection, web_client, test_web_address):
#     db_connection.seed("seeds/music_web_app_html.sql")
#     response = web_client.post('/albums', data={
#         'title': 'Voyage', 
#         'release_year': '2022', 
#         'artist_id': '2'
#         })

#     assert response.status_code == 200
#     assert response.data.decode('utf-8') == ''


"""
When: I make a GET request to /albums
Then: I should get a 200 response with a list of records, as html
"""
def test_get_all_records(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_web_app_html.sql")
    page.goto(f"http://{test_web_address}/albums")

    paragraph_tags = page.locator("p")

    expect(paragraph_tags).to_have_text(['\n                    Doolittle\n                ', '\n                    Surfer Rosa\n                ', '\n                    Waterloo\n                ', '\n                    Super Trouper\n                ', '\n                    Bossanova\n                ', '\n                    Lover\n                ', '\n                    Folklore\n                ', '\n                    I Put a Spell on You\n                ', '\n                    Baltimore\n                ', '\n                    Here Comes the Sun\n                ', '\n                    Fodder on My Wings\n                ', '\n                    Ring Ring\n                '])


# """
# When: I make a GET request to /albums
# Then: I should get a 200 response with a list of records
# """
# def test_get_all_records(db_connection, web_client):
#     db_connection.seed("seeds/music_web_app_html.sql")
#     web_client.post('/albums', data={
#     'title': 'Voyage', 
#     'release_year': '2022', 
#     'artist_id': '2'
#     })
#     response = web_client.get('/albums')

#     assert response.status_code == 200
#     assert response.data.decode('utf-8') == "" \
#         'Album(1, Doolittle, 1989, 1)\nAlbum(2, Surfer Rosa, 1988, 1)\nAlbum(3, Waterloo, 1974, 2)\nAlbum(4, Super Trouper, 1980, 2)\nAlbum(5, Bossanova, 1990, 1)\nAlbum(6, Lover, 2019, 3)\nAlbum(7, Folklore, 2020, 3)\nAlbum(8, I Put a Spell on You, 1965, 4)\nAlbum(9, Baltimore, 1978, 4)\nAlbum(10, Here Comes the Sun, 1971, 4)\nAlbum(11, Fodder on My Wings, 1982, 4)\nAlbum(12, Ring Ring, 1973, 2)\nAlbum(13, Voyage, 2022, 2)'


# """
# When: I make a POST request to /albums with no data
# Then: I should get a 400 response
# """
# def test_post_create_album_with_no_data(db_connection, web_client):
#     db_connection.seed("seeds/music_web_app_html.sql")

#     response = web_client.post("/albums")
#     assert response.status_code == 400
#     assert response.data.decode('utf-8') == "" \
#         "No data to create album"

#     get_response = web_client.get('/albums')
#     assert get_response.status_code == 200
#     assert get_response.data.decode('utf-8') == "" \
#         'Album(1, Doolittle, 1989, 1)\nAlbum(2, Surfer Rosa, 1988, 1)\nAlbum(3, Waterloo, 1974, 2)\nAlbum(4, Super Trouper, 1980, 2)\nAlbum(5, Bossanova, 1990, 1)\nAlbum(6, Lover, 2019, 3)\nAlbum(7, Folklore, 2020, 3)\nAlbum(8, I Put a Spell on You, 1965, 4)\nAlbum(9, Baltimore, 1978, 4)\nAlbum(10, Here Comes the Sun, 1971, 4)\nAlbum(11, Fodder on My Wings, 1982, 4)\nAlbum(12, Ring Ring, 1973, 2)'


# """
# When: I make a GET request to /artists
# Then: I should get a 200 response and a comma separated string of all artists
# """
# def test_get_all_artists_string(db_connection, test_web_address, web_client):
#     db_connection.seed("seeds/music_web_app_html.sql")

#     get_response = web_client.get("/artists")
#     assert get_response.status_code == 200
#     assert get_response.data.decode('utf-8') == "" \
#         'Pixies, ABBA, Taylor Swift, Nina Simone'



# """
# When: I make a POST request to /artists
# Then: I should get a 200 response and add a new artist to the DB
# """
# def test_post_new_artist(db_connection, test_web_address, web_client):
#     db_connection.seed("seeds/music_web_app_html.sql")

#     post_response = web_client.post('/artists', data={
#     'artist_name': 'Queen', 
#     'genre': 'Rock'
#     })
#     assert post_response.status_code == 200
#     assert post_response.data.decode('utf-8') == ""

#     get_response = web_client.get("/artists")
#     assert get_response.status_code == 200
#     assert get_response.data.decode('utf-8') == "" \
#         'Pixies, ABBA, Taylor Swift, Nina Simone, Queen'


"""
Given an album id
Entering the number in the url (.../albums/1) returns album with id=1 from the DB
"""
def test_show_album_1(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_web_app_html.sql")
    page.goto(f"http://{test_web_address}/albums/1")
    paragraph_tags = page.locator("p")

    expect(paragraph_tags).to_have_text(['\n                Released: 1989\n            '])


"""
The page returned by `GET /albums` should contain a link for each album listed. It should link to `/albums/<id>`, where `<id>` is the corresponding album's id. That page should then show information about the specific album.
"""

def test_click_album_sends_to_page_and_go_back(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_web_app_html.sql")
    page.goto(f"http://{test_web_address}/albums")
    page.click("text='Waterloo'")
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Album: Waterloo")

    paragraph_tag = page.locator("p")
    expect(paragraph_tag).to_have_text("Released: 1974")

    page.click("text='Back to all albums'")
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Albums")


"""
Given an artist id
Entering the number in the url (.../artists/1) returns artist with id=1 from the DB
"""
def test_show_artist_1(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_web_app_html.sql")
    page.goto(f"http://{test_web_address}/artists/1")
    paragraph_tags = page.locator("p")

    expect(paragraph_tags).to_have_text(['\n                Genre: Rock\n            '])


"""
When: I make a GET request to /artists
Then: I should get a 200 response with a list of artists, as html
"""
def test_get_all_artists(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_web_app_html.sql")
    page.goto(f"http://{test_web_address}/artists")

    paragraph_tags = page.locator("p")

    expect(paragraph_tags).to_have_text(['\n                    Pixies\n                ', '\n                    ABBA\n                ', '\n                    Taylor Swift\n                ', '\n                    Nina Simone\n                '])


"""
When we create a new album
We see it in the albums index
"""
def test_create_album(db_connection, page, test_web_address):
    db_connection.seed("seeds/music_web_app_html.sql")
    page.goto(f"http://{test_web_address}/albums")

    # This time we click the link with the text 'Add a new album'
    page.click("text=Add a new album")

    # Then we fill out the field with the name attribute 'title' # Voyage, 2021, 2
    page.fill("input[name='title']", "Voyage")

    # And the field with the name attribute 'release_year'
    page.fill("input[name='release_year']", '2021')

    # And the field with the name attribute 'artist_id'
    page.fill("input[name='artist_id']", '2')

    # Finally we click the button with the text 'Create Album'
    page.click("text=Create Album")

    # Just as before, the virtual browser acts just like a normal browser and
    # goes to the next page without us having to tell it to.

    title_element = page.locator(".t-title")
    expect(title_element).to_have_text("Album: Voyage")

    release_year_element = page.locator(".t-release-year")
    expect(release_year_element).to_have_text("Released: 2021")

"""
If we create a new album without a title or release_year or artist_id
We see an error message
"""
def test_create_album_error(db_connection, page, test_web_address):
    db_connection.seed("seeds/music_web_app_html.sql")
    page.goto(f"http://{test_web_address}/albums")
    page.click("text=Add a new album")
    page.click("text=Create Album")
    errors = page.locator(".t-errors")
    expect(errors).to_have_text("There were errors with your submission: Title can't be blank, Release Year can't be blank, Artist ID can't be blank")


"""
When we create a new artist
We see it in the artists index
"""
def test_create_artist(db_connection, page, test_web_address):
    db_connection.seed("seeds/music_web_app_html.sql")
    page.goto(f"http://{test_web_address}/artists")

    # This time we click the link with the text 'Add a new artist'
    page.click("text=Add a new artist")

    # Then we fill out the field with the name attribute 'artist_name' #Czarface Hip-Hop/Rap - 2015	Every Hero Needs a Villain
    page.fill("input[name='artist_name']", "Czarface")

    # And the field with the name attribute 'genre'
    page.fill("input[name='genre']", 'Hip-Hop/Rap')

    # Finally we click the button with the text 'Create Artist'
    page.click("text=Create Artist")

    # Just as before, the virtual browser acts just like a normal browser and
    # goes to the next page without us having to tell it to.

    artist_name_element = page.locator(".t-artist-name")
    expect(artist_name_element).to_have_text("Artist: Czarface")

    genre_element = page.locator(".t-genre")
    expect(genre_element).to_have_text("Genre: Hip-Hop/Rap")

"""
If we create a new artist without a artist_name or genre
We see an error message
"""
def test_create_artist_error(db_connection, page, test_web_address):
    db_connection.seed("seeds/music_web_app_html.sql")
    page.goto(f"http://{test_web_address}/artists")
    page.click("text=Add a new artist")
    page.click("text=Create Artist")
    errors = page.locator(".t-errors")
    expect(errors).to_have_text("There were errors with your submission: Artist name can't be blank, Genre can't be blank")