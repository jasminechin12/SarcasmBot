#imports
from __future__ import print_function
import json
import wordLength as wl
import numpy as np
import tensorflow as tf
from tensorflow.contrib.tensor_forest.python import tensor_forest
from tensorflow.python.ops import resources

dictionary = []
reverse_dictionary = []
try:  
  with open('dict.json', 'r') as file:
    dictionary = json.loads(file.readlines()[0]) # use `json.loads` to do the reverseiexcept:
  with open('rdict.json', 'r') as file:
    reverse_dictionary = json.loads(file.readlines()[0]) # use `json.loads` to do the reverseiexcept:
except:
  import wordVecBasic as vec
  dictionary = vec.dictionary
  reverse_dictionary = vec.reverse_dictionary

# read files

def vectorize(label):
  try: 
    return dictionary[label]
  except:
    return 0

sData = open('sarcasm.txt')
nData = open('no_sarcasm.txt')

# extract features 
input_x1 = [[vectorize(word) for word in wl.topLargest(10,line.rstrip('\n'))] for line in sData] 
input_x2 = [[vectorize(word) for word in wl.topLargest(10,line.rstrip('\n'))] for line in nData] 
input_x = input_x1+input_x2
input_y = [1] * len(input_x1) + [0] * len(input_x2)
# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(input_x, input_y, test_size = 0.25, random_state = 0)

# Parameters
num_steps = 30 # Total steps to train
num_classes = 2 
num_features = 10
num_trees = 100 
max_nodes = 1000 

# Placeholders/data sctructure

X = tf.placeholder(tf.float32, shape=[None, num_features])
Y = tf.placeholder(tf.int64, shape=[None])

# Random Forest Parameters
hparams = tensor_forest.ForestHParams(num_classes=num_classes, num_features=num_features, num_trees=num_trees, max_nodes=max_nodes).fill()

# Build the Random Forest
forest_graph = tensor_forest.RandomForestGraphs(hparams)

# Get training graph and loss
train_op = forest_graph.training_graph(X, Y)
loss_op = forest_graph.training_loss(X, Y)

# Measure the accuracy
infer_op, _, _ = forest_graph.inference_graph(X)
correct_prediction = tf.equal(tf.argmax(infer_op, 1), tf.cast(Y, tf.int64))
accuracy_op = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

# Initialize the variables (i.e. assign their default value) and forest resources
init_vars = tf.group(tf.global_variables_initializer(), resources.initialize_resources(resources.shared_resources()))
    
# Start TensorFlow session
sess = tf.Session()

# Run the initializer
sess.run(init_vars)

# Training
for i in range(1, num_steps + 1):
    _, l = sess.run([train_op, loss_op], feed_dict={X: input_x, Y: input_y})
    if i % 10 == 0 or i == 1:
        acc = sess.run(accuracy_op, feed_dict={X: X_train, Y: y_train})
        print('Step %i, Loss: %f, Acc: %f' % (i, l, acc))

# Test Model
print("Test Accuracy:", sess.run(accuracy_op, feed_dict={X: X_test, Y: y_test}))

#Get the output
while (True):
	str = input("Enter a string: " )
	str_in = [[vectorize(word) for word in wl.topLargest(10, str)]] 
	out = sess.run(infer_op, feed_dict={X: str_in})

	print("Normal: ")
	print(out[0][0])
	print("Sarcastic: ")
	print(out[0][1])
