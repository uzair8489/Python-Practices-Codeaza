#                                                       FLASK API

from flask import Flask, jsonify

app = Flask(__name__)

#functionality to check the prime number
@app.route("/is_prime/<int:number>")
def is_prime(number):
    is_prime = number > 1 and all(number % i != 0 for i in range(2, int(number**0.5) + 1))
    context = {
        "number": number,
        "is_prime": is_prime,
    }
    return jsonify(context)

if __name__ == "__main__":
    app.run()


"""
The above API i created checks the provided number if its prime or not and returns the result as a JSON response with the "is_prime"
field shows whether the number is prime (true) or not (false) and the "number" field shows the original number provided.

"""