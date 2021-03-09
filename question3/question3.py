from sklearn import neural_network
import pandas as pd


train_file = "/Users/peng/Desktop/NTU/AY20_MBDS_questions/Question 3/train_data.txt"
truth_file = "/Users/peng/Desktop/NTU/AY20_MBDS_questions/Question 3/train_truth.txt"
test_file = "/Users/peng/Desktop/NTU/AY20_MBDS_questions/Question 3/test_data.txt"

train_data  = pd.read_csv(train_file, sep = "\t")
train_truth = pd.read_csv(truth_file, sep = "\t")

test_data =  pd.read_csv(test_file, sep = "\t")


X = train_data[['x1','x2','x3']]
y = train_truth['y']

x_predict = test_data[['x1','x2','x3']]


# modeling
model = neural_network.MLPRegressor(hidden_layer_sizes=(5, 5,),learning_rate = 'adaptive')

# train model
model.fit(X, y)

#predict y
y = model.predict(x_predict)


with open('output_question_3', 'a') as f:
    f.write("y\n")
    for res in y:
        f.write(str(res))
        f.write('\n')
