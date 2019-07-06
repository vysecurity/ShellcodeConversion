import sys

f = open(sys.argv[1],"r")
s = f.read()
hex_list = ["{:02x}".format(ord(c)) for c in s]

str = ""

for a in hex_list[::-1]:
	str += "0x{}, ".format(a)

size = len(hex_list)
str = str[:-2]

template = """public static byte[] sc = new byte[{}]
{{
	{}
}};
"""

output = template.format(size, str)

print output
