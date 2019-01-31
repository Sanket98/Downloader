# Downloader
```
import requests as req
import os


class Downloader:
    'Download http files'
    def __init__(self,url,file_name):
        self.url=url
        self.file_name=file_name
        self.req=req.get(url,stream=True)
        self.size='% .2f mb'%(int(self.req.headers['Content-Length'])/(1000**2))
        self.format=self.req.headers['Content-Type'].split('/')[-1]
        print('file_name : {}.{} \nfile size : {}'.format(self.file_name,self.format,self.size))
    
    def download(self):
        if(not os.path.exists('downloaded_files')):
            os.mkdir('downloaded_files')
        with open('downloaded_files/ {}.{}'.format(self.file_name,self.format),'wb') as f:
            for chunk in self.req.iter_content(chunk_size=1024):
                if(chunk):
                    f.write(chunk)
```                    
