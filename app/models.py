import json
import secrets


class Movies:
    def __init__(self):
        try:
            with open("movies.json", "r") as f:
                self.movies = json.load(f)
        except FileNotFoundError:
            self.movies = []
        self.last_id = self.calculate_last_id()

    def calculate_last_id(self):
        return max([0] + [movie.get("id", 0) for movie in self.movies])

    def all(self):
        return [
            {key: value for key, value in movie.items() if key != "csrf_token"}
            for movie in self.movies
        ]

    def get(self, id):
        for movie in self.all():
            movie_id = movie.get("id")
            if movie_id is not None and movie_id == id:
                return movie
        return []

    def create(self, data):
        self.last_id += 1
        data["id"] = self.last_id
        data["csrf_token"] = secrets.token_urlsafe(91)
        self.movies.append(data)
        self.save_all()

    def save_all(self):
        with open("movies.json", "w") as f:
            json.dump(self.movies, f)

    def update(self, id, data):
        movie = self.get(id)
        if movie and "id" in movie:
            index = next(
                (i for i, m in enumerate(self.movies) if m.get("id") == id), None
            )
            if index is not None:
                data["id"] = id
                self.movies[index] = data
                self.save_all()
                return True
        return False

    def delete(self, id):
        movie = self.get(id)
        if movie:
            index = next((i for i, m in enumerate(self.movies) if m["id"] == id), None)
            if index is not None:
                del self.movies[index]
                self.save_all()
                return True
        return False


movies = Movies()
