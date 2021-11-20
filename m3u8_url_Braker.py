import requests

try:
    page_source = requests.get(input("Enter the streaming web page url\n"))
    page_source = page_source.text
except:
    print("Invalid urld")
    input()
    quit()

m = page_source.find(".m3u8")

if m == -1:
    print("No m3u8 url found")
else:
    url = ""
    while True:
        m -= 1
        if page_source[m] == "\"" :
            break

        url += page_source[m]

        if m == 0:
            break

    url = url[::-1]+".m3u8"

    print("m3u8 url is :\n" + url)

input()