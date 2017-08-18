# Solution is available in the other "solution.py" tab
import tensorflow as tf

softmax_data = [0.7, 0.2, 0.1]
one_hot_data = [1.0, 0.0, 0.0]

softmax = tf.placeholder(tf.float32)
one_hot = tf.placeholder(tf.float32)

# TODO: Print cross entropy from session
cross_entropy = - tf.reduce_sum(tf.multiply(one_hot, tf.log(softmax)))

with tf.Session() as sess:
    output = sess.run(cross_entropy, feed_dict={softmax: softmax_data, one_hot: one_hot_data})

print(output)





# All the pixels in the image (28 * 28 = 784)
features_count = 784
# All the labels
labels_count = 10

# TODO: Set the features and labels tensors
features = tf.placeholder(dtype=tf.float32, shape=[None, features_count])
labels = tf.placeholder(dtype=tf.float32, shape=[None, labels_count])

# TODO: Set the weights and biases tensors
weights = tf.Variable(initial_value=tf.random_normal(shape=[features_count, labels_count]))
biases = tf.Variable(initial_value=tf.zeros(shape=[labels_count]))
