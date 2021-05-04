import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):

    if word.lower() in data:
        return data[word]
    elif len(get_close_matches(word,data.keys()))> 0:

        confirmation = input("Do you mean %s instead? Press Y if yes or N if no: " % get_close_matches(word,data.keys())[0])
        if confirmation == "Y" or confirmation == "y":
            return data[get_close_matches(word,data.keys())[0]]
        elif confirmation == "N" or confirmation == "n":
            return "The word doesn't exist. Check Again."
        else:
            return "Invalid entry.Try Again."
        
    else:
        return "The word doesn't exist. Check Again."

word = input("Enter word: ")
result = translate(word)

if isinstance(result,list):
    for item in result:
        print(item)
else:
        print(result)