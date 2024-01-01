import sys

sys.path.insert(0, "app")


from flask import Flask, jsonify, abort, make_response, request
from models import movies

app = Flask(__name__)
app.config["SECRET_KEY"] = "nininini"


@app.route("/api/v1/movies", methods=["GET"])
def movies_list_api_v1():
    def sort_key(list):  # dodanie sortowania
        return list["title"]

    return jsonify(sorted(movies.all(), key=sort_key))


@app.route("/api/v1/movies/<int:movie_id>/", methods=["GET"])
def get_movie(movie_id):
    movie = movies.get(movie_id)
    if not movie:
        abort(404)
    else:
        return jsonify({"movie": movie})


@app.route("/api/v1/movies", methods=["POST"])
def create_movie():
    if not request.json or not "title" in request.json:
        abort(400)
    if movies.all():
        movie_id = movies.all()[-1]["id"] + 1
    else:
        movie_id = 1
    movie = {
        "id": movie_id,
        "title": request.json["title"],
        "opinion": request.json.get("opinion", ""),
        "watched": True,
    }
    movies.create(movie)
    return jsonify({"movie": movie}), 201


@app.route("/api/v1/movies/<int:movie_id>", methods=["DELETE"])
def delete_movie(movie_id):
    result = movies.delete(movie_id)
    print(movie_id)
    if not result:
        abort(404)
    else:
        return jsonify({"result": result})


@app.route("/api/v1/movies/<int:movie_id>", methods=["PUT"])
def update_movie(movie_id):
    movie = movies.get(movie_id)
    if not movie:
        abort(404)
    if not request.json:
        abort(400)
    data = request.json
    if any(
        [
            "title" in data and not isinstance(data.get("title"), str),
            "opinion" in data and not isinstance(data.get("opinion"), str),
            "watched" in data and not isinstance(data.get("watched"), bool),
        ]
    ):
        abort(400)
    movie = {
        "id": movie_id,
        "title": data.get("title", movie["title"]),
        "opinion": data.get("opinion", movie["opinion"]),
        "watched": data.get("watched", movie["watched"]),
    }
    movies.update(movie_id, movie)
    return jsonify({"movie": movie})


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({"error": "Not found", "status_code": 404}), 404)


@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({"error": "Bad request", "status_code": 400}), 400)


if __name__ == "__main__":
    app.run(debug=True)
