from flask import Blueprint, jsonify, request


from tracer.data.models import db, Keys

applications = Blueprint('applications', __name__)

@applications.route('/', methods=['POST'])
def create():

    return jsonify({})