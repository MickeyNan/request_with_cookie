import httplib
import urlparse

def request(url, cookie=''):
    ret = urlparse.urlparse(url)    # Parse input URL
    if ret.scheme == 'http':
        conn = httplib.HTTPConnection(ret.netloc)
    elif ret.scheme == 'https':
        conn = httplib.HTTPSConnection(ret.netloc)
        
    url = ret.path
    if ret.query: url += '?' + ret.query
    if ret.fragment: url += '#' + ret.fragment
    if not url: url = '/'
    
    conn.request(method='GET', url=url , headers={'Cookie': cookie})
    return conn.getresponse()

if __name__ == '__main__':
    direct_count = 0
    refund_count = 0
    count = 0
    cookie_str = ''
    url = ''
    while(count < 10000):
    	html_doc = request(url, cookie_str).read()
   	
	import re
    	direct = re.search('<input checked class="mt kv-v" name="direction" type="radio" value="2"/>', html_doc, re.IGNORECASE)
   	refund = re.search('<input checked class="mt kv-v" name="direction" type="radio" value="0"/>', html_doc, re.IGNORECASE)
    	if direct:
    		direct_count += 1
   	if refund:
    		refund_count += 1
    	count += 1

    print direct_count

