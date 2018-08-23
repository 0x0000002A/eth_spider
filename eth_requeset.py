import urllib2
response = urllib2.urlopen("http://api.etherscan.io/api?module=account&action=txlist&address=0xddbd2b932c763ba5b1b7ae3b362eac3e8d40121a&startblock=0&endblock=99999999&sort=asc")

the_page = response.read()  
print the_page
