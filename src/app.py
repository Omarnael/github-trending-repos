import json
from constants import TRENDING_REPOS
from helper import language_of_repo
from flask import Flask, jsonify
import requests

app = Flask(__name__)


@app.route('/repos')
def get_trending_data():
    repo_data = requests.get(TRENDING_REPOS).json()
    language_of_each_repo = language_of_repo(repo_data)
    trending_repos_data = {}

    for i in language_of_each_repo:
        trending_repos_data[i] = {}
        trending_repos_data[i]['repositories'] = language_of_each_repo[i]
        trending_repos_data[i]['number_of_repos'] = len(language_of_each_repo[i])

    return jsonify(trending_repos_data)


@app.route('/')
def global_info():
    return ' Entry point to view Github trending data is /repos'


if __name__ == '__main__':
    app.run()
