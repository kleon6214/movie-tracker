from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    # Movie list for the Spider-Man franchise
    movies = [
        {
           "title": "Spider-Man",
           "year": 2002,
           "director": "Sam Raimi",
           "cast": ["Tobey Maguire", "Kirsten Dunst", "Willem Dafoe"],
           "rating": 7.3,
           "poster": "https://example.com/spiderman2002.jpg"
        },
        
        {
            "title": "Spider-Man 2",
            "year": 2004,
            "director": "Sam Raimi",
            "cast": ["Tobey Maguire", "Kirsten Dunst", "Alfred Molina"],
            "rating": 7.3,
            "poster": "https://example.com/spiderman2004.jpg"
        },

        {
            "title": "Spider-Man 3",
            "year": 2007,
            "director": "Sam Raimi",
            "cast": ["Tobey Maguire", "Kirsten Dunst", "James Franco"],
            "rating": 6.2,
            "poster": "https://example.com/spiderman2007.jpg"
        },

        {
            "title": "The Amazing Spider-Man",
            "year": 2012,
            "director": "Marc Webb",
            "cast": ["Andrew Garfield", "Emma Stone", "Rhys Ifans"],
            "rating": 7.0,
            "poster": "https://example.com/amazing_spiderman2012.jpg"
        },

        {
            "title": "The Amazing Spider-Man 2",
            "year": 2014,
            "director": "Marc Webb",
            "cast": ["Andrew Garfield", "Emma Stone", "Jamie Foxx"],
            "rating": 6.6,
            "poster": "https://example.com/amazing_spiderman2.jpg"
        },

        {
            "title": "Spider-Man: Homecoming",
            "year": 2017,
            "director": "Jon Watts",
            "cast": ["Tom Holland", "Michael Keaton", "Zendaya"],
            "rating": 7.4,
            "poster": "https://example.com/spiderman_homecoming.jpg"
        },

        {
            "title": "Spider-Man: Far From Home",
            "year": 2019,
            "director": "Jon Watts",
            "cast": ["Tom Holland", "Jake Gyllenhaal", "Zendaya"],
            "rating": 7.5,
            "poster": "https://example.com/spiderman_farfromhome.jpg"
        },

        {   
            "title": "Spider-Man: No Way Home",
            "year": 2021,
            "director": "Jon Watts",
            "cast": ["Tom Holland", "Benedict Cumberbatch", "Zendaya"],
            "rating": 8.3,
            "poster": "https://example.com/spiderman_nowayhome.jpg"
        },
    ]
    return render_template("home.html", movies=movies)

if __name__ == '__main__':
    app.run(debug=True)