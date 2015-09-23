import sys

def extract(sys_argv):
	r = to_hex(sys_argv[1])
	g = to_hex(sys_argv[2])
	b = to_hex(sys_argv[3])

	return r+g+b

def to_hex(number_str):
	hex_str = hex(int(number_str)).split('x')[1]
	if len(hex_str) < 2:
		hex_str = '0' + hex_str
	
	return hex_str.upper()

# name of file is considered an argument
num_of_args = len(sys.argv) - 1;

if num_of_args != 3:
	print 'Wrong number of arguments ('+str(num_of_args)+' of 3 required: <command> [R] [G] [B])'
else:
	hex = extract(sys.argv)
	print '#'+hex


