"""All the functions related to section_1 are written here"""

from bs4 import BeautifulSoup
import requests
import time
import re
import csv


def _request_delayed(seconds: float, url: str) -> requests.Response:
    """
    Sends a request with pre-delay and return response
    :param seconds: Number of seconds to delay
    :param url: Url to hit
    :return:
    """
    time.sleep(seconds)
    return requests.get(url)


def _get_top_links(count: int = 5):
    """
    Scraps and parses absolute links for all n movies.
    :param count: Count of top movies
    :return:
    """
    base_url = 'http://www.imdb.com'
    top_movies_url = f'{base_url}/chart/top'
    response = _request_delayed(0.0, top_movies_url)
    soup = BeautifulSoup(response.text, 'lxml')
    mov_links = [a.attrs.get('href') for a in soup.select(selector='td.titleColumn a', limit=count)]

    return [f'{base_url}{link}' for link in mov_links]


def _scrap_movie_data(response: requests.Response):
    """
    Scrap movies data from response. Where as movies data contains:
    - Title
    - Total Number of Ratings
    - Rating Score
    - Genre
    - Budget
    - Gross USA
    :param response: Response of each page
    :return:
    """
    soup = BeautifulSoup(response.text, 'lxml')

    title = soup.find("div", class_="title_wrapper").findChild("h1").text.strip()
    print(f'Getting data for {title}')

    # Convert currency format to number
    total_ratings = int(''.join(re.findall(r'\d', soup.find("span", itemprop="ratingCount").text)))
    rating_score = float(soup.find("span", itemprop="ratingValue").text)

    genre = soup.find("h4", string="Genres:").parent.text.split(':')[1].strip().split('\xa0|\n ')

    # Convert currency format to number
    try:
        budget = int(''.join(re.findall(r'\d+', soup.find("h4", string="Budget:").parent.text)))
    except AttributeError:
        print(f'No budget found for the current movie: {title}, fallback to zero')
        budget = 0
    try:
        gross = int(''.join(re.findall(r'\d+', soup.find("h4", string="Gross USA:").parent.text)))
    except AttributeError:
        print(f'No Gross USA: for this: {title}, fallback to Cumulative Worldwide Gross:')
        gross = int(''.join(re.findall(r'\d+', soup.find("h4", string="Cumulative Worldwide Gross:")
                                       .parent.text)))
    return {'title': title, 'total_ratings': total_ratings, 'rating_score': rating_score,
            'genre': genre, 'budget': budget, 'gross': gross}


def _get_data_for_movies(movie_links: list) -> list:
    """
    Get data for each movie
    :param movie_links: Links of movies
    :return:
    """
    d = []
    for i in range(0, len(movie_links)):
        # First request not delayed, then every request is delayed with incremental scheme and won't
        # exceed 3 seconds
        print(movie_links[i])
        d.append(_scrap_movie_data(_request_delayed(min(i, 3), movie_links[i])))

    return d


def _write_to_csv(file_name: str, data: list):
    """
    Writes movies data to csv file
    :param file_name Name of the file
    :param data: Data to be written in csv file
    :return:
    """
    with open(file_name, 'w') as file:
        csv_writer = csv.writer(file)
        # Write Header
        csv_writer.writerow(['Title', 'Total Ratings', 'Rating Score', 'Genre', 'Budget',
                             'Gross USA'])
        for row in data:
            csv_writer.writerow([row['title'], row['total_ratings'], row['rating_score'],
                                 row['genre'], row['budget'], row['gross']])


def collect(count: int, csv_filename: str):
    """
    Entry point for section 1
    :param count: Count of first N movies to get data
    :param csv_filename Filename of csv file
    :return:
    """
    # Get links of top n movies
    links = _get_top_links(count=count)

    # Get data for each movie
    data = _get_data_for_movies(links)

    # Write data to csv
    _write_to_csv(csv_filename, data)