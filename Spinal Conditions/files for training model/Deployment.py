from flask import Flask, request, render_template
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained SVM model
model = joblib.load('svm_spinal_classifier.pkl')

@app.route('/')
def home():
    return render_template('deploy.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get input values from the form
    pelvic_incidence = float(request.form['pelvic_incidence'])
    pelvic_tilt = float(request.form['pelvic_tilt'])
    lumbar_lordosis_angle = float(request.form['lumbar_lordosis_angle'])
    sacral_slope = float(request.form['sacral_slope'])
    pelvic_radius = float(request.form['pelvic_radius'])
    degree_spondylolisthesis = float(request.form['degree_spondylolisthesis'])

    # Prepare the input data for prediction
    input_data = np.array([[pelvic_incidence, pelvic_tilt, lumbar_lordosis_angle, sacral_slope, pelvic_radius, degree_spondylolisthesis]])

    # Make the prediction
    prediction = model.predict(input_data)

    # Map the predicted label to a meaningful class name (adjust as necessary)
    labels = ['DH', 'SL', 'NO']  # Assuming these are your class labels
    predicted_class = labels[prediction[0]]

    return render_template('deploy.html', prediction_text=f'Predicted Spinal Condition: {predicted_class}')

if __name__ == "__main__":
    app.run(debug=True)
