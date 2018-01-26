import json


def formatList(aList):
    result = ""
    for str in aList:
        result = result,"", str
        return result

arr = ['汉字','2','3']
dic = {'1':'2','2':'3'}
print json.dumps(",".join(arr))


