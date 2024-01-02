import json
import secrets


class Movies:
    def __init__(self):
        try:
            with open("movies.json", "r") as f:
                self.movies = json.load(f)
        except FileNotFoundError:
            self.movies = []

    def all(self):
        return [
            {key: value for key, value in movie.items() if key != "csrf_token"}
            for movie in self.movies
        ]

    def get(self, id):
        movie = [movie for movie in self.all() if movie["id"] == id]
        if movie:
            return movie[0]
        return []

    def create(self, data):
        data["csrf_token"] = secrets.token_urlsafe(91)
        self.movies.append(data)
        self.save_all()

    def save_all(self):
        with open("movies.json", "w") as f:
            json.dump(self.movies, f)

    def update(self, id, data):
        movie = self.get(id)
        if movie:
            index = self.movies.index(movie)
            self.movies[index] = data
            self.save_all()
            return True
        return False

    def delete(self, id):
        movie = self.get(id)
        if movie:
            self.movies.remove(movie)
            self.save_all()
            return True
        return False


movies = Movies()
