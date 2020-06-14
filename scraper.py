from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
from pprint import pprint

def simple_get(url):
    """
    Attempts to get the content at `url` by making an HTTP GET request.
    If the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None.
    """
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None

    except RequestException as e:
        print('Error during requests to {0} : {1}'.format(url, str(e)))
        return None

def is_good_response(resp):
    """
    Returns True if the response seems to be HTML, False otherwise.
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200 
            and content_type is not None 
            and content_type.find('html') > -1)

def get_colorhex(style):
    return str(style).split(':')[1]

def get_title(title):
    return str(title).split('Color palette ')[1]

def get_palettes(url):
    
    raw_html = simple_get(str(url))
    html = BeautifulSoup(raw_html, 'html.parser')
    
    palettes = {}
    
    container = html.find_all('div', {'class': 'palettecontainerlist'})
    
    for i in range(len(container)):
        title = container[i].find('a', href=True).get('title')
        hex_colors = []
        color_set = container[i].find_all('div', {'class': 'palettecolordiv'})
        for ii in color_set:
            style = ii.get('style')
            hex_colors.append(get_colorhex(style))            
        palettes[get_title(title)] = hex_colors
    
    return palettes
        
        
    
if __name__ == "__main__":
    print(get_palettes('https://www.color-hex.com/color-palettes/?page=2')['Buddy 2'])
    # raw_html = simple_get('https://www.color-hex.com/color-palettes/popular.php')
    
    # html = BeautifulSoup(raw_html, 'html.parser')
    # c = html.find_all('div', {'class': 'palettecontainerlist'})
    
    # for x in c:
    #     b = x.find('a', href=True)
    #     a = x.find_all('div', {'class': 'palettecolordiv'})
    
    # print(get_colorhex(a[0].get('style')))
    # pprint(a)
   