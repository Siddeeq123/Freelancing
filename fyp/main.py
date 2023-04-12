# This is a sample Python script.
import string

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from flask import Flask, request, jsonify
import pickle
import numpy as np
import  sklearn

model = pickle.load(open('model1.pkl', 'rb'))
app = Flask(__name__)


@app.route('/')
def home():
    return "successful"


#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
@app.route('/predict', methods=['Post'])
def predict():
    # price = request.form.get('price')

    itching = request.form.get('itching')
    skin_rash = request.form.get('skin_rash')
    nodal_skin_eruptions = request.form.get('nodal_skin_eruptions')
    continuous_sneezing = request.form.get('continuous_sneezing')
    shivering = request.form.get('shivering')
    joint_pain = request.form.get('joint_pain')
    spotting_urination = request.form.get('spotting_urination')
    high_fever = request.form.get('high_fever')
    input_query = np.array([[itching, skin_rash, nodal_skin_eruptions, continuous_sneezing, shivering, joint_pain, spotting_urination,high_fever]], dtype = float)
    result = model.predict(input_query)[0]




    # result = {'price': price, 'location': location, 'city': city, 'baths': baths}
    return jsonify({'placement':str(result)})


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
