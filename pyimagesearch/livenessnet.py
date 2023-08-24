# import the necessary packages
from keras.src.layers.core import Flatten
from keras.src.layers.core import Dropout
from keras.src.layers.core import Dense
from keras.models import Model
from keras.applications.resnet50 import ResNet50

# from tensorflow.python.keras.models import Model
# from tensorflow.python.keras.layers import Flatten, Dense, Dropout
# from tensorflow.python.keras.applications import ResNet50
# from tensorflow.python.keras.models import Sequential


class LivenessNet:
	@staticmethod
	def build(width, height, depth, classes):

		# net = ResNet50(include_top=False, weights='imagenet', input_tensor=None,
		# 			   input_shape=(width, height, depth))
		# res = net.output
		# res = GlobalAveragePooling2D()(res)
		# fc = Dense(classes, activation='softmax', name='fc1000')(res)
		# model = Model(inputs=net.input, outputs=fc)

		net = ResNet50(include_top=False, weights='imagenet', input_tensor=None, input_shape=(width, height, depth))
		res = net.output
		res = Flatten()(res)
		res = Dropout(0.5)(res)
		fc = Dense(classes, activation='softmax', name='fc2')(res)
		model = Model(inputs=net.input, outputs=fc)

		# model = Sequential()
		# model.add(ResNet50(include_top=False, pooling='avg', weights='imagenet', input_shape=(width, height, depth)))
		# model.add(Flatten())
		# # model.add(BatchNormalization())
		# model.add(Dense(classes, activation='softmax', name='fc2'))

		# return the constructed network architecture

		return model
