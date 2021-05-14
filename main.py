from google_images_search import GoogleImagesSearch

# using your custom progressbar function
def my_progressbar(url, progress):
    print(url + ' ' + progress + '#')

# you can provide API key and CX using arguments,
# or you can set environment variables: GCS_DEVELOPER_KEY, GCS_CX
gis = GoogleImagesSearch('AIzaSyCsTj4ORxL98_xtyWN7yyXpxnbwCGdQD-I', '864ad66b1230b9dd5')
Searchindex = []


keywords = open('keywords.txt', 'r')

for x in keywords:
    Searchindex.append(x.rstrip('\n'))

#enter search indexes here


search_params = {
    'q': '',
    'num': 300,
    'fileType': 'jpg',
    'imgDominantColor': 'blue'
}

for index in list(Searchindex):
    search_params['q'] = index
    try:
        gis.search(search_params=search_params, path_to_dir=index,progressbar_fn=my_progressbar)
        Searchindex.pop(index)
    except:
        continue
