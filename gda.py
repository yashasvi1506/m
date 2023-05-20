import numpy as np
import tensorflow as tf
x_train = np.random.rand(100, 1) * 10
y_train = 2 * x_train - 3 + np.random.randn(100, 1)
model = tf.keras.Sequential([tf.keras.layers.Dense(units=1, input_shape=[1])])
loss_fn = tf.keras.losses.MeanSquaredError()
optimizer = tf.keras.optimizers.SGD(learning_rate=0.01)
train_dataset = tf.data.Dataset.from_tensor_slices((x_train, y_train)).batch(32)
for epoch in range(1000):
  for x_batch, y_batch in train_dataset:
    with tf.GradientTape() as tape:
      y_pred = model(x_batch)
      loss = loss_fn(y_batch, y_pred)
    gradients = tape.gradient(loss, model.trainable_variables)
    optimizer.apply_gradients(zip(gradientsgradientsgradientsgradients, model.trainable_variables))
    if epoch % 100 == 0:
      print("Epoch {}: w = {}, b = {}".formatformatformatformat(epoch, model.get_weights()[0], model.get_weights()[1]))
      model.get_weights()
