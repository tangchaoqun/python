from PIL import Image
import os

for file in os.listdir('origin'):
	if file.endswith('.jpg'):
		image_file=Image.open(os.path.join('origin',file))
		image_file=image_file.convert('L')
		image_file.save(os.path.join('result',file[:-4]+'_grey.png'))

