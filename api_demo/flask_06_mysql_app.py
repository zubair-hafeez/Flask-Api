from flask import Flask, jsonify
import pymysql
import time
import json
from flask_demo.api_demo.flask_06_db_config import get_mysql_connection
from flask_restx import Api, Resource, fields

app = Flask(__name__)
api = Api(
    app,
    version="1.0",
    title="Flask App using MySQL",
    description="A simple API to demonstrate the power of RestAPI with MySQL",
)

# Establish database connections
mysql_conn = get_mysql_connection()

@api.route("/", methods=["GET"])
class sakila(Resource):
    def get():
        """Load HomePage.

        Args: None

        Returns:
            json: Hello World.
        """
        return jsonify("Welcome to Sakila Database")


film_model = api.model(
    "Film",
    {
        "film_id": fields.Integer(description="Film ID", required=True, example=2),
    },
)

film_actor_model = api.model(
    "Film",
    {
        "film_id": fields.Integer(description="Film ID", required=True, example=2),
    },
)


@api.route("/film/<int:film_id>", methods=["GET"])
class film(Resource):
    @api.doc(model=[film_model])
    def get(self, film_id):
        """Retrieve film details by film ID.

        Args:
            film_id (int): The ID of the film.

        Returns:
            json: Film details including title, description, release year, source, and time taken.
        """
        film_key = f"film:{film_id}"

        with mysql_conn.cursor() as cursor:
            sql = "SELECT title, description, release_year FROM film WHERE film_id = %s"
            cursor.execute(sql, (film_id,))
            result = cursor.fetchone()
            if result:
                film_data = {
                    "title": result[0],
                    "description": result[1],
                    "release_year": result[2],
                }
                film = film_data
            else:
                return jsonify({"message": "Film not found"}), 404
            
        return jsonify({"film": film})


@api.route("/film/<int:film_id>/actors", methods=["GET"])
class film_actor(Resource):
    @api.doc(model=[film_actor_model])
    def get(self, film_id):
        """Retrieve all actors for a given film and other films acted by them.

        Args:
            film_id (int): The ID of the film.

        Returns:
            json: Actor details and other films they have acted in, along with the source and time taken.
        """
        actors_data = []
        with mysql_conn.cursor() as cursor:
            actor_query = """
            SELECT a.actor_id, a.first_name, a.last_name
            FROM actor a
            JOIN film_actor fa ON a.actor_id = fa.actor_id
            WHERE fa.film_id = %s
            """
            cursor.execute(actor_query, (film_id,))
            actors = cursor.fetchall()

            for actor in actors:
                actor_id, first_name, last_name = actor
                other_films_query = """
                SELECT f.film_id, f.title
                FROM film f
                JOIN film_actor fa ON f.film_id = fa.film_id
                WHERE fa.actor_id = %s AND f.film_id != %s
                """
                cursor.execute(other_films_query, (actor_id, film_id))
                other_films = cursor.fetchall()

                actors_data.append(
                    {
                        "actor_id": actor_id,
                        "first_name": first_name,
                        "last_name": last_name,
                        "other_films": other_films,
                    }
                )

        return jsonify(
            {"actors": actors_data}
        )


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5006)
    ## app.run(host="127.0.0.1", port=5006, debug=True)
