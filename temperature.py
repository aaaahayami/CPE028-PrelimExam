from flask import Flask, jsonify, request

app = Flask (__name__)
temp=[
    {
        "temp_id" : "1",
        "date" : "October 4, 2022",
        "temperature" : "37C"
    }
]

@app.route('/temp', methods=['GET'])
def readTemp():
    return jsonify(temp)

@app.route('/temp', methods=['POST'])
def addTemp():
    x = request.get_json()
    temp.append(x)
    return {'id': len(temp)}, 200

@app.route('/temp/<int:index>', methods=['DELETE'])
def deleteTemp(index):
    temp.pop(index)
    return 'Temperature Successfully deleted', 200

if __name__=='__main__':
    app.run()