import os

print('''
	This is a script to mass compress images using jpegoptim.
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
			print("Old size: " + str(os.stat(file).st_size / 1_000_000) + " MB")
			os.system(f'jpegoptim \'{file}\' --force --max={compression}')
			print(f'Compressed: {file}')
			print("New size: " + str(os.stat(file).st_size / 1_000_000) + " MB")
			print("-----------------------")
