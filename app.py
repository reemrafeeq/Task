from flask import Flask, render_template, request ,jsonify
import pandas as pd
from services.analyzer import analyze_data


app = Flask(__name__)
@app.route("/", methods=["GET","POST"])
def home():
    if request.method == "GET":
        return render_template("index.html")
    # request.method == "POST":

    file = request.files["file"]
    df = pd.read_csv(file)
    df, class_average, top_performer, pass_percentage = analyze_data(df)
        # df["Total"] = (
        #     df["python"] 
        #     + df["java"] 
        #     + df["html"] 
        #     + df["css"])
        # df["Average"] = df["Total"] / 4
        # df["Grade"] = df["Average"].apply(calculate_grade (df["average"]))
        # class_average = df["Average"].mean()
        # top_performer = df.loc[df["Average"].idxmax(), "name"]
        # pass_count = (df["Average"] >= 50).sum()
        # total_students = len(df)
        # pass_percentage = (pass_count / total_students) * 100
    students = df.to_dict("records")

    return render_template(
            "results.html",
            students=students,
            class_average=class_average,
            top_performer=top_performer,
            pass_percentage=pass_percentage
        )

@app.route("/api/analyze", methods=["POST"])
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


if __name__ == "__main__":
    app.run(debug=True)
