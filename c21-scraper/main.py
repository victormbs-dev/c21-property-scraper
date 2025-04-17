

import century_scraper


def main():
    """
    Main function to scrape data from the Century 21 Mexico website.
    This function initializes the scraping process by setting up parameters
    such as the starting index, limit, property type, and user agent. It uses
    the `Century21Scraper` class to retrieve URLs, scrape data from the pages,
    and export the collected data to a JSON file.
    Returns:
        dict: A dictionary containing the scraped data exported to a JSON file.
    """

    start_ = 0
    limit_ = 5
    type_ = "terreno"
    csv_file = 'urls.csv'

    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:136.0) ' \
        'Gecko/20100101 Firefox/136.0'
    url_base = 'https://century21mexico.com'

    scraper = century_scraper.Century21Scraper()
    url_list = scraper.get_urls(csv_file, url_base, start_, limit_, type_)
    all_data = scraper.get_all_pages_data(url_list, scraper, user_agent)
    json_data = scraper.export_to_json(all_data, start_, limit_, type_)
    print("Data exported to JSON file:" +
          f"century_data_{type_}_{start_}-{limit_}.json")

    return json_data


if __name__ == "__main__":
    main()
