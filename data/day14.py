"""
Personal Movie Tracker with JSON
"""
import os
import json

FILENAME = "movies.json"

def load_movies():
    if not os.path.exists(FILENAME):
        return []

    with open(FILENAME,'r',encoding='utf-8') as f:
        return json.load(f)

def save_movie(movies):
    with open(FILENAME,'w',encoding='utf-8') as f:
        json.dump(movies,f,indent=2)

def add_movies(movies):
    title = input('Enter the movie name:').strip().lower()
    if any(movie['title'].lower() == title for movie in movies):
        print('Movie already exists')
        return
    genre = input('Genre: ').strip().lower()
    try:
        rating = float(input('Enter rating(0-10): '))
        if not (0 <= rating <=10):
            raise ValueError
    except ValueError:
        print('Pls enter valid number')
        return
    
    movies.append({'title':title,'genre':genre,'rating':rating})
    save_movie(movies)
    print('Movie added')

def search_movies(movies):
    term = input('Enter the movie title or genre: ').strip().lower()
    results = [
        movie for movie in movies 
        if term in movie['title'].lower() or term in movie['genre'].lower()        
    ]
    if not results:
        print('NO matching results')
        return
    print(f'Found {len(results)} result(S)')

    for movie in results:
        print(f'{movie['title']} -- {movie['genre']} -- {movie['rating']}')

def view_movie(movies):
    if not movies:
        print('No movies in db')
        return

    for movie in movies:
        print(f'{movie['title']} -- {movie['genre']} -- {movie['rating']}')

    print('*' * 30)

def run_movie_db():
    movies= load_movies()
    while 1:
        print('MyMovieDb')
        print('1.add movie')
        print('2.view all movies')
        print('3.search movie')
        print('4.exit')

        choice = input('chosse an option(1-4): ').strip()
        match choice:
            case "1":
                add_movies(movies)
            case "2":
                view_movie(movies)
            case '3':
                search_movies(movies)
            case '4':
                break
            case _:
                print('Enter valid choice')
                

if __name__ == "__main__":
    run_movie_db()