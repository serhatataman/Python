
# Example file for retrieving data from the internet

import urllib.request


def main():
    # open a connection to a URL using urllib
    webUrl = urllib.request.urlopen("http://www.google.com")

    # get the result code and print it
    print("result code: " + str(webUrl.getcode()))

    # read the data from the URL and print it
    data = webUrl.read()
    print(data)


if __name__ == "__main__":
    main()

