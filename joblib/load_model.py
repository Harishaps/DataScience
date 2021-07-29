import joblib

#load the model

loaded_model = joblib.load('dib_79.pkl')

pred = loaded_model.predict([[20,20,30,40,50,10,20,60]])

if pred[0] == 1:
    print('the person is diabetic')
else:
    print('person is not diabetic')
# print(pred)