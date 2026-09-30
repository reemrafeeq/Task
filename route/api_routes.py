from flask import Blueprint, request, jsonify
import pandas as pd

from services.analyzer import analyze_data


api = Blueprint("api", __name__)


@api.route("/analyze", methods=["POST"])
def analyze():

    data = request.get_json()

    students = data["students"]

    df = pd.DataFrame(students)

    df, class_average, top_performer, pass_percentage = analyze_data(df)

    results = df.to_dict("records")

    return jsonify({
        "class_average": class_average,
        "top_performer": top_performer,
        "pass_percentage": pass_percentage,
        "students": results
    })