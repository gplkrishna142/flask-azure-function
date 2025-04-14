import logging
import azure.functions as func
from flask import Flask, request

# Create the Flask app
app = Flask(__name__)

# Define a simple route
@app.route('/')
def home():
    return "Hello from Flask inside Azure Function!"

# Azure Function entry point
def main(req: func.HttpRequest, context: func.Context) -> func.HttpResponse:
    return func.WsgiMiddleware(app.wsgi_app).handle(req, context)
