import tensorflow as tf
import numpy as np

FLAGS = None

# create data
x_data = np.random.rand(100).astype(np.float32)
print(x_data)
y_data = np.power(x_data, 2) * 0.1 + 0.35

# create tensorflow structure start
Weights = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
biases = tf.Variable(tf.zeros([1]))
with tf.name_scope('summaries'):
    mean = tf.reduce_mean(Weights)
    tf.summary.scalar('mean', mean)

y = tf.multiply(Weights, np.power(x_data, 2)) + biases

loss = tf.reduce_mean(tf.square(y - y_data))

optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)

init = tf.initialize_all_variables()
# create tensorflow structure end

sess = tf.Session()
sess.run(init)  # very important


# Merge all the summaries and write them out to /tmp/mnist_logs (by default)
merged = tf.summary.merge_all()
train_writer = tf.summary.FileWriter(FLAGS.summaries_dir + '/train',
                                      sess.graph)

for step in range(201):
    sess.run(train)
    if step % 20 == 0:
        print(step, sess.run(Weights), sess.run(biases))
        train_writer.add_summary(summary, i)
