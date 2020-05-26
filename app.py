from flask import Flask, jsonify, request, make_response
from predictor import predict_jihad
app = Flask(__name__, instance_relative_config=True)
predict_jihad = predict_jihad()

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)
@app.errorhandler(500)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 500)

@app.route('/')
def index():
    text = request.args.get('text')
    if type(text) is str and len(text)!=0:
        return jsonify({"probability":predict_jihad.get_prediction(text)})
    else:
        return jsonify({"error":"check passed value"})

if __name__ == "__main__":
    app.run(debug=False)