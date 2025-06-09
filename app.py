from flask import Flask, render_template, request, redirect, session
import pandas as pd
import ast
import random


app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for session

# Load rules and dataset
apriori_rules = pd.read_csv("apriori_rules.csv")
fpgrowth_rules = pd.read_csv("fpgrowth_rules.csv")
all_rules = pd.concat([apriori_rules, fpgrowth_rules]).drop_duplicates()

df = pd.read_csv("final_dataset_ready_superclean.csv")
categories = df["main_category"].unique()
products = df[["product_name", "main_category", "image"]].drop_duplicates()

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def do_login():
    username = request.form["username"]
    password = request.form["password"]
    if username == "admin" and password == "1234":
        session["user"] = username
        return redirect("/categories")
    else:
        return render_template("login.html", error="Invalid credentials")

@app.route("/categories", methods=["GET"])
def category_page():
    if "user" not in session:
        return redirect("/")
    return render_template("categories.html", categories=categories)

@app.route("/products", methods=["POST"])
def product_page():
    if "user" not in session:
        return redirect("/")
    selected_category = request.form["category"]
    filtered = products[products["main_category"] == selected_category]
    return render_template("products.html", products=filtered, category=selected_category)

@app.route("/recommend", methods=["POST"])
def recommend():
    if "user" not in session:
        return redirect("/")

    selected_product = request.form["product_name"].strip()
    recommendations = []

    for _, row in all_rules.iterrows():
        if selected_product in str(row["antecedents"]):
            try:
                items = list(ast.literal_eval(row["consequents"]))
                recommendations.extend(items)
            except:
                continue

    # Deduplicate and shuffle
    recommendations = list(set(recommendations))
    random.shuffle(recommendations)

    result = df[df["product_name"].isin(recommendations)][["product_name", "image"]].drop_duplicates()

    # ✅ Fallback if no recommendations found
    if result.empty:
        category = df[df["product_name"] == selected_product]["main_category"].values[0]
        fallback = df[(df["main_category"] == category) & (df["product_name"] != selected_product)]
        result = fallback.sample(n=min(4, len(fallback)))  # max 4 fallback
        message = "No rule-based matches found. Showing similar category products."
    else:
        message = ""

    return render_template("recommendations.html",
                           selected_product=selected_product,
                           recommendations=result.to_dict("records"),
                           message=message)
if __name__ == "__main__":
    app.run(debug=True)
