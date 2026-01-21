from flask import Flask, jsonify, request
from pymongo import MongoClient

app = Flask("__name__")

client = MongoClient("mongodb+srv://vikram_DB:FsGnNq5GNa6idbot@vikramhemchandar.rtgw4pn.mongodb.net/")
db = client["pythonfordevops"]
col = db["fruits"]

@app.route("/")
def showProductsDBItem():
    # data = request.args.get("name")
    # usrsearch = data["name"]
    data = []
    c = col.find({},{"_id":0})
    for i in c:
        data.append(i)
    print(data)
    return jsonify(data)

@app.route("/productdb", methods=["GET"])
def searchGetDBItem():
    usrsearch = request.args.get("name")
    print("GET User search :", usrsearch)
    data = []
    c = col.find({"name": usrsearch},{"_id":0})
    for i in c:
        data.append(i)
    print("In GET method" , data)
    return jsonify(data)

@app.route("/productdb", methods=["POST"])
def searchPostDBItem():
    data = request.get_json()
    print("Data in Post method : ", data)
    usrsearch = data["name"]
    print("POST User search :", usrsearch)
    data = []
    c = col.find({"name": usrsearch},{"_id":0})
    for i in c:
        data.append(i)
    print("In POST method" , data)
    return jsonify(data)


# @app.route("/productdb", methods=["POST"])
# def searchPostDBItem():
#     data = request.get_json()
#     usrsearch = data["name"]
#     print("POST User search :", usrsearch)
#     data = []
#     c = col.find({"name": usrsearch},{"_id":0})
#     # check=0
#     for i in c:
#         # if i["name"] == usrsearch:
#             data.append(i)
#             # check = 1
#             print("In Post Method", data)
#             return jsonify(data)
#         # else:
#             # check = 0
#     # return jsonify(data)

if __name__ == ("__main__"):
    app.run(debug=True)
