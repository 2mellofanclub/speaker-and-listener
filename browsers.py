import pychrome, time, os
from selenium import webdriver
from urllib.parse import urlparse, parse_qs



# the pychrome browser will use this
def handle_request_event(*args, **kwargs):
    request_url = kwargs.get('request').get('url')
    request_query_string = parse_qs(urlparse(request_url).query)
    # request_post_data = kwargs.get('request').get('postData')
    #############################################
    #                                           #
    #  here's where you pick apart the request  #
    #                                           #
    #############################################
    print(f"url: {urlparse(request_url).path}")
    print(f"query string: {request_query_string}")

# this selenium browser will do the web browsing
options = webdriver.ChromeOptions()
options.add_argument("--remote-debugging-port=7777")
options.add_argument("--remote-allow-origins=http://localhost:7777")
options.add_argument("--ignore-certificate-errors")
driver = webdriver.Chrome(options=options)

# this pychrome browser will listen in the background
dev_tools = pychrome.Browser(url="http://localhost:7777")
tab = dev_tools.list_tab()[0]
tab.start()
tab.call_method("Network.enable", _timeout=20)
tab.set_listener("Network.requestWillBeSent", handle_request_event)



with open("testpages.txt", encoding="utf-8") as pages:
    print("\n\n")
    for page in pages:
        try:
            print(f"Visiting {page}")
            driver.get(page)
            # couple seconds for requests
            time.sleep(2)
        except Exception as err:
            print(err)
print("All done.")
# wont go clean
try:
    tab.stop()
except:
    pass
driver.quit()

