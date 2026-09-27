#!/usr/bin/env python3

from flask import Flask, request, current_app, g, make_response, jsonify

contracts = [
    {"id": 1, "contract_information": "This contract is for John and building a shed"},
    {"id": 2, "contract_information": "This contract is for a deck for a buisiness"},
    {"id": 3, "contract_information": "This contract is to confirm ownership of this car"},
]
customers = ["bob", "bill", "john", "sarah"]
app = Flask(__name__)


@app.route("/contract/<int:id>", methods=["GET"])
def get_contract(id):
    """Look up a contract by its id.

    200 -> contract found, return its info.
    404 -> no contract with that id exists.
    """
    contract = next((c for c in contracts if c["id"] == id), None)

    if contract is None:
        return jsonify({"error": f"Contract with id {id} not found"}), 404

    return jsonify(contract), 200


@app.route("/customer/<customer_name>", methods=["GET"])
def get_customer(customer_name):
    """Check whether a customer exists, without exposing any of their data.

    204 -> customer found, but the body is intentionally empty (sensitive!).
    404 -> no customer with that name exists.
    """
    exists = customer_name.lower() in customers

    if not exists:
        return jsonify({"error": f"Customer '{customer_name}' not found"}), 404

    return "", 204


if __name__ == '__main__':
    app.run(port=5555, debug=True)
