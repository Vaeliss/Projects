import requests
from plotly.graph_objs import Bar,Layout
from plotly import offline

url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
headers = {"Accept":"application/vnd,github.v3+json"}
r = requests.get(url,headers)
response_dict = r.json()
repo_dicts = response_dict["items"]

repo_links, stars, labels = [], [], []

for repo_dict in repo_dicts:
    stars.append(repo_dict['stargazers_count'])
    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    label = f"{owner}<br />{description}"
    labels.append(label)
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)

data = [{'type':'bar',
         'x':repo_links,
         'y':stars,
         'hovertext':labels,
         'marker':{
             'color':'red',
             'line':{
                 'width':1.5,
                 'color':'grey'
                 },
             'opacity':0.6
             }
    }]
my_layout = Layout(title="most starred python repositories")
offline.plot({'data':data,'layout':my_layout},filename='repo.html')
