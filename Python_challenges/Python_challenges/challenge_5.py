import urllib.request
from timeit import default_timer as timer

def main():
    
    start = timer()
    url = 'https://www.google.com'
    
    response = urllib.request.urlopen(url)
    
    webContent = response.read()

    f = open('web-download.html', 'wb')
    f.write(webContent)
    f.close
    print('elapsed time: ', timer() - start, ' seconds')
