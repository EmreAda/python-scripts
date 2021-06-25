# -*- encoding: utf-8 -*-
import sys
import requests
import json


def getArticleData():
    """
    $ python wikipedia.py [random|"<araştırılacak argüman">]
    """
    if sys.argv[1] == "random":
        randomistek = requests.get("https://tr.wikipedia.org/w/api.php?action=query&list=random&rnnamespace=0&rnlimit=2&format=json")
        randomjsondata = json.loads(randomistek.text.encode().decode("unicode-escape"))["query"]["random"][0]
        id, ns, title = randomjsondata["id"], randomjsondata["ns"], randomjsondata["title"].replace(" ", "_")
        getarticledata = requests.get("https://tr.wikipedia.org/w/api.php?action=query&prop=extracts&exsentences=10&exlimit=1&titles=" + title + "&explaintext=1&formatversion=2&format=json")
        articlejsondata = json.loads(getarticledata.text)["query"]["pages"][0]["extract"]
        print(f"{title.replace('_', ' ')} \n" + articlejsondata.split("\n")[0])
    elif sys.argv[1] != "random":
        getarticledata = requests.get("https://tr.wikipedia.org/w/api.php?action=query&prop=extracts&exsentences=10&exlimit=1&titles=" + sys.argv[1].replace(" ", "_") + "&explaintext=1&formatversion=2&format=json")
        try:
            articlejsondata = json.loads(getarticledata.text)["query"]["pages"][0]["extract"]
            print(f"{sys.argv[1]} \n" + articlejsondata.split("\n")[0])
        except KeyError:
            print(f"Aratılan argüman tr.wikipedi.org'da bulunamadı. {sys.argv[1]}")

    else:
        print(f"Eksik argüman. Doğru kullanım: {getArticleData.__doc__}")

getArticleData()
