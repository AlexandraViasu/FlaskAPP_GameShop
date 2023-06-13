from flask import Flask

app = Flask(__name__, static_folder="static")
            
from controllers import controller

if __name__ == "__main__":
    app.run(debug=True)

