# Air-Angel

First, the system, used in this project is a Raspberry Pi + GrovePi board + Grove Temperature and humidity sensor pro + Grove barometer sensor BMP280.

The project's purpose is to train a model to predict air quality parameters. You need to get some data containing Temperature, Humidity, Air Pressure, and some pollutants in the air (like Nitrogen Oxide) for the model training, and
then decide which pollutants to predict with it.

All starts with the ChosenModelTuning.py script. In this script, you load some csv data for training, do some data processing (in the script I use scalers), choose a machine learning
algorithm, and train the model. After the training, if the model satisfies your needs, dump it in a file using the joblib library:

from joblib import dump

dump(regr,”regr.joblib”)

dump(xscaler,”xscaler.joblib”)

dump(yscaler,”yscaler.joblib”)


Do not forget to dump your data processing models.

To be able to use the BMP280 sensor, you need to execute these steps:

•	sudo apt-get install build-essential python-pip python-dev python-smbus git

•	git clone https://github.com/adafruit/Adafruit_Python_GPIO.git

•	cd Adafruit_Python_GPIO

•	sudo python3 setup.py install

•	Note: ATLAS should also be installed: sudo apt-get install libatlas-base-dev


The Sensors_Read.py script is used to read from the sensors and return the read values. The code from it is used in the ReadSensorsAndPredict.py script, where the trained model,
which is assumed to be saved to a file, is loaded and used to predict pollutants, based on the measured values.

There are two UIs. The UI.py script executes a grid, which fills rows with measured and predicted values, counts exceeds of pollutant norms, and logs every row, exceed, and exceed counters.

The code for scrolling in the UI.py script is taken from (Bryan Oakley, 2017) (profile: https://stackoverflow.com/users/7432/bryan-oakley), who commented this question: https://stackoverflow.com/questions/3085696/adding-a-scrollbar-to-a-group-of-widgets-in-tkinter/3092341#3092341

The second UI is the PredictValueUI.py script. Its job is to allow a user to enter values for Temperature, Humidity, and Air Pressure, use our trained model, and get predicted values.
