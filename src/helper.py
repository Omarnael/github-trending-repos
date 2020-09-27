def language_of_repo(repos):
    repo_language = {}
    for repo in repos:
        repo_language.setdefault(repo['language'], []).append(repo['name'])
    return repo_language
