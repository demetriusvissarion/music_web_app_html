class Artist:
    # We initialise with all of our attributes
    # Each column in the table should have an attribute here
    def __init__(self, id, name, genre, albums = []):
        self.artist_id = id
        self.artist_name = name
        self.genre = genre
        self.albums = albums

    # This method allows our tests to assert that the objects it expects
    # are the objects we made based on the database records.
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    # This method makes it look nicer when we print an Artist
    def __repr__(self):
        if len(self.albums) > 0:
            return f"Artist({self.artist_id}, {self.artist_name}, {self.genre}, {self.albums})"
        return f"Artist({self.artist_id}, {self.artist_name}, {self.genre})"

    # These next two methods will be used by the controller to check if
    # books are valid and if not show errors to the user.
    def is_valid(self):
        if self.artist_name == None or self.artist_name == "":
            return False
        if self.genre == None or self.genre == "":
            return False
        return True
    
    def generate_errors(self):
        errors = []
        if self.artist_name == None or self.artist_name == "":
            errors.append("Artist name can't be blank")
        if self.genre == None or self.genre == "":
            errors.append("Genre can't be blank")
        if len(errors) == 0:
            return None
        else:
            return ", ".join(errors)