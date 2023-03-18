import os

print('''
	This is a script to mass compress images using jpegoptim. You must have jpegoptim installed in order to use this script.
	Recommended settings for fast websites are as follows:
	Max MB: 0.1 MB
	Compression: 70
	------------------------------------------------------------
	Recommended settings for regular users is as follows:
	Max MB: 1 MB
	Compression: 75

	''')

max_mb = float(input('Enter max MB for images: '))
compression = int(input('Enter compression percentage (0-100): '))



for file in os.listdir():
	if file.endswith('JPG'):
		if os.stat(file).st_size > (max_mb * 1_000_000):
			print(f'File: {file}')
			print("Old size: " + str(os.stat(file).st_size / 1_000_000) + " MB")
			os.system(f'jpegoptim \'{file}\' --force --max={compression}')
			print("New size: " + str(os.stat(file).st_size / 1_000_000) + " MB")
			print("-----------------------")
