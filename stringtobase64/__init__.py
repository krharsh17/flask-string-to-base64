from flask import Flask, request, jsonify
import base64

 
# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)
 
# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.
@app.route('/', methods=['GET'])
def convert():
    input_string = request.args.get('input_string')

    if input_string is None:
        return "Please provide a valid 'input_string' parameter in the query."

    b = base64.b64encode(bytes(input_string, 'utf-8'))
    base64_str = b.decode('utf-8')


    return jsonify(base64_str)

 
# main driver function
if __name__ == '__main__':
 
    # run() method of Flask class runs the application 
    # on the local development server.
    app.run(port=8000)