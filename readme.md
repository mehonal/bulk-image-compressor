Status: Functional but lacks testing

This is a script to mass compress images using jpegoptim. You must have jpegoptim installed in order to use this script.

# How to use the script
The script is fairly easy to use. It is placed in the folder containing the photos to compress, then run. The script will ask the following:
- Min MB: this refers to the minimum MB a file must be in order to be compressed. If a file is smaller than the provided Min MB, it will be bypassed.
- Compression: This is the compression percentage value (from 0 to 100). The lower this value is, the smaller the file size will be. Similarly, the lower this value is, the lower the images' quality will be. 

# Recommended Settings
## Websites
Recommended settings for fast websites are as follows:
- Min MB: 0.1 MB
- Compression: 70
## Regular photos
Recommended settings for regular users is as follows:
- Min MB: 1 MB
- Compression: 75
