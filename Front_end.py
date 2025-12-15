##
## EPITECH PROJECT, 2025
## API-Sqlite-python-
## File description:
## Front_end
##

from flask import Flask

app = Flask(__name__)

@app.route("/")
def main():
    return "hello BIRTHDAY"

@app.route("insert")
def test():
    return "hello shit"

if __name__ == "__main__":
    app.run(debug=True)