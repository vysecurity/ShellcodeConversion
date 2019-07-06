import sys
import base64
import codecs

f = open(sys.argv[1],"r")
s = f.read()
hex_list = ["{:02x}".format(ord(c)) for c in s]

size = len(hex_list)

reverse = hex_list[::-1]

print base64.b64encode(''.join(reverse).decode("hex"))
