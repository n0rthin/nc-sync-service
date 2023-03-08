from flask import request, jsonify, make_response
from functools import wraps
import os

def token_required(f):
  @wraps(f)
  def decorator(*args, **kwargs):
      token = None
      # ensure the jwt-token is passed with the headers
      if 'x-access-token' in request.headers:
          token = request.headers['x-access-token']
      if not token or token != os.environ["API_TOKEN"]: # throw error if no token provided
          return make_response(jsonify({"message": "Unauthorized!"}), 401)
      
      return f(*args, **kwargs)
  return decorator