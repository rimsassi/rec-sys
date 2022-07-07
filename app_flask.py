import flask
import pandas as pd


df_output = pd.read_csv("./option1_recommendation_new.csv")


def customer_recomendation(customer_id):
    if customer_id not in df_output.index:
        print("Customer not found.")
        return customer_id
    return df_output.loc[customer_id]


app = flask.Flask(__name__, template_folder="template")


@app.route("/", methods=["GET", "POST"])
def main():
    if flask.request.method == "GET":
        return flask.render_template("main.html")

    if flask.request.method == "POST":
        customer_id = flask.request.form["customer_id"]
        customer_id = int(customer_id)

        recommendedProducts = customer_recomendation(customer_id)

        return flask.render_template(
            "main.html",
            original_input={"Identifiant du client": customer_id},
            result=recommendedProducts.iloc[1],
        )


if __name__ == "__main__":
    # app.debug = True
    app.run()
