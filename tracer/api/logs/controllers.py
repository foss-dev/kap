from flask import Blueprint, jsonify, request
from werkzeug import generate_password_hash
from sqlalchemy.exc import IntegrityError

from tracer.data.models import db, Languages, ExceptionTypes, Logs
