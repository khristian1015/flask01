#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask

def main():
    print("en main")
    app = Flask(__name__)

    @app.route("/")
    def index():
        return "Hello World"

    app.run(port = 5000, debug = True)
    
    return 0
    
if __name__ == '__main__':
    print("en if dentro")
    main()


