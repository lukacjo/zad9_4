from collections import namedtuple
from flask import (
    Flask,
    request,
    render_template,
    redirect,
    url_for,
    jsonify,
    abort,
    make_response,
)
from forms import MovieForm
from models import movies

app = Flask(__name__)
app.config["SECRET_KEY"] = "nininini"


@app.route("/movies/", methods=["GET", "POST"])
def movies_list():
    form = MovieForm()
    error = ""
    if request.method == "POST":
        if form.validate_on_submit():
            movies.create(form.data)
            movies.save_all()
        return redirect(url_for("movies_list"))
    return render_template("movies.html", form=form, movies=movies.all(), error=error)


@app.route("/movies/<int:movie_id>/", methods=["GET", "POST"])
def todo_details(movie_id):
    movie = movies.get(movie_id)
    form = MovieForm(data=movie)

    if request.method == "POST":
        if form.validate_on_submit():
            movies.update(movie_id, form.data)
        return redirect(url_for("movies_list"))
    return render_template("movie.html", form=form, movie_id=movie_id)


if __name__ == "__main__":
    app.run(debug=True)
