import tensorflow as tf

num = tf.Variable(111,name='num')
init = tf.initialize_all_variables()

with tf.Session() as sess:
    sess.run(init)
    print(sess.run(num))