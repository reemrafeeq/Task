def calculate_grade(average):

    if average >= 90:
        return "A+"

    elif average >= 80:
        return "A"

    elif average >= 70:
        return "B"

    elif average >= 60:
        return "C"

    elif average >= 50:
        return "D"

    else:
        return "F"

def analyze_data(df):

      df["Total"] = (
        +df["python"]
        + df["java"]
        + df["html"]
        + df["css"]
    )
      df["Average"] = df["Total"] / 4

      df["Grade"] = df["Average"].apply(calculate_grade)

      class_average = df["Average"].mean()

      top_performer = df.loc[ df["Average"].idxmax(), "name"]

      pass_count = (df["Average"] >= 50).sum()

      total_students = len(df)

      pass_percentage = (pass_count / total_students) * 100

      return df, class_average, top_performer, pass_percentage