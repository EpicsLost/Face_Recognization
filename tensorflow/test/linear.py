import tensorflow as tf

x = tf.placeholder(tf.float32)
W = tf.Variable(tf.zeros([1]))
b = tf.Variable(tf.zeros([1]))
y_ = tf.placeholder(tf.float32)


y = W * x + b
lost = tf.reduce_mean(tf.square(y-y_))
optimizer = tf.train.GradientDescentOptimizer(0.0000001)
train_step = optimizer.minimize(lost)

sess = tf.Session()
init = tf.global_variables_initializer()
sess.run(init)

step = 1000
for i in range(step):
    xs = [i]
    ys = [3*i]
    feed = {x:xs,y_:ys}
    sess.run(train_step,feed_dict=feed)
    if i%100 == 0:
        print("After %d iteration:"%i)
        print("W:%f"%sess.run(W))
        print("b:%f"%sess.run(b))
        print("lost:%f"%sess.run(lost,feed_dict=feed))