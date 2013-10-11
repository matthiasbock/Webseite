#!/usr/bin/python

from subprocess import Popen, PIPE
from shlex import split
from PIL import Image

files = Popen(split('find . -iname "*.jpg"'), stdout=PIPE).communicate()[0].strip().split("\n")
#files = ["2013-03-25 13.25.17.jpg"]

max_width = 1024

for file in files:
	try:
		im = Image.open(file)
		print file+" - "+str(im.size) # (height,width) tuple
		if im.size[0] > max_width:
			percentage = str(int(max_width*100/im.size[0]))
			cmd = 'mogrify -scale '+percentage+'% -quality 85% "'+file+'"'
			print cmd
			Popen(split(cmd)).wait()
	except:
		pass
