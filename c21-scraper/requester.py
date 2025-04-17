

import requests


class Requester():

    def __init__(self):
        self.__requests_tries = 3
        self.timeout = 30
        self.__init_session()

    def __init_session(self):
        """
        Initializes a session object for making requests.

        Returns:
            requests.Session: The session object.

        """
        self.session = requests.Session()

    def get_requests(self, url, headers, proxy=None):
        """
        Sends a GET request to the specified URL using the provided session,
        headers, and proxy.

        Args:
            session (requests.Session): The session object to use for making
            the request.
            url (str): The URL to send the request to.
            headers (dict): The headers to include in the request.
            proxy (dict, optional): The proxy to use for the request. Defaults
            to None.

        Returns:
            requests.Response or None: The response object if the request is
            successful (status code 200),
            otherwise None.

        Raises:
            requests.exceptions.RequestException: If an error occurs while
            making the request.
            requests.exceptions.Timeout: If the request times out.

        """
        for _ in range(self.__requests_tries):
            try:
                response = self.session.get(
                    url,
                    headers=headers,
                    proxies=proxy,
                    timeout=self.timeout
                )
                if response.status_code == 200:
                    return response
            except requests.exceptions.RequestException as e:
                print(e)
            except requests.exceptions.Timeout as e:
                print(e)
        return None
