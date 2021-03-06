from flask import Flask, request, jsonify
import random

app = Flask(__name__)

@app.route('/getQuote')
def getQuote():
    keyList = list(phrases.keys())
    num = random.randint(-1, len(keyList)-1)
    return jsonify({"quote": phrases[keyList[num]]})

@app.route('/getResponse',
methods = ['POST'])
def getResponse():
    request_json = request.get_json()
    print(request_json)
    print(phrases)
    return jsonify({"response": phrases.get(request_json.get("inp", "").lower(), "")})



if __name__=='__main__':
    lines = []

    f = open('nicoli.txt', 'r')
    lines = f.readlines()
    f.close()

    phrases = {}
    lines = [i.strip("\n") for i in lines]
    for line in lines:
        if '#' not in line and ':' in line:
            splitLine = line.split(":")
            splitLine = [i.strip() for i in splitLine]
            phrases[splitLine[0].lower()] = splitLine[1]
    print(phrases)
    app.run(debug=True)
