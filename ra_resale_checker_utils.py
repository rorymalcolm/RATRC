import urllib.request


def get_ra_page(url):
    response = urllib.request.urlopen(url)
    return response.read()


def check_ra_page(page_for_check):
    if 'onsale' in str(page_for_check):
        return True
    else:
        return False
