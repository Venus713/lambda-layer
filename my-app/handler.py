import json
import xmltodict
import pprint


def hello(event, context):
    body = {
        "message": "Python Function executed successfully!"
    }
    o = xmltodict.parse('<e> <a>text</a> <a>text</a> </e>')
    res = json.dumps(o)
    response = {
            "statusCode": 200,
            "body": json.dumps(body),
            "data": json.dumps(res)
        }
    return response
