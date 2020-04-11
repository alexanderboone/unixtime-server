'''
Microservice that returns the Unix Time (AKA epoch time), which is
the time that has elapsed since 12:00 AM GMT on January 1, 1970, in seconds.
'''

import os
import time
from flask import Flask

app = Flask(__name__)

@app.route('/unixtime/')
def get_unixtime():
    '''Return unix time in seconds'''
    unixtime = int(time.time())
    return str(unixtime)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6738))
    app.run(host='0.0.0.0', port=port)