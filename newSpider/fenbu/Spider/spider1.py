import requests
import re
def getCntent(url):
    # print(url)
    print("111111111111")
    reg = '<span property="v:itemreviewed">(.*?)</span>'
    response = requests.get(url)
    response = response.text
    result = re.findall(reg , response)
    print(result)