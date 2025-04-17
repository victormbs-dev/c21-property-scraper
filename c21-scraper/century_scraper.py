

import pandas as pd
import json
import requester


class Century21Scraper(requester.Requester):
    """ Century21Scraper
    A class for scraping property data from the Century 21 Mexico website.
    This class inherits from the `requester.Requester` class and provides
    methods for generating URLs, fetching data from webpages, and exporting
    the scraped data to JSON files.
    Methods:
        __init__():
            Initializes the Century21Scraper instance by calling the parent
            class constructor.
        get_urls(csv_data, url_base, start, limit, type_):
        get_urls_not_valids(url):
        get_data_page(requester, url_page, user_agent):
        get_all_pages_data(url_list, req, user_agent):
        export_to_json(data_all_pages, star, end, type_p):
            Exports the scraped data to a JSON file with a specific filename
            format.
    Attributes:
        None """

    def __init__(self):
        super().__init__()

    def get_urls(self, csv_data, url_base, start, limit, type_):
        """
        Generates a list of URLs based on filtered data from a CSV file.
        Args:
            csv_data (str): Path to the CSV file containing property data.
            url_base (str): Base URL to prepend to the property-specific URLs.
            start (int): Starting index for slicing the filtered data.
            limit (int): Ending index for slicing the filtered data.
            type_ (str): Property type to filter the data by.
        Returns:
            list: A list of complete URLs for the filtered properties.
        """

        df = pd.read_csv(csv_data)
        df_filtered = df[df['tipoPropiedad'] == type_]
        subset = df_filtered.iloc[start:limit]
        url_pages = [f'{url_base}{url}' for url in
                     subset['urlCorrectaPropiedad']]

        return url_pages

    def get_urls_not_valids(self, url):
        """
        Collects and returns a list of URLs that are considered not valid.
        Args:
            url (str): The URL to be marked as not valid.
        Returns:
            list: A list containing the provided URL as not valid.
        """

        urls_not_valids = []
        urls_not_valids.append(url)

        return urls_not_valids

    def get_data_page(self, requester, url_page, user_agent):
        """
        Fetches and processes data from a given webpage using the provided
        requester and user agent.
        Args:
            requester (object): An object responsible for making HTTP requests.
                                It must have a `get_requests` method.
            url_page (str): The URL of the webpage to fetch data from.
            user_agent (str): The User-Agent string to include in the request
            headers.
        Returns:
            dict: A dictionary containing the JSON data from the webpage if
            the request is successful.
                  Returns None if the request fails or the response is invalid.
        Side Effects:
            Appends invalid URLs to the `urls_not_valids` list if the request
            fails.
        Notes:
            - The function makes two requests to the given URL: one for the
            main page and another
              for the JSON data by appending `?json=true` to the URL.
            - The function assumes the response contains a JSON object with a
            'results' key.
        """

        urls_not_valids = []

        headers_page = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Encoding': 'gzip, deflate, br, zstd',
            'Accept-Language': 'en-US,en;q=0.5',
            'Connection': 'keep-alive',
            'DNT': '1',
            'Host': 'century21mexico.com',
            'Priority': 'u=0, i',
            'Referer': url_page,
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-GPC': '1',
            'TE': 'trailers',
            'User-Agent': user_agent,
        }

        response = requester.get_requests(url_page, headers_page)

        if response is not None and response.status_code == 200:
            response_url = requester.get_requests(f"{url_page}?json=true",
                                                  headers_page)
            data_page = response_url.json()
            print(url_page)
            return data_page
        else:
            urls_not_valids.append(url_page)

        response = requester.get_requests(url_page, headers_page)
        data_page = response.json()
        data = data_page.get('results')

        return data

    def get_all_pages_data(self, url_list, req, user_agent):
        """
        Retrieves data from all pages in the provided URL list.
        This method iterates through a list of URLs, fetching data from each
        page using the `get_data_page` method.
        Args:
            url_list (list): A list of URLs to scrape data from.
            req (requests.Session): A requests session object for making HTTP
            requests.
            user_agent (str): The user agent string to include in the request
            headers.
        Returns:
            list: A list containing the data retrieved from each page.
        """

        all_data = [self.get_data_page(req, link, user_agent) for link in
                    url_list]
        return all_data

    def export_to_json(self, data_all_pages, star, end, type_p):
        """
        Exports the scraped data to a JSON file.
        Args:
            data_all_pages (list): A list containing the data from all pages.
            star (int): The starting index or identifier for the data being
            exported.
            end (int): The ending index or identifier for the data being
            exported.
            type_p (str): A string representing the type or category of the
            data.
        The JSON file will be saved with a filename in the format:
        'century_data_<type_p>_<star>-<end>.json', and the data will be
        formatted with an indentation of 4 spaces.
        """

        with open(f'century_data_{type_p}_{star}-{end}.json',
                  "w") as json_file:
            json.dump(data_all_pages, json_file, indent=4)
