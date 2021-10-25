import json
import sys
import requests

json_file = sys.argv[1]
quay_domain = 'https://quay.io'
result = []
with open(json_file) as f:
    data = f.read()
json_data = json.loads(data)
for i in range(len(json_data)):
    repository = json_data[i]['Organisation'] + '/' + json_data[i]['Repository']
    tag = json_data[i]['Tag']
    image_id = []
    image_content = {}
    image_content['Organisation'] = json_data[i]['Organisation']
    image_content['Repository'] = json_data[i]['Repository']
    image_content['Tag'] = json_data[i]['Tag']
    req_endpoint = quay_domain + '/api/v1/repository/' + repository + '/tag/' + tag + '/images?owned=true'
    r = requests.get(req_endpoint)
    if r.status_code != 200:
        image_content['Status'] = 'Response status is non 200'
    else:
        res = r.json()
        if len(res['images']) == 0:
            image_content['Result'] = 'No images with such given information'
        else:
            for j in range(len(res['images'])):
                image_id.append(res['images'][j]['id'])
            for j in range(len(image_id)):
                vulnerabilities = []
                req_endpoint = quay_domain + '/api/v1/repository/' + repository + '/image/' + image_id[j] + '/security?vulnerabilities=true'
                r = requests.get(req_endpoint)
                if r.status_code != 200:
                    image_content['Vulnerabilities'] = 'Response status is non 200'
                else:
                    res = r.json()
                    image_features = res['data']['Layer']['Features']
                    for k in range(len(image_features)):
                        if 'Vulnerabilities' in image_features[k]:
                            vulnerabilities.append(image_features[k])
                    if len(vulnerabilities) > 0:
                        image_content['Vulnerabilities'] = vulnerabilities
                    else:
                        image_content['Vulnerabilities'] = ''
    result.append(image_content)

with open('output.json', 'w') as f:  
    json.dump(result, f, indent=4)
