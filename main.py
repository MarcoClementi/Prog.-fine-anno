from scraper import scrape_imdb_page

def filtro_anno(movie_list, anno=None, durata=None):
    filtered_movies = movie_list

    if anno:
        filtered_movies = [movie for movie in filtered_movies if movie['year'] == anno]

    return filtered_movies

def main():
    url = 'https://www.imdb.com/search/title/?title_type=feature&sort=num_votes,desc'
    movies = scrape_imdb_page(url)
    if not movies:
        print("Nessun dato estratto. Verifica i selettori utilizzati.")
    else:
        anno = input("Inserisci l'anno del film (opzionale): ").strip()

        filtered_movies = filtro_anno(movies, anno)

        if filtered_movies:
            print("\nEcco una lista di film che corrispondono ai criteri specificati:")
            for idx, movie in enumerate(filtered_movies, start=1):
                print(f"Nome - {movie['title']}")
                print(f"Anno - {movie['year']}")
                print(f"Durata - {movie['duration']}")
                print(f"Rating - {movie['rating']}")
                print(f"Descrizione - {movie['description']}\n")
        else:
            print("Nessun film trovato che corrisponde ai criteri specificati.")

if __name__ == '__main__':
    main()

