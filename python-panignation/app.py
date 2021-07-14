import os

from flask import (
    Flask,
    redirect,
    url_for,
    render_template,
    request,
    abort,
    jsonify,
    json,
)
from flask_cors import CORS, cross_origin
from werkzeug.exceptions import HTTPException
from dotenv import load_dotenv
from db_conn import get_pg_connection

from controller.controller import *

load_dotenv()

# postgres connection objecst
pg = get_pg_connection()


app = Flask(__name__)
# app.config["SECRET_KEY"] = os.getenv("SECRET")
# CORS(app, supports_credentials=True)
# app.config["CORS_HEADERS"] = "Content-Type"


@app.route("/", methods=["GET", "POST"])
# @cross_origin()
def post_user_details():
    if request.method == "POST":  
        request_json = request.json
        response = post_data(request_json, pg)
        return response
    return {"msg": "Hello Tech savvy", "success": True}


@app.route("/data/<page_number>")
def view(page_number):
    items_per_page = 5
    offset = (int(page_number) - 1) * 5
    limit = offset + 5
    return jsonify(
        get_data(
            pg=pg,
            offset=str(offset),
            limit=str(limit),
        )
    )


@app.errorhandler(HTTPException)
def handle_exception(e):
    """Return JSON instead of HTML for HTTP errors."""
    # start with the correct headers and status code from the error
    response = e.get_response()
    # replace the body with JSON
    response.data = json.dumps(
        {
            "code": e.code,
            "name": e.name,
            "description": e.description,
        }
    )
    response.content_type = "application/json"
    return response


if __name__ == "__main__":
    # DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(host="0.0.0.0", port=8080, debug=True)
