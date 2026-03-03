
from flask import Flask, render_template
import pandas as pd
import os

app = Flask(__name__)

EXCEL_FILE = "data.xlsx"
WHATSAPP = "972526766106"

def load_data():
    if not os.path.exists(EXCEL_FILE):
        return None
    return pd.read_excel(EXCEL_FILE).fillna("")

@app.route("/")
def home():
    return "SERVER WORKING"

@app.route("/r/<id>")
def record(id):

    df = load_data()

    if df is None:
        return "Excel file missing"

    row = df[df["ID"].astype(str) == id]

    if row.empty:
        return "Record not found"

    rec = row.iloc[0].to_dict()

    name = rec.get("Name","")

    data = []

    for k,v in rec.items():
        if v != "":
            data.append((k,v))

    link = f"https://wa.me/{WHATSAPP}?text=Support%20Request%20ID%20{id}"

    return render_template("record.html",name=name,id=id,data=data,wa=link)

if __name__ == "__main__":
    app.run()
