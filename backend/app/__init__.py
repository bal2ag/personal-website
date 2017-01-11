from flask import Flask, jsonify, current_app

def create_app():
    app = Flask(__name__)

    import logging, sys
    date_fmt = "%Y-%m-%dT%H:%M:%SZ"
    fmt_string = "APP_[%(levelname)s %(asctime)s %(process)d " +\
        "%(threadName)s %(filename)s:%(lineno)d] %(message)s"
    formatter = logging.Formatter(fmt_string, date_fmt)
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(formatter)

    app.logger.addHandler(handler)
    app.logger.setLevel("INFO")

    from api import api as api_blueprint
    app.register_blueprint(api_blueprint)

    from healthcheck import healthcheck as healthcheck_blueprint
    app.register_blueprint(healthcheck_blueprint)

    return app
