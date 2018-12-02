import requests

def download(url, file_name):
    # open in binary mode
    with open(file_name, "wb") as file:
        # get request
        response = requests.get(url)
        # write to file
        file.write(response.content)

IMAGE_FORMATS = ("image/png", "image/jpeg", "image/jpg")

with open("URL_list.txt") as file:

    # Making a list where each element is a URL-line from opened file.
    # Each element except the last one contains '\n' in the end.

    raw_list_of_urls = file.readlines()
    clear_list_of_urls = []

    # Getting rid of '\n'
    for i in raw_list_of_urls:
        clear_list_of_urls.append(i.replace('\n',''))

    for url in clear_list_of_urls:
        r = requests.get(url)

        # checking if URL is an image and its size is less or equal to 5 Mb. If yes - downloading the image
        if r.headers["Content-Type"] in IMAGE_FORMATS and int(r.headers["Content-Length"]) <= 5242880:
            download(url, input("file name: "))
