# Flask_ConcreteStrengthPredictor
End-to-end data science Project to predict concrete strength. Includes model training using machine learning, model serialization with pickle, and deployment via a Flask-based web application.

**Features:**
Model Training & Evaluation: Uses machine learning techniques to predict concrete strength.
Model Serialization: Saves the trained model with Pickle for easy deployment.
Flask Web Application: A user-friendly interface that takes concrete ingredients as input and predicts the strength.
Lightweight Interface: Simple and easy to use for testing predictions.

**Technologies Used**
Programming Language: Python
Libraries: Scikit-learn, Pandas, Numpy
Web Framework: Flask (for creating the web app)
Model Serialization: Pickle (for saving and loading the trained model)

**Deployment (Development Server)**
The Flask application runs on the local server for development purposes.

**Folder Structure**
Flask_ConcreteStrengthPredictor/
│
├── static/                                 # Contains JS file for the Flask app
├── templates/                              # Contains HTML templates for the Flask app
├── Concrete_Data.csv/                      # Dataset used for training
├── concrete.pkl/                           # Saved model file (Pickle format)
├── concrete strength_prediction.py         # Script for training the ML model
├── app.py                                  # Flask application file
├── requirements.txt                        # Dependencies
├── README.md                               # Description

**Usage**
>Install Dependencies:
First, install the required Python libraries by running the following command:
pip install -r requirements.txt

>Train the Model:
Run the program to train the machine learning model.
python concrete_strength_prediction.py
This will create a pickled model file (concrete.pkl) for deployment.

Run the Flask Application:
Run program to start the Flask web server:
python app.py

Make Predictions:
Enter the concrete ingredient values (e.g., cement, water, age) in user interface.
Click the Submit button to get the estimated concrete strength.

**Demo**
Screenshots of the app interface and functionality can be found in the repository.
