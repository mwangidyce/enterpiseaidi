# from flask import Flask, render_template, request
# import os
# from pathlib import Path
# import functools
# from flask import request

# from sqlite_project.flask_app.db import get_db

# def create_app():
#     app = Flask(__name__)
#     app.config.from_mapping(
#         SECRET_KEY='dev',
#         DATABASE=Path(app.instance_path).resolve() / 'flaskr.sqlite',
#     )

#     # Check whether is directory
#     if not Path(app.instance_path).is_dir():
#         os.makedirs(app.instance_path)

#     from . import db
#     db.init_app(app)

#     @app.route("/get_post", methods=["GET", "POST"])
#     def get_post_operations():
#         if request.method == "POST":
#             db = get_db()
#             result_dict: dict = request.get_json()
#             try:
#                 db.execute(
#                     "INSERT INTO student (first_name, last_name ) VALUES (?, ?)",
#                     (result_dict["first_name"], result_dict["last_name"]),
#                 )
#             except:
#                 pass

#         ...

#     @app.route("/update_post", methods=["UPDATE"])
#     def update_operation():
#         ...

#     @app.route("/get_post", methods=["DELETE"])
#     def delete_operation():
#         ...

#     return app
