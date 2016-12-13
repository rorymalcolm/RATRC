from cement.core import foundation
import validators
import ra_resale_checker_utils as ra_check
import time

app = foundation.CementApp('ra_resale_checker')

app.setup()

app.args.add_argument('-u', action='store', dest='url',
                      help='URL for checking')

app.run()


def url_method(url_for_input):
    global url
    url = url_for_input


def validate_url(url_for_val):
    return validators.url(url_for_val)

url = app.pargs.url
if validate_url(url):
    response = ra_check.get_ra_page(url)
    is_ticket = True
    while is_ticket:
        if ra_check.check_ra_page(response):
            print('***** RA TICKET FOR SALE *****')
            is_ticket = False
            break
        time.sleep(20)
    input()
app.close()
