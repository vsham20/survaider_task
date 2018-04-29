from app import app
from flask import render_template, jsonify, request
from utils import fetch_gender_and_relationship_data, people_count_in_each_relationship, get_all_data
from models import IndividualDetails

@app.route('/dashboard', methods=["GET"])
def index():
    pagination, all_data, offset = get_all_data(request)
    kwargs = {'pagination':pagination,'all_data':all_data,'offset':offset}
    return render_template('base.html', **kwargs)

@app.route('/count/gender', methods=["GET"])
def get_count_per_gender():
    count_per_gender = fetch_gender_and_relationship_data()
    return jsonify(count_per_gender)

@app.route('/count/relationship', methods=["GET"])
def get_count_per_relationship():
    count_per_relationship = people_count_in_each_relationship()
    return jsonify(count_per_relationship)