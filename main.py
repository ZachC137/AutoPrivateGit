from requests import Session
from bs4 import BeautifulSoup


blacklist = [
    "repo1",
    "repo2"
]
username = "ZachC137"
page = "2"


s = Session()

cookies = {

}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://github.com',
    'priority': 'u=0, i',
    'referer': 'https://github.com/'+username+'/reponame/settings',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}



s.cookies.update(cookies)
s.headers.update(headers)

repos = s.get(f'https://github.com/{username}?page='+page+'&tab=repositories').text
soup = BeautifulSoup(repos, 'html.parser')

rlist = soup.find(id='user-repositories-list')
repos = rlist.find_all('li')

for repo in repos:
    
    repo_name = repo.find('a').text.strip()
    repo_status = repo.find('span', class_='Label').text.strip()
    
    if repo_name in blacklist:
        continue
    if repo_status == 'Private':
        continue
    
    try:
        repo_settings = s.get(f'https://github.com/{username}/{repo_name}/settings').text
        soup = BeautifulSoup(repo_settings, 'html.parser')

        vform = soup.find(action='/'+username+'/'+repo_name+'/settings/set_visibility')

        authenticity_token = vform.find(name='input', attrs={'name': 'authenticity_token'})['value']

        data = {
            'authenticity_token': authenticity_token,
            'verify': username+'/'+repo_name,
            'visibility': 'private',
        }
        print("Setting "+repo_name+" to private with token "+authenticity_token)
        response = s.post(
            'https://github.com/'+username+'/'+repo_name+'/settings/set_visibility',
            data=data,
        )
        print(response.status_code)
        if response.status_code == 200 or response.status_code == 302:
            print("Successfully set "+repo_name+" to private.")
        else:
            print("Failed to set "+repo_name+" to private.")
        
    except Exception as e:
        print("Failed to set "+repo_name+" to private. (Could be forked repo)")
