
import time
import requests
import json


def run():
    print("new round")
#     payload = json.dumps({"ref": "main"})
    key = "iYCKxRNPAeR8"
    token = "ghp_{}".format(key)
    header = {'Authorization': 'token {}1t9ZBL9H4v1FfvPXA54Ujfh7'.format(token),
              "Accept": "application/vnd.github.v3+json"}
#     name_list = ['files_rename','E5api','wzry-skins']
    url_list = [r'https://api.github.com/repos/oldboyprq/E5api/actions/workflows/Task.yml/dispatches',]
#                 r'https://api.github.com/repos/oldboyprq/files_rename/actions/workflows/Task.yml/dispatches',
#                 r'https://api.github.com/repos/oldboyprq/wzry-skins/actions/workflows/Task.yml/dispatches'
    for url in url_list:
#         if url_list.index(url) > 0:
        payload = json.dumps({"ref": "master"})
        r = requests.post(url, data=payload, headers=header)
        print("status_code:",r.status_code)
#         print("{} run once.".format(name_list[url_list.index(url)]))


count = 0
while count < 10:
    run()
    time.sleep(600)
    count += 1
