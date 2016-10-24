import requests
import sys


def get_data(endpoint):
    url = "http://anapioficeandfire.com/api/{}/".format(endpoint)
    while url:
        results = requests.get(url)
        json_results= results.json()

        for item in json_results:
            print("Name: {}\n URL: {}\n".format(item["name"], item["url"]))

        if input("Enter to continue, 'q' to go back: "):
            break
        url = results.headers['link'].split(";")[0].replace('<', '').replace('>', '')


def get_specific_data(endpoint, num, lookup1="allegiances", lookup2="born", lookup3="died"):
    url = "http://anapioficeandfire.com/api/{}/{}/".format(endpoint, num)
    while url:
        results = requests.get(url)
        json_results= results.json()

        if endpoint == "characters":
            print("Name: {}\n Allegiances: {}\n Born: {}\n Died: {}".format(json_results["name"], json_results[lookup1], json_results[lookup2], json_results[lookup3]))

        elif endpoint == "houses":
            print("Name: {}\n Coat of Arms: {}\n House Words: {}\n Current Lord: {}".format(json_results["name"], json_results[lookup1], json_results[lookup2], json_results[lookup3]))
        else:
            print("Name: {}\n Number of Pages: {}\n Released: {}\n Authors: {}".format(json_results["name"], json_results[lookup1], json_results[lookup2], json_results[lookup3]))

        if input("Type 'q' to go back: "):
            break



while True:
    specific = input("Would you like to look up by [l]ists or by [s]pecific ID? To exit, type 'exit'.\n> ")
    if specific == 'exit':
        sys.exit()
    value = input("What would you like to look up? (characters), (houses), (books)?\n> ")
    if specific == 'l':
        get_data(value)
    else:
        value_id = input("What is the ID?\n> ")
        if value == "characters":
            get_specific_data(value, int(value_id))
        elif value == "houses":
            get_specific_data(value, int(value_id), lookup1="coatOfArms", lookup2="words", lookup3="currentLord")
        else:
            get_specific_data(value, int(value_id), lookup1="numberOfPages", lookup2="released", lookup3="authors")
