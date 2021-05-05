from flask import Flask, jsonify

# Createing a "games" JSON / dict to emulate data coming from a database.
games = [
  {
    "id": 0,
    "name": "Scrabble",
    "editor": "mattel",
    "year_published": "1978",
    "description": "descp",
    "category": "family",
    "time": "60min",
    "number_player": "2-5"
  },
  {
    "id": 1,
    "name": "Aventuriers du rail",
    "editor": "asmodee",
    "year_published": "2006",
    "description": "descp",
    "category": "family",
    "time": "45min",
    "number_player": "2-5"
  }
]

Utilisateur = [
  {
    "id": 0,
    "identifiant": "toto",
    "nom": "toto",
    "prenom": "toto1",
    "role": "membre",
    "Presentation": "moi",
    "Avatar": "https://www.monimage.fr/img.jpg",
    "Email": "string",
    "Password": "string"
  },
  {
    "id": 1,
    "identifiant": "titi",
    "nom": "titi",
    "prenom": "titi1",
    "role": "membre",
    "Presentation": "toi",
    "Avatar": "https://www.monimage.fr/img.jpg",
    "Email": "string",
    "Password": "string"
  }
]


# Creating a new "app" by using the Flask constructor. Passes __name__ as a parameter.
app = Flask(__name__)

# Annotation that allows the function to be hit at the specific URL.
@app.route("/")
# Generic Python functino that returns "Hello world!"
def index():
    return "Hello world!"

# Annotation that allows the function to be hit at the specific URL. Indicates a GET HTTP method.
@app.route("/bordgames/v1.0/games", methods=["GET"])
# Function that will run when the endpoint is hit.
def get_games():
    # Returns a JSON of the games defined above. jsonify is a Flask function that serializes the object for us.
    return jsonify({"games": games})


# Annotation that allows the function to be hit at the specific URL with a parameter. Indicates a GET HTTP method.
@app.route("/bordgames/v1.0/games/<int:game_id>", methods=["GET"])
# This function requires a parameter from the URL.
def get_game(game_id):
    # Create an empty dictionary.
    result = {}

    # Loops through all the different games to find the one with the id that was entered.
    for game in games:
        # Checks if the id is the same as the parameter.
        if game["id"] == game_id:
            # Sets the result to the game and makes it a JSON.
            result = jsonify({"game": game})

    # Returns the game in JSON form or an empty dictionary. Should handle the error like 404, but will not cover here.
    return result


@app.route("/bordgames/v1.0/games/<int:game_id>/<string:game_name>/<string:game_editor>/<string:game_year>/<string:game_desc>/<string:game_cat>/<string:game_time>/<string:game_nbplayer>", methods=["POST"])
# This function requires a parameter from the URL.
def postadd_game(game_id,game_name,game_editor,game_year,game_desc,game_cat,game_time,game_nbplayer):
    # Create an empty dictionary.
    result = {
    "id": game_id,
    "name": game_name,
    "editor": game_editor,
    "year_published": game_year,
    "description": game_desc,
    "category": game_cat,
    "time": game_time,
    "number_player": game_nbplayer
}
    result = jsonify(result)
    # Returns the game in JSON form or an empty dictionary. Should handle the error like 404, but will not cover here.
    return result

@app.route("/bordgames/v1.0/games/<int:game_id>/<string:game_name>/<string:game_editor>/<string:game_year>/<string:game_desc>/<string:game_cat>/<string:game_time>/<string:game_nbplayer>", methods=["PUT"])
# This function requires a parameter from the URL.
def put_game(game_id,game_name,game_editor,game_year,game_desc,game_cat,game_time,game_nbplayer):
    # Create an empty dictionary.
    result = {
    "id": game_id,
    "name": game_name,
    "editor": game_editor,
    "year_published": game_year,
    "description": game_desc,
    "category": game_cat,
    "time": game_time,
    "number_player": game_nbplayer
}
    result = jsonify(result)
    # Returns the game in JSON form or an empty dictionary. Should handle the error like 404, but will not cover here.
    return result

@app.route("/bordgames/v1.0/games/<int:game_id>/<string:game_name>/<string:game_editor>/<string:game_year>/<string:game_desc>/<string:game_cat>/<string:game_time>/<string:game_nbplayer>", methods=["DELETE"])
# This function requires a parameter from the URL.
def del_game(game_id,game_name,game_editor,game_year,game_desc,game_cat,game_time,game_nbplayer):
    for game in games:
        # Checks if the id is the same as the parameter.
        if game["id"] == game_id:
          retour = games.pop(game["id"])
          #print("Elements supprimé:",retour)
            # Sets the result to the game and makes it a JSON.
        result = jsonify(games)  

    # Returns the game in JSON form or an empty dictionary. Should handle the error like 404, but will not cover here.
    return result

@app.route("/bordgames/v1.0/games/<int:game_id>/<string:game_name>/<string:game_editor>/<string:game_year>/<string:game_desc>/<string:game_cat>/<string:game_time>/<string:game_nbplayer>", methods=["PUT"])
# This function requires a parameter from the URL.
def putt_game(game_id,game_name,game_editor,game_year,game_desc,game_cat,game_time,game_nbplayer):
    # Create an empty dictionary.
    result = {
    "id": game_id,
    "name": game_name,
    "editor": game_editor,
    "year_published": game_year,
    "description": game_desc,
    "category": game_cat,
    "time": game_time,
    "number_player": game_nbplayer
}
    result = jsonify(result)
    # Returns the game in JSON form or an empty dictionary. Should handle the error like 404, but will not cover here.
    return result

@app.route("/bordgames/v1.0/games/<int:game_id>/<string:game_identifiant>/<string:game_nom>/<string:game_prenom>/<string:game_role>/<string:game_Presentation>/<string:game_Avatar>/<string:game_Email>/<string:game_Password>", methods=["POST"])
# This function requires a parameter from the URL.
def postuser_game(game_id,game_identifiant,game_nom,game_prenom,game_role,game_Presentation,game_Avatar,game_Email,game_Password):
    # Create an empty dictionary.
    result = {"id": game_id,
    "identifiant": game_identifiant,
    "nom": game_nom,
    "prenom": game_prenom,
    "role": game_role,
    "Presentation": game_Presentation,
    "Avatar": game_Avatar,
    "Email": game_Email,
    "Password": game_Password}
    result = jsonify(result)
    # Returns the game in JSON form or an empty dictionary. Should handle the error like 404, but will not cover here.
    return result




'''
# Ajout jeux.
@app.route("/bordgames/v1.0/games/", methods=["POST"])
# This function requires a parameter from the URL.
def post_game():
    # Create dictionary.
    result = {
    "id": 2,
    "identifiant": "tutu",
    "nom": "tutu",
    "prenom": "tutu1",
    "role": "membre",
    "Presentation": "toi",
    "Avatar": "https://www.monimage.fr/img.jpg",
    "Email": "string",
    "Password": "string"
  }
    # Loops through all the different games to find the one with the id that was entered.
    for game in games:
        # Checks if the id is the same as the parameter.
        if game["id"] == game_id:
            # Sets the result to the game and makes it a JSON.
            result = jsonify({"game": game})

    # Returns the game in JSON form or an empty dictionary. Should handle the error like 404, but will not cover here.
    return result
'''

# Checks to see if the name of the package is the run as the main package.
if __name__ == "__main__":
    # Runs the Flask application only if the main.py file is being run.
    app.run(host='0.0.0.0')