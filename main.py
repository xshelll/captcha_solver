from flask import Flask, redirect, url_for, request
from solver import Solve

app = Flask(__name__)
print("App initialized")

@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name


@app.route("/captcha/gettext",methods=['POST'])
def home():
    if request.method == 'POST':
        try:
            request_data = request.get_json()
            username = request_data['username']
            apikey = request_data['apikey']
            data = request_data['data']
        except:
            return {'error':'All fields are required!'}

        if username == '' or apikey == '' or data == '':
            return {'error':'All fields are required!'}

        status,text = Solve(username=username,apikey=apikey,data=data)
        if status:
            return {'result': text}
        else:
            return {'error': text}



if __name__ == "__main__":
    import os
    PORT = os.getenv("PORT",5000)
    app.run("0.0.0.0",PORT)