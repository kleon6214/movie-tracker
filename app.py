from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    movies = [
        "Spider-Man (2002)",
        "Spider-Man 2 (2004)",
        "Spider-Man 3 (2007)",
        "The Amazing Spider-Man (2012)",
        "The Amazing Spider-Man 2 (2014)",
        "Spider-Man: Homecoming (2017)",
        "Spider-Man: Into the Spider-Verse (2018)",
        "Spider-Man: Far From Home (2019)",
        "Spider-Man: No Way Home (2021)",
        "Spider-Man: Across the Spider-Verse (2023)"
    ]
    return render_template("home.html", movies=movies)

if __name__ == '__main__':
    app.run(debug=True)