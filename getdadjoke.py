import requests
import json

# takes a searchString, prints a list of 20 related jokes, and returns a list of those jokes
def searchDadJokes(searchString):
    baseurl = 'https://icanhazdadjoke.com/search'

    params_dict = {}
    params_dict['term'] = searchString

    head_dict = {}
    head_dict['User-Agent'] = 'https://jmf.codes'
    head_dict['Accept'] = 'application/json'

    res = requests.get(url = baseurl, params = params_dict, headers = head_dict)

    jokes_json = res.json()

    jokes_list = []
    for joke in jokes_json['results']:
        jokes_list.append(joke['joke'])
    for joke in jokes_list:
        print(joke)

    return jokes_list

# fetches random joke 
def randomDadJoke():
    baseurl = 'https://icanhazdadjoke.com/'
    head_dict = {}
    head_dict['User-Agent'] = 'https://jmf.codes'
    head_dict['Accept'] = 'application/json'
    res = requests.get(url = baseurl, headers = head_dict)
    jokes_json = res.json()
    print(jokes_json['joke'])


searchString = input("Enter a search term or hit enter for a random joke: ")
if searchString == '':
    randomDadJoke()
else:
    searchDadJokes(searchString)
