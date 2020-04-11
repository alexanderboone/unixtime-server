import os
import datetime
from flask import Flask

app = Flask(__name__)

@app.route('/unixtime/')
def get_unixtime():
    unixtime = "Placeholder for Unix Time"
    return unixtime

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6738))
    app.run(host='0.0.0.0', port=port)