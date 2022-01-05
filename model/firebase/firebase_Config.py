import pyrebase

config = {
  "apiKey": "AIzaSyDZLq3ecuwMG9nLmT0IHwDeiPJFypMU7yQ",
  "authDomain": "huan-sa-hsu-final-99e3a.firebaseapp.com",
  "databaseURL": "https://huan-sa-hsu-final-99e3a-default-rtdb.asia-southeast1.firebasedatabase.app",
  "projectId": "huan-sa-hsu-final-99e3a",
  "storageBucket": "huan-sa-hsu-final-99e3a.appspot.com",
  "messagingSenderId": "547943655261",
  "appId": "1:547943655261:web:439e0013b923485f62aab4",
  "measurementId": "G-G3JD9S90V5"
}

firebase = pyrebase.initialize_app(config)

db_firebase = firebase.database()