import requests
import time
import sys
import threading
import urllib.request

stop_download = False

def download():
    startUrl = input("Paste the video details here: ")

    codeResult = startUrl.find("?wvideo=")

    downloadUrlPart1 = "https://fast.wistia.net/embed/iframe/"
    downloadUrlPart2 = "?videoFoam=true"

    code = ""

    for i in range(codeResult + 8, codeResult + 18):
        code += startUrl[i]

    toDownload = downloadUrlPart1 + code + downloadUrlPart2

    r = requests.get(toDownload)
    page_source = r.text

    codeResult = page_source.find('.bin')

    toDownload =  ""

    for i in range(codeResult - 72, codeResult + 4):
        toDownload += page_source[i]

    name = input("Enter desired video name: ")

    r = requests.get(toDownload, stream = True)
    with open (f'{name}.mp4', 'wb') as f:
        while (stop_download == False):
            try: 
                f.write(r.iter_content(1024))
            except StopIteration:
                break
        
        if (stop_download == True):
            r.close()

if __name__ == '__main__':
    t = threading.Thread(target=download).start()
    time.sleep(5)
    stop_download = True
