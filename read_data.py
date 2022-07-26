# reads in data from video and annotations file
# eventually want to save images to training folder on github
import numpy as np
import cv2
import os

labels = {
    'no label': 0,
    'tongue': 1,
    'paw': 2,
    'groom': 3,
    'air lick': 4,
    'chin': 5,
    'air groom': 6,
    'no contact': 7,
    'tongue out': 8,
    'ambiguous': 9,
}

# class to read in video and annotations
class readVideoAnnotations():
	def __init__(self, video_path, annotations_path):
		self.vidPath = video_path
		self.anPath = annotations_path

		if not os.path.exists('./images'):
			for key in labels:
				os.makedirs('./images/%s' %(key))


	def readAnnotations(self):
		self.annotations = np.load(self.anPath)['lickStates']
		print(set(self.annotations))

	def readVideo(self):
		self.vid = cv2.VideoCapture(self.vidPath)
		print(self.vid.get(cv2.CAP_PROP_FRAME_COUNT))

		success,image = self.vid.read()
		count = 0

		while success:
			success,image = self.vid.read()
			#print('Read a new frame: ', success)
			count += 1

		print(count)

if __name__ == '__main__':
	folder = '//10.128.50.43/sd6.3/habituation/'
	vidFile = '1047487717_521466_20200831/1047487717_521466_20200831.behavior.mp4'
	annotationFile = '1047487717_521466_20200831/1047487717_521466_20200831.behavior_08312020_212513_sync.npz'
	readData = readVideoAnnotations(folder + vidFile, folder + annotationFile)

	readData.readAnnotations()
	readData.readVideo()

 
