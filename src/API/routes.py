
from flask import Flask, request, jsonify


from coach import Coach, load_coaches, save_coach

app = Flask(__name__)




@app.route('/coaches', methods=['GET'])
def get_coaches():
    coaches = load_coaches()
    return jsonify(coaches)




@app.route('/add_coache', methods=['POST'])
def add_coach():
    data = request.json
    new_coach = Coach(data.get('name'),data.get('sport'),data.get('experience'),[])
    try : 
        save_coach(new_coach)
        return jsonify({"message": f"Coach {data.get('name')} added successfully."}), 201
    except :
        return jsonify({"message": f"Coach can not be added."}), 500






if __name__ == '__main__':
    app.run(debug=True)