# import sys
import os
os.system("python /Users/wangxin/PycharmProjects/ParkingPaymentSystem/recoginzer_licenseplate.py 1>>log.txt")
# import time
# import random
#
# import numpy as np
# import tensorflow as tf
#
# from PIL import Image
#
# SIZE = 1280
# WIDTH = 32
# HEIGHT = 40
#
# NUM_CLASSES_P = 6
# iterations_P = 300
#
# NUM_CLASSES_L = 26
# iterations_L = 500
#
# NUM_CLASSES_D = 34
# iterations_D = 1000
#
# SAVER_DIR_P = "train-saver/province/"
# SAVER_DIR_L = "train-saver/letters/"
# SAVER_DIR_D = "train-saver/digits/"
#
# PROVINCES = ("京", "闽", "粤", "苏", "沪", "浙")
# nProvinceIndex = 0
#
# LETTERS_DIGITS_L = (
# "A", "B", "C", "D", "E", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
# "I", "O")
# # license_num = ""
#
# LETTERS_DIGITS_D = (
#     "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G", "H", "J", "K", "L", "M", "N",
#     "P",
#     "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z")
#
# time_begin = time.time()
#
# # 定义输入节点，对应于图片像素值矩阵集合和图片标签(即所代表的数字)
# x = tf.placeholder(tf.float32, shape=[None, SIZE])
# y_P = tf.placeholder(tf.float32, shape=[None, NUM_CLASSES_P])
# y_L = tf.placeholder(tf.float32, shape=[None, NUM_CLASSES_L])
# y_D = tf.placeholder(tf.float32, shape=[None, NUM_CLASSES_D])
#
# x_image = tf.reshape(x, [-1, WIDTH, HEIGHT, 1])
#
# # 定义卷积函数
# def conv_layer(inputs, W, b, conv_strides, kernel_size, pool_strides, padding):
#     L1_conv = tf.nn.conv2d(inputs, W, strides=conv_strides, padding=padding)
#     L1_relu = tf.nn.relu(L1_conv + b)
#     return tf.nn.max_pool(L1_relu, ksize=kernel_size, strides=pool_strides, padding='SAME')
#
# # 定义全连接层函数
# def full_connect(inputs, W, b):
#     return tf.nn.relu(tf.matmul(inputs, W) + b)
#
# #训练省份
# def train_province():
#     global iterations_P
#     global time_begin
# #if __name__ == '__main__' and sys.argv[1] == 'train':
#     # 第一次遍历图片目录是为了获取图片总数
#     input_count = 0
#     for i in range(0, NUM_CLASSES_P):
#         dir = './train_images/training-set/chinese-characters/%s/' % i  # 这里可以改成你自己的图片目录，i为分类标签
#         for rt, dirs, files in os.walk(dir):
#             for filename in files:
#                 input_count += 1
#
#     # 定义对应维数和各维长度的数组
#     input_images = np.array([[0] * SIZE for i in range(input_count)])
#     input_labels = np.array([[0] * NUM_CLASSES_P for i in range(input_count)])
#
#     # 第二次遍历图片目录是为了生成图片数据和标签
#     index = 0
#     for i in range(0, NUM_CLASSES_P):
#         dir = './train_images/training-set/chinese-characters/%s/' % i  # 这里可以改成你自己的图片目录，i为分类标签
#         for rt, dirs, files in os.walk(dir):
#             for filename in files:
#                 filename = dir + filename
#                 img = Image.open(filename)
#                 width = img.size[0]
#                 height = img.size[1]
#                 for h in range(0, height):
#                     for w in range(0, width):
#                         # 通过这样的处理，使数字的线条变细，有利于提高识别准确率
#                         if img.getpixel((w, h)) > 230:
#                             input_images[index][w + h * width] = 0
#                         else:
#                             input_images[index][w + h * width] = 1
#                 input_labels[index][i] = 1
#                 index += 1
#
#     # 第一次遍历图片目录是为了获取图片总数
#     val_count = 0
#     for i in range(0, NUM_CLASSES_P):
#         dir = './train_images/validation-set/chinese-characters/%s/' % i  # 这里可以改成你自己的图片目录，i为分类标签
#         for rt, dirs, files in os.walk(dir):
#             for filename in files:
#                 val_count += 1
#
#     # 定义对应维数和各维长度的数组
#     val_images = np.array([[0] * SIZE for i in range(val_count)])
#     val_labels = np.array([[0] * NUM_CLASSES_P for i in range(val_count)])
#
#     # 第二次遍历图片目录是为了生成图片数据和标签
#     index = 0
#     for i in range(0, NUM_CLASSES_P):
#         dir = './train_images/validation-set/chinese-characters/%s/' % i  # 这里可以改成你自己的图片目录，i为分类标签
#         for rt, dirs, files in os.walk(dir):
#             for filename in files:
#                 filename = dir + filename
#                 img = Image.open(filename)
#                 width = img.size[0]
#                 height = img.size[1]
#                 for h in range(0, height):
#                     for w in range(0, width):
#                         # 通过这样的处理，使数字的线条变细，有利于提高识别准确率
#                         if img.getpixel((w, h)) > 230:
#                             val_images[index][w + h * width] = 0
#                         else:
#                             val_images[index][w + h * width] = 1
#                 val_labels[index][i] = 1
#                 index += 1
#
#     with tf.Session() as sess:
#         # 第一个卷积层
#         W_conv1 = tf.Variable(tf.truncated_normal([8, 8, 1, 16], stddev=0.1), name="W_conv1")
#         b_conv1 = tf.Variable(tf.constant(0.1, shape=[16]), name="b_conv1")
#         conv_strides = [1, 1, 1, 1]
#         kernel_size = [1, 2, 2, 1]
#         pool_strides = [1, 2, 2, 1]
#         L1_pool = conv_layer(x_image, W_conv1, b_conv1, conv_strides, kernel_size, pool_strides, padding='SAME')
#
#         # 第二个卷积层
#         W_conv2 = tf.Variable(tf.truncated_normal([5, 5, 16, 32], stddev=0.1), name="W_conv2")
#         b_conv2 = tf.Variable(tf.constant(0.1, shape=[32]), name="b_conv2")
#         conv_strides = [1, 1, 1, 1]
#         kernel_size = [1, 1, 1, 1]
#         pool_strides = [1, 1, 1, 1]
#         L2_pool = conv_layer(L1_pool, W_conv2, b_conv2, conv_strides, kernel_size, pool_strides, padding='SAME')
#
#         # 全连接层
#         W_fc1 = tf.Variable(tf.truncated_normal([16 * 20 * 32, 512], stddev=0.1), name="W_fc1")
#         b_fc1 = tf.Variable(tf.constant(0.1, shape=[512]), name="b_fc1")
#         h_pool2_flat = tf.reshape(L2_pool, [-1, 16 * 20 * 32])
#         h_fc1 = full_connect(h_pool2_flat, W_fc1, b_fc1)
#
#         # dropout
#         keep_prob = tf.placeholder(tf.float32)
#
#         h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob)
#
#         # readout层
#         W_fc2 = tf.Variable(tf.truncated_normal([512, NUM_CLASSES_P], stddev=0.1), name="W_fc2")
#         b_fc2 = tf.Variable(tf.constant(0.1, shape=[NUM_CLASSES_P]), name="b_fc2")
#
#         # 定义优化器和训练op
#         y_conv = tf.matmul(h_fc1_drop, W_fc2) + b_fc2
#         cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y_P, logits=y_conv))
#         train_step = tf.train.AdamOptimizer((1e-4)).minimize(cross_entropy)
#
#         correct_prediction = tf.equal(tf.argmax(y_conv, 1), tf.argmax(y_P, 1))
#         accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
#
#         # 初始化saver
#         saver = tf.train.Saver()
#
#         sess.run(tf.global_variables_initializer())
#
#         time_elapsed = time.time() - time_begin
#         print("读取图片文件耗费时间：%d秒" % time_elapsed)
#         time_begin = time.time()
#
#         print("一共读取了 %s 个训练图像， %s 个标签" % (input_count, input_count))
#
#         # 设置每次训练op的输入个数和迭代次数，这里为了支持任意图片总数，定义了一个余数remainder，譬如，如果每次训练op的输入个数为60，图片总数为150张，则前面两次各输入60张，最后一次输入30张（余数30）
#         batch_size = 60
#         iterations_P = iterations_P
#         batches_count = int(input_count / batch_size)
#         remainder = input_count % batch_size
#         print("训练数据集分成 %s 批, 前面每批 %s 个数据，最后一批 %s 个数据" % (batches_count + 1, batch_size, remainder))
#
#         # 执行训练迭代
#         for it in range(iterations_P):
#             # 这里的关键是要把输入数组转为np.array
#             for n in range(batches_count):
#                 train_step.run(feed_dict={x: input_images[n * batch_size:(n + 1) * batch_size],
#                                           y_P: input_labels[n * batch_size:(n + 1) * batch_size], keep_prob: 0.5})
#             if remainder > 0:
#                 start_index = batches_count * batch_size;
#                 train_step.run(feed_dict={x: input_images[start_index:input_count - 1],
#                                           y_P: input_labels[start_index:input_count - 1], keep_prob: 0.5})
#
#             # 每完成五次迭代，判断准确度是否已达到100%，达到则退出迭代循环
#             iterate_accuracy = 0
#             if it % 5 == 0:
#                 iterate_accuracy = accuracy.eval(feed_dict={x: val_images, y_P: val_labels, keep_prob: 1.0})
#                 print('第 %d 次训练迭代: 准确率 %0.5f%%' % (it, iterate_accuracy * 100))
#                 if iterate_accuracy >= 0.9999 and it >= 150:
#                     break;
#
#         print('完成训练!')
#         time_elapsed = time.time() - time_begin
#         print("训练耗费时间：%d秒" % time_elapsed)
#         time_begin = time.time()
#
#         # 保存训练结果
#         if not os.path.exists(SAVER_DIR_P):
#             print('不存在训练数据保存目录，现在创建保存目录')
#             os.makedirs(SAVER_DIR_P)
#         saver_path = saver.save(sess, "%smodel.ckpt" % (SAVER_DIR_P))
#
# #训练城市代号
# def train_letters():
#     global iterations_L
#     global time_begin
# # if __name__ == '__main__' and sys.argv[1] == 'train':
#     # 第一次遍历图片目录是为了获取图片总数
#     input_count = 0
#     for i in range(0 + 10, NUM_CLASSES_L + 10):
#         dir = './train_images/training-set/letters/%s/' % i  # 这里可以改成你自己的图片目录，i为分类标签
#         for rt, dirs, files in os.walk(dir):
#             for filename in files:
#                 input_count += 1
#
#     # 定义对应维数和各维长度的数组
#     input_images = np.array([[0] * SIZE for i in range(input_count)])
#     input_labels = np.array([[0] * NUM_CLASSES_L for i in range(input_count)])
#
#     # 第二次遍历图片目录是为了生成图片数据和标签
#     index = 0
#     for i in range(0 + 10, NUM_CLASSES_L + 10):
#         dir = './train_images/training-set/letters/%s/' % i  # 这里可以改成你自己的图片目录，i为分类标签
#         for rt, dirs, files in os.walk(dir):
#             for filename in files:
#                 filename = dir + filename
#                 img = Image.open(filename)
#                 width = img.size[0]
#                 height = img.size[1]
#                 for h in range(0, height):
#                     for w in range(0, width):
#                         # 通过这样的处理，使数字的线条变细，有利于提高识别准确率
#                         if img.getpixel((w, h)) > 230:
#                             input_images[index][w + h * width] = 0
#                         else:
#                             input_images[index][w + h * width] = 1
#                 # print ("i=%d, index=%d" % (i, index))
#                 input_labels[index][i - 10] = 1
#                 index += 1
#
#     # 第一次遍历图片目录是为了获取图片总数
#     val_count = 0
#     for i in range(0 + 10, NUM_CLASSES_L + 10):
#         dir = './train_images/validation-set/%s/' % i  # 这里可以改成你自己的图片目录，i为分类标签
#         for rt, dirs, files in os.walk(dir):
#             for filename in files:
#                 val_count += 1
#
#     # 定义对应维数和各维长度的数组
#     val_images = np.array([[0] * SIZE for i in range(val_count)])
#     val_labels = np.array([[0] * NUM_CLASSES_L for i in range(val_count)])
#
#     # 第二次遍历图片目录是为了生成图片数据和标签
#     index = 0
#     for i in range(0 + 10, NUM_CLASSES_L + 10):
#         dir = './train_images/validation-set/%s/' % i  # 这里可以改成你自己的图片目录，i为分类标签
#         for rt, dirs, files in os.walk(dir):
#             for filename in files:
#                 filename = dir + filename
#                 img = Image.open(filename)
#                 width = img.size[0]
#                 height = img.size[1]
#                 for h in range(0, height):
#                     for w in range(0, width):
#                         # 通过这样的处理，使数字的线条变细，有利于提高识别准确率
#                         if img.getpixel((w, h)) > 230:
#                             val_images[index][w + h * width] = 0
#                         else:
#                             val_images[index][w + h * width] = 1
#                 val_labels[index][i - 10] = 1
#                 index += 1
#
#     with tf.Session() as sess:
#         # 第一个卷积层
#         W_conv1 = tf.Variable(tf.truncated_normal([8, 8, 1, 16], stddev=0.1), name="W_conv1")
#         b_conv1 = tf.Variable(tf.constant(0.1, shape=[16]), name="b_conv1")
#         conv_strides = [1, 1, 1, 1]
#         kernel_size = [1, 2, 2, 1]
#         pool_strides = [1, 2, 2, 1]
#         L1_pool = conv_layer(x_image, W_conv1, b_conv1, conv_strides, kernel_size, pool_strides, padding='SAME')
#
#         # 第二个卷积层
#         W_conv2 = tf.Variable(tf.truncated_normal([5, 5, 16, 32], stddev=0.1), name="W_conv2")
#         b_conv2 = tf.Variable(tf.constant(0.1, shape=[32]), name="b_conv2")
#         conv_strides = [1, 1, 1, 1]
#         kernel_size = [1, 1, 1, 1]
#         pool_strides = [1, 1, 1, 1]
#         L2_pool = conv_layer(L1_pool, W_conv2, b_conv2, conv_strides, kernel_size, pool_strides, padding='SAME')
#
#         # 全连接层
#         W_fc1 = tf.Variable(tf.truncated_normal([16 * 20 * 32, 512], stddev=0.1), name="W_fc1")
#         b_fc1 = tf.Variable(tf.constant(0.1, shape=[512]), name="b_fc1")
#         h_pool2_flat = tf.reshape(L2_pool, [-1, 16 * 20 * 32])
#         h_fc1 = full_connect(h_pool2_flat, W_fc1, b_fc1)
#
#         # dropout
#         keep_prob = tf.placeholder(tf.float32)
#
#         h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob)
#
#         # readout层
#         W_fc2 = tf.Variable(tf.truncated_normal([512, NUM_CLASSES_L], stddev=0.1), name="W_fc2")
#         b_fc2 = tf.Variable(tf.constant(0.1, shape=[NUM_CLASSES_L]), name="b_fc2")
#
#         # 定义优化器和训练op
#         y_conv = tf.matmul(h_fc1_drop, W_fc2) + b_fc2
#         cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y_L, logits=y_conv))
#         train_step = tf.train.AdamOptimizer((1e-4)).minimize(cross_entropy)
#
#         correct_prediction = tf.equal(tf.argmax(y_conv, 1), tf.argmax(y_L, 1))
#         accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
#
#         sess.run(tf.global_variables_initializer())
#
#         time_elapsed = time.time() - time_begin
#         print("读取图片文件耗费时间：%d秒" % time_elapsed)
#         time_begin = time.time()
#
#         print("一共读取了 %s 个训练图像， %s 个标签" % (input_count, input_count))
#
#         # 设置每次训练op的输入个数和迭代次数，这里为了支持任意图片总数，定义了一个余数remainder，譬如，如果每次训练op的输入个数为60，图片总数为150张，则前面两次各输入60张，最后一次输入30张（余数30）
#         batch_size = 60
#         iterations_L = iterations_L
#         batches_count = int(input_count / batch_size)
#         remainder = input_count % batch_size
#         print("训练数据集分成 %s 批, 前面每批 %s 个数据，最后一批 %s 个数据" % (batches_count + 1, batch_size, remainder))
#
#         # 执行训练迭代
#         for it in range(iterations_L):
#             # 这里的关键是要把输入数组转为np.array
#             for n in range(batches_count):
#                 train_step.run(feed_dict={x: input_images[n * batch_size:(n + 1) * batch_size],
#                                           y_L: input_labels[n * batch_size:(n + 1) * batch_size], keep_prob: 0.5})
#             if remainder > 0:
#                 start_index = batches_count * batch_size;
#                 train_step.run(feed_dict={x: input_images[start_index:input_count - 1],
#                                           y_L: input_labels[start_index:input_count - 1], keep_prob: 0.5})
#
#             # 每完成五次迭代，判断准确度是否已达到100%，达到则退出迭代循环
#             iterate_accuracy = 0
#             if it % 5 == 0:
#                 iterate_accuracy = accuracy.eval(feed_dict={x: val_images, y_L: val_labels, keep_prob: 1.0})
#                 print('第 %d 次训练迭代: 准确率 %0.5f%%' % (it, iterate_accuracy * 100))
#                 if iterate_accuracy >= 0.9999 and it >= iterations_L:
#                     break;
#
#         print('完成训练!')
#         time_elapsed = time.time() - time_begin
#         print("训练耗费时间：%d秒" % time_elapsed)
#         time_begin = time.time()
#
#         # 保存训练结果
#         if not os.path.exists(SAVER_DIR_L):
#             print('不存在训练数据保存目录，现在创建保存目录')
#             os.makedirs(SAVER_DIR_L)
#         # 初始化saver
#         saver = tf.train.Saver()
#         saver_path = saver.save(sess, "%smodel.ckpt" % (SAVER_DIR_L))
#
# #训练车牌字母与数字
# def train_digits():
#     global time_begin
#     global iterations_D
# # if __name__ == '__main__' and sys.argv[1] == 'train':
#     # 第一次遍历图片目录是为了获取图片总数
#     input_count = 0
#     for i in range(0, NUM_CLASSES_D):
#         dir = './train_images/training-set/%s/' % i  # 这里可以改成你自己的图片目录，i为分类标签
#         for rt, dirs, files in os.walk(dir):
#             for filename in files:
#                 input_count += 1
#
#     # 定义对应维数和各维长度的数组
#     input_images = np.array([[0] * SIZE for i in range(input_count)])
#     input_labels = np.array([[0] * NUM_CLASSES_D for i in range(input_count)])
#
#     # 第二次遍历图片目录是为了生成图片数据和标签
#     index = 0
#     for i in range(0, NUM_CLASSES_D):
#         dir = './train_images/training-set/%s/' % i  # 这里可以改成你自己的图片目录，i为分类标签
#         for rt, dirs, files in os.walk(dir):
#             for filename in files:
#                 filename = dir + filename
#                 img = Image.open(filename)
#                 width = img.size[0]
#                 height = img.size[1]
#                 for h in range(0, height):
#                     for w in range(0, width):
#                         # 通过这样的处理，使数字的线条变细，有利于提高识别准确率
#                         if img.getpixel((w, h)) > 230:
#                             input_images[index][w + h * width] = 0
#                         else:
#                             input_images[index][w + h * width] = 1
#                 input_labels[index][i] = 1
#                 index += 1
#
#     # 第一次遍历图片目录是为了获取图片总数
#     val_count = 0
#     for i in range(0, NUM_CLASSES_D):
#         dir = './train_images/validation-set/%s/' % i  # i为分类标签
#         for rt, dirs, files in os.walk(dir):
#             for filename in files:
#                 val_count += 1
#
#     # 定义对应维数和各维长度的数组
#     val_images = np.array([[0] * SIZE for i in range(val_count)])
#     val_labels = np.array([[0] * NUM_CLASSES_D for i in range(val_count)])
#
#     # 第二次遍历图片目录是为了生成图片数据和标签
#     index = 0
#     for i in range(0, NUM_CLASSES_D):
#         dir = './train_images/validation-set/%s/' % i  # 这里可以改成你自己的图片目录，i为分类标签
#         for rt, dirs, files in os.walk(dir):
#             for filename in files:
#                 filename = dir + filename
#                 img = Image.open(filename)
#                 width = img.size[0]
#                 height = img.size[1]
#                 for h in range(0, height):
#                     for w in range(0, width):
#                         # 通过这样的处理，使数字的线条变细，有利于提高识别准确率
#                         if img.getpixel((w, h)) > 230:
#                             val_images[index][w + h * width] = 0
#                         else:
#                             val_images[index][w + h * width] = 1
#                 val_labels[index][i] = 1
#                 index += 1
#
#     with tf.Session() as sess:
#         # 第一个卷积层
#         W_conv1 = tf.Variable(tf.truncated_normal([8, 8, 1, 16], stddev=0.1), name="W_conv1")
#         b_conv1 = tf.Variable(tf.constant(0.1, shape=[16]), name="b_conv1")
#         conv_strides = [1, 1, 1, 1]
#         kernel_size = [1, 2, 2, 1]
#         pool_strides = [1, 2, 2, 1]
#         L1_pool = conv_layer(x_image, W_conv1, b_conv1, conv_strides, kernel_size, pool_strides, padding='SAME')
#
#         # 第二个卷积层
#         W_conv2 = tf.Variable(tf.truncated_normal([5, 5, 16, 32], stddev=0.1), name="W_conv2")
#         b_conv2 = tf.Variable(tf.constant(0.1, shape=[32]), name="b_conv2")
#         conv_strides = [1, 1, 1, 1]
#         kernel_size = [1, 1, 1, 1]
#         pool_strides = [1, 1, 1, 1]
#         L2_pool = conv_layer(L1_pool, W_conv2, b_conv2, conv_strides, kernel_size, pool_strides, padding='SAME')
#
#         # 全连接层
#         W_fc1 = tf.Variable(tf.truncated_normal([16 * 20 * 32, 512], stddev=0.1), name="W_fc1")
#         b_fc1 = tf.Variable(tf.constant(0.1, shape=[512]), name="b_fc1")
#         h_pool2_flat = tf.reshape(L2_pool, [-1, 16 * 20 * 32])
#         h_fc1 = full_connect(h_pool2_flat, W_fc1, b_fc1)
#
#         # dropout
#         keep_prob = tf.placeholder(tf.float32)
#
#         h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob)
#
#         # readout层
#         W_fc2 = tf.Variable(tf.truncated_normal([512, NUM_CLASSES_D], stddev=0.1), name="W_fc2")
#         b_fc2 = tf.Variable(tf.constant(0.1, shape=[NUM_CLASSES_D]), name="b_fc2")
#
#         # 定义优化器和训练op
#         y_conv = tf.matmul(h_fc1_drop, W_fc2) + b_fc2
#         cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y_D, logits=y_conv))
#         train_step = tf.train.AdamOptimizer((1e-4)).minimize(cross_entropy)
#
#         correct_prediction = tf.equal(tf.argmax(y_conv, 1), tf.argmax(y_D, 1))
#         accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
#
#         sess.run(tf.global_variables_initializer())
#
#         time_elapsed = time.time() - time_begin
#         print("读取图片文件耗费时间：%d秒" % time_elapsed)
#         time_begin = time.time()
#
#         print("一共读取了 %s 个训练图像， %s 个标签" % (input_count, input_count))
#
#         # 设置每次训练op的输入个数和迭代次数，这里为了支持任意图片总数，定义了一个余数remainder，譬如，如果每次训练op的输入个数为60，图片总数为150张，则前面两次各输入60张，最后一次输入30张（余数30）
#         batch_size = 60
#         iterations_D = iterations_D
#         batches_count = int(input_count / batch_size)
#         remainder = input_count % batch_size
#         print("训练数据集分成 %s 批, 前面每批 %s 个数据，最后一批 %s 个数据" % (batches_count + 1, batch_size, remainder))
#
#         # 执行训练迭代
#         for it in range(iterations_D):
#             # 这里的关键是要把输入数组转为np.array
#             for n in range(batches_count):
#                 train_step.run(feed_dict={x: input_images[n * batch_size:(n + 1) * batch_size],
#                                           y_D: input_labels[n * batch_size:(n + 1) * batch_size], keep_prob: 0.5})
#             if remainder > 0:
#                 start_index = batches_count * batch_size;
#                 train_step.run(feed_dict={x: input_images[start_index:input_count - 1],
#                                           y_D: input_labels[start_index:input_count - 1], keep_prob: 0.5})
#
#             # 每完成五次迭代，判断准确度是否已达到100%，达到则退出迭代循环
#             iterate_accuracy = 0
#             if it % 5 == 0:
#                 iterate_accuracy = accuracy.eval(feed_dict={x: val_images, y_D: val_labels, keep_prob: 1.0})
#                 print('第 %d 次训练迭代: 准确率 %0.5f%%' % (it, iterate_accuracy * 100))
#                 if iterate_accuracy >= 0.9999 and it >= iterations_D:
#                     break;
#
#         print('完成训练!')
#         time_elapsed = time.time() - time_begin
#         print("训练耗费时间：%d秒" % time_elapsed)
#         time_begin = time.time()
#
#         # 保存训练结果
#         if not os.path.exists(SAVER_DIR_D):
#             print('不存在训练数据保存目录，现在创建保存目录')
#             os.makedirs(SAVER_DIR_D)
#         # 初始化saver
#         saver = tf.train.Saver()
#         saver_path = saver.save(sess, "%smodel.ckpt" % (SAVER_DIR_D))
#
# #识别省份
# def recognizer_P():
# #if __name__ == '__main__' and sys.argv[1] == 'predict':
#     saver = tf.train.import_meta_graph("%smodel.ckpt.meta" % (SAVER_DIR_P))
#     with tf.Session() as sess:
#         model_file = tf.train.latest_checkpoint(SAVER_DIR_P)
#         saver.restore(sess, model_file)
#
#         # 第一个卷积层
#         W_conv1 = sess.graph.get_tensor_by_name("W_conv1:0")
#         b_conv1 = sess.graph.get_tensor_by_name("b_conv1:0")
#         conv_strides = [1, 1, 1, 1]
#         kernel_size = [1, 2, 2, 1]
#         pool_strides = [1, 2, 2, 1]
#         L1_pool = conv_layer(x_image, W_conv1, b_conv1, conv_strides, kernel_size, pool_strides, padding='SAME')
#
#         # 第二个卷积层
#         W_conv2 = sess.graph.get_tensor_by_name("W_conv2:0")
#         b_conv2 = sess.graph.get_tensor_by_name("b_conv2:0")
#         conv_strides = [1, 1, 1, 1]
#         kernel_size = [1, 1, 1, 1]
#         pool_strides = [1, 1, 1, 1]
#         L2_pool = conv_layer(L1_pool, W_conv2, b_conv2, conv_strides, kernel_size, pool_strides, padding='SAME')
#
#         # 全连接层
#         W_fc1 = sess.graph.get_tensor_by_name("W_fc1:0")
#         b_fc1 = sess.graph.get_tensor_by_name("b_fc1:0")
#         h_pool2_flat = tf.reshape(L2_pool, [-1, 16 * 20 * 32])
#         h_fc1 = full_connect(h_pool2_flat, W_fc1, b_fc1)
#
#         # dropout
#         keep_prob = tf.placeholder(tf.float32)
#
#         h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob)
#
#         # readout层
#         W_fc2 = sess.graph.get_tensor_by_name("W_fc2:0")
#         b_fc2 = sess.graph.get_tensor_by_name("b_fc2:0")
#
#         # 定义优化器和训练op
#         conv = tf.nn.softmax(tf.matmul(h_fc1_drop, W_fc2) + b_fc2)
#
#         for n in range(1, 2):
#             path = "test_images/%s.bmp" % (n)
#             img = Image.open(path)
#             width = img.size[0]
#             height = img.size[1]
#
#             img_data = [[0] * SIZE for i in range(1)]
#             for h in range(0, height):
#                 for w in range(0, width):
#                     if img.getpixel((w, h)) < 190:
#                         img_data[0][w + h * width] = 1
#                     else:
#                         img_data[0][w + h * width] = 0
#
#             result = sess.run(conv, feed_dict={x: np.array(img_data), keep_prob: 1.0})
#             max1 = 0
#             max2 = 0
#             max3 = 0
#             max1_index = 0
#             max2_index = 0
#             max3_index = 0
#             for j in range(NUM_CLASSES_P):
#                 if result[0][j] > max1:
#                     max1 = result[0][j]
#                     max1_index = j
#                     continue
#                 if (result[0][j] > max2) and (result[0][j] <= max1):
#                     max2 = result[0][j]
#                     max2_index = j
#                     continue
#                 if (result[0][j] > max3) and (result[0][j] <= max2):
#                     max3 = result[0][j]
#                     max3_index = j
#                     continue
#
#             nProvinceIndex = max1_index
#             # print("概率：  [%s %0.2f%%]    [%s %0.2f%%]    [%s %0.2f%%]" % (PROVINCES[max1_index], max1 * 100, PROVINCES[max2_index], max2 * 100, PROVINCES[max3_index], max3 * 100))
#
#         print("省份简称是: %s" % PROVINCES[nProvinceIndex])
#         return PROVINCES[nProvinceIndex]
# #识别城市代号
# def recoginzer_L():
#     license_num =''
# # if __name__ == '__main__' and sys.argv[1] == 'predict':
#     saver = tf.train.import_meta_graph("%smodel.ckpt.meta" % (SAVER_DIR_L))
#     with tf.Session() as sess:
#         model_file = tf.train.latest_checkpoint(SAVER_DIR_L)
#         saver.restore(sess, model_file)
#
#         # 第一个卷积层
#         W_conv1 = sess.graph.get_tensor_by_name("W_conv1:0")
#         b_conv1 = sess.graph.get_tensor_by_name("b_conv1:0")
#         conv_strides = [1, 1, 1, 1]
#         kernel_size = [1, 2, 2, 1]
#         pool_strides = [1, 2, 2, 1]
#         L1_pool = conv_layer(x_image, W_conv1, b_conv1, conv_strides, kernel_size, pool_strides, padding='SAME')
#
#         # 第二个卷积层
#         W_conv2 = sess.graph.get_tensor_by_name("W_conv2:0")
#         b_conv2 = sess.graph.get_tensor_by_name("b_conv2:0")
#         conv_strides = [1, 1, 1, 1]
#         kernel_size = [1, 1, 1, 1]
#         pool_strides = [1, 1, 1, 1]
#         L2_pool = conv_layer(L1_pool, W_conv2, b_conv2, conv_strides, kernel_size, pool_strides, padding='SAME')
#
#         # 全连接层
#         W_fc1 = sess.graph.get_tensor_by_name("W_fc1:0")
#         b_fc1 = sess.graph.get_tensor_by_name("b_fc1:0")
#         h_pool2_flat = tf.reshape(L2_pool, [-1, 16 * 20 * 32])
#         h_fc1 = full_connect(h_pool2_flat, W_fc1, b_fc1)
#
#         # dropout
#         keep_prob = tf.placeholder(tf.float32)
#
#         h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob)
#
#         # readout层
#         W_fc2 = sess.graph.get_tensor_by_name("W_fc2:0")
#         b_fc2 = sess.graph.get_tensor_by_name("b_fc2:0")
#
#         # 定义优化器和训练op
#         conv = tf.nn.softmax(tf.matmul(h_fc1_drop, W_fc2) + b_fc2)
#
#         for n in range(2, 3):
#             path = "test_images/%s.bmp" % (n)
#             img = Image.open(path)
#             width = img.size[0]
#             height = img.size[1]
#
#             img_data = [[0] * SIZE for i in range(1)]
#             for h in range(0, height):
#                 for w in range(0, width):
#                     if img.getpixel((w, h)) < 190:
#                         img_data[0][w + h * width] = 1
#                     else:
#                         img_data[0][w + h * width] = 0
#
#             result = sess.run(conv, feed_dict={x: np.array(img_data), keep_prob: 1.0})
#
#             max1 = 0
#             max2 = 0
#             max3 = 0
#             max1_index = 0
#             max2_index = 0
#             max3_index = 0
#             for j in range(NUM_CLASSES_L):
#                 if result[0][j] > max1:
#                     max1 = result[0][j]
#                     max1_index = j
#                     continue
#                 if (result[0][j] > max2) and (result[0][j] <= max1):
#                     max2 = result[0][j]
#                     max2_index = j
#                     continue
#                 if (result[0][j] > max3) and (result[0][j] <= max2):
#                     max3 = result[0][j]
#                     max3_index = j
#                     continue
#
#             if n == 3:
#                 license_num += "-"
#             license_num = license_num + LETTERS_DIGITS_L[max1_index]
#             # print("概率：  [%s %0.2f%%]    [%s %0.2f%%]    [%s %0.2f%%]" % (
#             # LETTERS_DIGITS_L[max1_index], max1 * 100, LETTERS_DIGITS_L[max2_index], max2 * 100, LETTERS_DIGITS_L[max3_index],
#             # max3 * 100))
#
#         # print("城市代号是: 【%s】" % license_num)
#         return license_num
# #识别车牌字母与数字
# def recoginzer_D():
#     license_num =''
# # if __name__ == '__main__' and sys.argv[1] == 'predict':
#     saver = tf.train.import_meta_graph("%smodel.ckpt.meta" % (SAVER_DIR_D))
#     with tf.Session() as sess:
#         model_file = tf.train.latest_checkpoint(SAVER_DIR_D)
#         saver.restore(sess, model_file)
#
#         # 第一个卷积层
#         W_conv1 = sess.graph.get_tensor_by_name("W_conv1:0")
#         b_conv1 = sess.graph.get_tensor_by_name("b_conv1:0")
#         conv_strides = [1, 1, 1, 1]
#         kernel_size = [1, 2, 2, 1]
#         pool_strides = [1, 2, 2, 1]
#         L1_pool = conv_layer(x_image, W_conv1, b_conv1, conv_strides, kernel_size, pool_strides, padding='SAME')
#
#         # 第二个卷积层
#         W_conv2 = sess.graph.get_tensor_by_name("W_conv2:0")
#         b_conv2 = sess.graph.get_tensor_by_name("b_conv2:0")
#         conv_strides = [1, 1, 1, 1]
#         kernel_size = [1, 1, 1, 1]
#         pool_strides = [1, 1, 1, 1]
#         L2_pool = conv_layer(L1_pool, W_conv2, b_conv2, conv_strides, kernel_size, pool_strides, padding='SAME')
#
#         # 全连接层
#         W_fc1 = sess.graph.get_tensor_by_name("W_fc1:0")
#         b_fc1 = sess.graph.get_tensor_by_name("b_fc1:0")
#         h_pool2_flat = tf.reshape(L2_pool, [-1, 16 * 20 * 32])
#         h_fc1 = full_connect(h_pool2_flat, W_fc1, b_fc1)
#
#         # dropout
#         keep_prob = tf.placeholder(tf.float32)
#
#         h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob)
#
#         # readout层
#         W_fc2 = sess.graph.get_tensor_by_name("W_fc2:0")
#         b_fc2 = sess.graph.get_tensor_by_name("b_fc2:0")
#
#         # 定义优化器和训练op
#         conv = tf.nn.softmax(tf.matmul(h_fc1_drop, W_fc2) + b_fc2)
#
#         for n in range(3, 8):
#             path = "test_images/%s.bmp" % (n)
#             img = Image.open(path)
#             width = img.size[0]
#             height = img.size[1]
#
#             img_data = [[0] * SIZE for i in range(1)]
#             for h in range(0, height):
#                 for w in range(0, width):
#                     if img.getpixel((w, h)) < 190:
#                         img_data[0][w + h * width] = 1
#                     else:
#                         img_data[0][w + h * width] = 0
#
#             result = sess.run(conv, feed_dict={x: np.array(img_data), keep_prob: 1.0})
#
#             max1 = 0
#             max2 = 0
#             max3 = 0
#             max1_index = 0
#             max2_index = 0
#             max3_index = 0
#             for j in range(NUM_CLASSES_D):
#                 if result[0][j] > max1:
#                     max1 = result[0][j]
#                     max1_index = j
#                     continue
#                 if (result[0][j] > max2) and (result[0][j] <= max1):
#                     max2 = result[0][j]
#                     max2_index = j
#                     continue
#                 if (result[0][j] > max3) and (result[0][j] <= max2):
#                     max3 = result[0][j]
#                     max3_index = j
#                     continue
#
#             license_num = license_num + LETTERS_DIGITS_D[max1_index]
#             # print("概率：  [%s %0.2f%%]    [%s %0.2f%%]    [%s %0.2f%%]" % (
#             #     LETTERS_DIGITS[max1_index], max1 * 100, LETTERS_DIGITS[max2_index], max2 * 100,
#             #     LETTERS_DIGITS[max3_index],
#             #     max3 * 100))
#
#         print("车牌编号是: 【%s】" % license_num)
#         return license_num
#
#
#
# #
# # if __name__ =='__main__':
# # dd=recoginzer_D()
#
# # pp=recognizer_P()
#
# # ll=recoginzer_L()
# #     recognizer_P()
# # print(ll)