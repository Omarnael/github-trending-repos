import json
from constants import TRENDING_REPOS
from helper import language_of_repo
from flask import Flask, jsonify
import requests

app = Flask(__name__)

# Route that
@app.route('/repos')
def get_trending_data():

    # API Call to get trending repos during the previous month
    repo_data = requests.get(TRENDING_REPOS).json()

    # Language used by each repo
    repo_languages = language_of_repo(repo_data)

    # Stores the data required regarding each repo
    trending_repos_data = {}

    for language in language_of_each_repo:
        trending_repos_data[language] = {}
        trending_repos_data[language]['repositories'] = repo_languages[language]
        trending_repos_data[language]['number_of_repos'] = len(repo_languages[language])

    return jsonify(trending_repos_data)


@app.route('/')
def global_info():
    return ' Entry point to view Github trending data is /repos'


if __name__ == '__main__':
    app.run()
