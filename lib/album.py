class Album:
    def __init__(self, id, title, release_year, artist_id):
        self.album_id = id
        self.title = title
        self.release_year = release_year
        self.artist_id = artist_id

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f"Album({self.album_id}, {self.title}, {self.release_year}, {self.artist_id})"
    
    # These next two methods will be used by the controller to check if
    # books are valid and if not show errors to the user.
    def is_valid(self):
        if self.title == None or self.title == "":
            return False
        if self.release_year == None or self.release_year == "":
            return False
        if self.artist_id == None or self.artist_id == "":
            return False
        return True
    
    def generate_errors(self):
        errors = []
        if self.title == None or self.title == "":
            errors.append("Title can't be blank")
        if self.release_year == None or self.release_year == "":
            errors.append("Release Year can't be blank")
        if self.artist_id == None or self.artist_id == "":
            errors.append("Artist ID can't be blank")
        if len(errors) == 0:
            return None
        else:
            return ", ".join(errors)