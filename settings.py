REQUEST_HEADER_AGENT_COMPONENTS = {
    "CHROME":
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 \
    (KHTML, like Gecko) Chrome/45.0.1271.64 Safari/537.11" ,
    "SAFARI":
    "Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) \
    AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
    "FIREFOX":
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; zh-CN; rv:1.9.2.15) \
    Gecko/20110303 Firefox/32.6.15",
    "IE":
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)",
}

REQUEST_CONNECTION = "keep-alive"

REQUEST_USERAGENT_ID = "CHROME"

REQUEST_USERAGENT = REQUEST_HEADER_AGENT_COMPONENTS[REQUEST_USERAGENT_ID]

DEFAULT_WRITE_FILE_TYPE = "csv"

STORAGE_DIRECTORY = "./data"

SUB_STORAGE_DOWNALOADS_DIR = STORAGE_DIRECTORY + "/downloads"

SUB_STORAGE_INTERMIDIA_DIR = STORAGE_DIRECTORY + "/intermedia"

SUB_STORAGE_PRODUCT_DIR = STORAGE_DIRECTORY + "/product"

LINESEP = "\n"



