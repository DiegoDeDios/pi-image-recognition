set FLASK_APP=flaskr
set FLASK_ENV=development
set GOOGLE_APPLICATION_CREDENTIALS=KEY_PATH = %1 

echo Installing dependencies...
pip3 install -r ./requires.txt