import requests as req
import sys

if len(sys.argv) > 0:
    url = sys.argv[1]
    istek = req.post("https://git.io/create", data={"url": url})
    if istek.status_code == 200:
        print(f"https://git.io/{istek.text}")
    elif istek.status_code == 500:
        print(f"Invalid link. {istek.text}")
    else:
        print(f"{istek.text}")