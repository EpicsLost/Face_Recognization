import tensorflow as tf
# 全0
v1 = tf.get_variable('v1', shape=[5], initializer=tf.zeros_initializer())
# 全1
v2 = tf.get_variable('v2', shape=[5], initializer=tf.ones_initializer())

v3 = tf.get_variable('v3',shape=[3,2], initializer=tf.constant_initializer([[1,2],[3,4],[5,6]]))


with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    print(v1.eval())
    print(sess.run(v1))
    print(v2.eval())
    print(v3.eval())

