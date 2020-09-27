# github-trending-repos
A REST microservice developed using Flask to retrieve data regarding the trending Github repositories during the last month.

# Functional Specs
* Trending repositories were retrieved using this unofficial API https://github.com/huchenme/github-trending-api
* Develop a REST microservice that list the languages used by the trending public repos on GitHub
* For every language, you need to calculate the attributes below :
  * Number of repos using this language
  * The list of repos using the language

# Entry Points

* **/repos**
   * Languages used, number of repos using this language, and the list of repos using the language.

* **/**
    * Global info.


# Instructions

* Install dependencies
```shell
pip install Requests
pip install flask
```
* Run
```shell
python app.py
```

