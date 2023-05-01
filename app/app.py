import json
from difflib import get_close_matches
import uvicorn
from fastapi import FastAPI


app = FastAPI()

data = json.load(open("data.json"))


# def translate(w):
#     w = w.lower()
#     yn = ""
#     if w in data:
#         return data[w]
#     elif len(get_close_matches(w, data.keys())) > 0:
#         yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(w, data.keys())[0])
#         if yn.lower() == "y":
#             return data[get_close_matches(w, data.keys())[0]]
#         elif yn.lower() == "n":
#             return "The word doesn't exist. Please double check it."
#         else:
#             return "We didn't understand your entry."
#     else:
#         return "The word doesn't exist. Please double check it."


@app.get('/{word}')
def get_meaning(word):
    if word.lower() in data:
        return {"success": 1, "data" :  data[word.lower()]}
    else :
        return {"success": 0, "data" : "Word not found"}
@app.get('/closed/{word}')
def get_closed_match(word):
    closed_matches = get_close_matches(word.lower(), data.keys())
    if len(closed_matches) > 0:
        return {"success": 1, "data" : closed_matches}
    else :
        return {"success": 0, "data" : "Word not found"}
       
if __name__ == "__main__":
    uvicorn.run(app,host = "0.0.0.0", port=8000)
# word = input("Enter word: ")
# output = translate(word)
# if type(output) == list:
#     for item in output:
#         print(item)
# else:
#     print(output)
