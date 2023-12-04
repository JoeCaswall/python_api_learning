import requests
import plotly.express as px
import sqlite3

con = sqlite3.connect("tutorial.db")
cur = con.cursor()


# Make an api call and check the response
# searching for python repos with more than 10_000 stars
url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"

headers = {"Accept": "application/vnd.github.v3+json"}
res = requests.get(url, headers=headers)
print(f"Status code: {res.status_code}")

response_dict = res.json()

print(response_dict.keys())

# Explore info about the repos
print(f"Total repositories: {response_dict["total_count"]}")
print(f"Complete results: {not response_dict['incomplete_results']}")

repo_dicts = response_dict["items"]
repo_names, stars = [], []
for repo_dict in repo_dicts:
    repo_names.append(repo_dict["name"])
    stars.append(repo_dict["stargazers_count"])

title = "Most-Starred Python Projects on Github"
labels = {"x": "Repository", "y": "Stars"}
fig = px.bar(x=repo_names, y=stars, title=title, labels=labels)

fig.update_layout(title_font_size=28, xaxis_title_font_size=20, yaxis_title_font_size=20)
fig.show()


