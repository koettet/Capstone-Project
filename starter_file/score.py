import json

def init():
    print("This is init()")


def run(request):
    reqBody = request.get_data(False)
        # For a real-world solution, you would load the data from reqBody
        # and send it to the model. Then return the response.
        resp = AMLResponse(reqBody, 200)
        resp.headers["Allow"] = "OPTIONS, GET, POST"
        resp.headers["Access-Control-Allow-Methods"] = "OPTIONS, GET, POST"
        resp.headers['Access-Control-Allow-Origin'] = "http://www.example.com"
        resp.headers['Access-Control-Allow-Headers'] = "*"
