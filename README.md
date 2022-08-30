# m3u8_URL_Breaker
Simple python code to extract .m3u8 file URL from web page.

### Usage
Run the python code in terminal. `python m3u8_url_Breaker.py`  
Paste your streaming web page link. eg: Youtue live  
It will then grab the page source and try to find a .m3u8 url. Copy the extracted m3u8 url and now you can use it in your m3u playlist or streaming app.

##### Shell script
You can simply do this by a single command in linux terminal using *curl* and *grep*.  
Here is a simple shell script for this. Just run the *m3u8.sh* script:
```
chmod +x m3u8.sh
./m3u8.sh <URL>
```
