import requests

url = 'http://www.blpack.com/post.php'

form_data = {
    'usrname': '342522490',
    'usrpass': '553156',
    'docinfo': 'https://wenku.baidu.com/view/3fc852b4d4bbfd0a79563c1ec5da50e2524dd1d7.html',
    'taskid': 'up_down_doc1'
}

requests.post(url, data=form_data)