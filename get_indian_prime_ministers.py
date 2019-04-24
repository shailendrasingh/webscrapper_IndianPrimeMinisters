import asyncio
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
from PrimeMinister import PrimeMinister
from Logger import Logger


def getFormerIndianPrimeMinisters(url):
	
	Logger.debug("getFormerIndianPrimeMinisters started")
	rawHtml = simple_get(url)
	Logger.debug("rawHtml found")
	soup = BeautifulSoup(rawHtml, 'html.parser')
	list = soup.find(class_='former-holder clearfix').find_all('li')
	Logger.debug("soup list generated== {0} ".format(len(list)))
	for item in list:
		formerDescription = item.find(class_='former-description')
		pmName = formerDescription.find('h3').contents[0]
		dates = formerDescription.find('span').contents[0]
		description = formerDescription.find('p').contents[0]
		link = formerDescription.find('a').get('href')
		imageLink = item.find('img').get('src')
		pm = PrimeMinister()
		pm.name = pmName
		pm.date = dates
		#Logger.info(pmName+"("+dates+")\n"+description.strip()+"\n"+link+"\n\n")
		Logger.info(pm.name+ pm.date)
	Logger.debug("getFormerIndianPrimeMinisters end")

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
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None


def is_good_response(resp):
    """
    Returns True if the response seems to be HTML, False otherwise.
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200 
            and content_type is not None 
            and content_type.find('html') > -1)


def log_error(e):
    """
    It is always a good idea to log errors. 
    This function just prints them, but you can
    make it do anything.
    """
    Logger.info(e)
	
URL = "https://www.pmindia.gov.in/en/former-prime-ministers/"
getFormerIndianPrimeMinisters(URL)
#loop = asyncio.get_event_loop()
#loop.run_until_complete(getData(URL))