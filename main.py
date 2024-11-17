import os

class SETTINGS:
	MB = 1_048_576 # in bytes

print('''
	This is a script to mass compress images using jpegoptim. You must have jpegoptim installed in order to use this script.
	Recommended settings for fast websites are as follows:
	Min MB: 0.1 MB
	Compression: 70
	------------------------------------------------------------
	Recommended settings for regular users is as follows:
	Min MB: 1 MB
	Compression: 75

	''')

min_mb = float(input('Enter minimum size of images to compress in MB: '))
compression = int(input('Enter compression percentage (0-100): '))



for file in os.listdir():
	if file.upper().endswith('JPG'):
		if os.stat(file).st_size > (min_mb * SETTINGS.MB):
			print(f'File: {file}')
			print("Old size: " + str(os.stat(file).st_size / SETTINGS.MB) + " MB")
			os.system(f'jpegoptim \'{file}\' --force --max={compression}')
			print("New size: " + str(os.stat(file).st_size / SETTINGS.MB) + " MB")
			print("-----------------------")
