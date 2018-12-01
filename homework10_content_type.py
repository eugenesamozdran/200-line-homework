import requests

def download(url, file_name):
    # open in binary mode
    with open(file_name, "wb") as file:
        # get request
        response = requests.get(url)
        # write to file
        file.write(response.content)

IMAGE_FORMATS = ("image/png", "image/jpeg", "image/jpg")

file = open("URL_list.txt", "r")

# Making a list where each element is a URL-line from opened file.
# Each element except the last one contains '\n' in the end.

raw_list_of_urls = file.readlines()
clear_list_of_urls = []

# Getting rid of '\n'
for i in raw_list_of_urls:
    clear_list_of_urls.append(i.replace('\n',''))

for url in clear_list_of_urls:
    r = requests.get(url)
    if r.headers["Content-Type"] in IMAGE_FORMATS:
        download(url, input("file name: "))

file.close()
