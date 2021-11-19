from flask import Flask,request,jsonify,render_template
from flask_cors import CORS
import recommendation


app = Flask(__name__)
CORS(app)

@app.route('/')
@app.route('/index',methods=['GET'])
def index():
    return render_template('master.html')

@app.route('/go')
def go():
    # save user input in query
    query = request.args.get('query', '')
    res = recommendation.find_similar_games(int(query))
    if res==False:
        return render_template(
            'go.html',
            query='The game you like is not in the our recommend system.',
        )
    else:
        return render_template(
            'go.html',
            query='The game you type in is ' + str(res[0])+'.\n '
                    'These are the games we think you might like:\n'+str(res[1:]),
        )

if __name__=='__main__':
    app.run(port = 5000, debug = True)
