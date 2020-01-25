import tensorflow as tf


with tf.compat.v1.Session() as sess:
    x= tf.Variable(3, name="x")
    y= tf.Variable(4, name="x")
    f = x*x*y + y + 2

    sess.run(x.initializer)
    sess.run(y.initializer)
    result = sess.run(f)
    print(result)
