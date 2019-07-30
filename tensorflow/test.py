import tensorflow as tf

data = tf.constant("hello")
print(data)

a = tf.placeholder(tf.int32)
b = tf.placeholder(tf.int32)

add = tf.add(a,b)
mul = tf.multiply(a,b)
c = tf.constant([[2,3]])
d = tf.constant([[4],[5]])
matmul = tf.matmul(c,d)

init = tf.global_variables_initializer()
a2 = tf.get_variable('a2', shape=[1], initializer=tf.constant_initializer(1))

with tf.Session() as sess:
    sess.run(init)
    print("add:%i"%sess.run(add,feed_dict={a:2,b:3}))
    print("mul:%i"%sess.run(mul,feed_dict={a:3,b:4}))
    print(sess.run(matmul))
    print(sess.run(a2))


