from PIL import Image
import sys

filename = sys.argv[1]
string = "..1743569" 
string_len = len(string)-1

im = Image.open(filename).convert('L')
aspect = im.width/im.height
h = 40
w = int(h*aspect)
if (w>140):
	w = 140
	h = int(w//aspect)
final = im.resize((w,h))

w = final.width
h = final.height
final_string = []

for i in range(h):
	temp_string = ""
	for j in range(w):
		pixel = final.getpixel((j,i))
		temp_string += string[pixel*string_len//255]
	final_string.append(temp_string)
	print(temp_string)