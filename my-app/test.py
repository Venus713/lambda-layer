import xmltodict, json

o = xmltodict.parse('<e> <a>text</a> <a>text</a> </e>')
res = json.dumps(o) # '{"e": {"a": ["text", "text"]}}'
print(res)