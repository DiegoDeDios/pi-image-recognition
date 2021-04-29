export FLASK_APP=pi-image-recognition
export FLASK_ENV=development
export GOOGLE_APPLICATION_CREDENTIALS= $1

echo Installing dependencies...
pip3 install -r ./requires.txt