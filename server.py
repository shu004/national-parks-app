"""Server for national park app"""

from flask import (Flask, render_template, session, redirect, request, flash)
from model import connect_to_db

app = Flask(__name__)


# Replace this with routes and view functions!


if __name__ == "__main__":
    # DebugToolbarExtension(app)
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
