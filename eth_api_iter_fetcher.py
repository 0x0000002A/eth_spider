from utils import request as request_util
from utils.filter import ImplFilter
from utils.file_handler import *

# local settings
class LocalSettings:
    api_main_url = "http://api.etherscan.io/"
    api_type = "api?module=account&action=txlist"
    # todo to be more universal address input
    api_address = "&address=0xddbd2b932c763ba5b1b7ae3b362eac3e8d40121a"
    api_address_sep = ","
    api_sort = "&startblock=0&endblock=99999999&sort=asc"
    default_elements = []

def demo_read_url():
    request = request_util.request_handle()
    raw_response = request.read_url("http://api.etherscan.io/api?module=account&action=txlist&address=0xddbd2b932c763ba5b1b7ae3b362eac3e8d40121a&startblock=0&endblock=99999999&sort=asc")
    the_page = raw_response.read()
    print(the_page)

def address_list_getter():
    address_list = []
    #todo
    return address_list

def eth_api_fetcher():
    api_url = LocalSettings.api_main_url + LocalSettings.api_type +\
              LocalSettings.api_address + LocalSettings.api_sort
    request = request_util.request_handle()
    request.read_url(api_url)
    page_content_filter = ImplFilter(request.page_content)
    page_content_filter.selected_elements = LocalSettings.default_elements
    page_content_filter.eth_api_reponse_filter()
    # todo move to storage part
    page_content_filter.eth_api_response_storage_filter()
    return page_content_filter.file_content

def eth_api_storage(file_content):
    file_handler = FileHandler
    # todo to make directory & file name rules
    file_handler.__init__(file_handler,"D:\\","test")
    file_handler.file_content = file_content
    file_handler.file_open_write(file_handler)
    file_handler.file_close(file_handler)

if __name__ == '__main__':
    result = eth_api_fetcher()
    eth_api_storage(result)