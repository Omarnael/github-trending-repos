# Helper function that returns the language used by each repo
def language_of_repo(repos):
    repo_language = {}
    for repo in repos:
        repo_language.setdefault(repo['language'], []).append(repo['name'])
    return repo_language
