import requests
from bs4 import BeautifulSoup
import json

def scrape_imdb_page(url):
    # Intestazione per far sembrare che la richiesta provenga da un browser
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    # Invia una richiesta GET al sito con l'intestazione
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Verifica che la richiesta sia stata completata con successo

    # Analizza il contenuto HTML della pagina
    soup = BeautifulSoup(response.text, 'html.parser')

    # Trova tutti i contenitori dei film nella pagina
    movies = soup.find_all('div', class_='ipc-metadata-list-summary-item__c')

    # Verifica se sono stati trovati i contenitori dei film
    if not movies:
        print("Nessun film trovato. Verifica la struttura HTML della pagina.")
        return []

    # Lista per salvare i risultati
    movie_list = []

    # Estrazione delle informazioni di ogni film
    for movie in movies:
        name_tag = movie.find('h3', class_='ipc-title__text')
        metadata_tags = movie.find_all('span', class_='sc-b189961a-8 kLaxqf dli-title-metadata-item')
        rating_tag = movie.find('span', class_='ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating')
        description_tag = movie.find('div', class_='ipc-html-content-inner-div')
        
        
        if name_tag and metadata_tags and rating_tag:
            nome = name_tag.text.strip()[4:]           # Titolo del film rimuove i primi 4 caratteri che sarebbe l'elenco puntato
            anno = metadata_tags[0].text.strip()       # Anno del film
            durata = metadata_tags[1].text.strip()   # Durata del film
            rating = rating_tag.text.strip()           # Rating del film
            descrizione = description_tag.text.strip() if description_tag else "Nessuna descrizione disponibile" # Descrizione del film
            movie_list.append({'title': nome, 'year': anno, 'duration': durata, 'rating': rating, 'description': descrizione})

    return movie_list
