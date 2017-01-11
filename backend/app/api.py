from flask import Blueprint, current_app, send_from_directory

import os

api = Blueprint('api', __name__)

@api.route('/resume', methods=["GET"])
def get_latest_resume():
    resumes = []
    for fn in os.listdir('./resumes'):
        if os.path.isfile(fn) and fn.endswith('.pdf'):
            resumes.append(fn)
    latest = sorted(resumes, reverse=True)[0]
    return send_from_directory('/usr/src/app/resumes', latest)
