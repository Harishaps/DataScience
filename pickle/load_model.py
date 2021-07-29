import pickle

#load the model

loaded_model = pickle.load(open('diabetes_79.pkl','rb'))

pred = loaded_model.predict([[20,20,30,40,50,10,20,60]])

if pred[0] == 1:
    print('the person is diabetic')
else:
    print('person is not diabetic')
# print(pred)