import random
from Demo import Demo

try:
	if __name__ == '__main__':
		code = [chr(i) for i in range(97, 123)]
		random.shuffle(code)
		code_str = "".join(code)
		print()
		print(code_str)
		print()
		d = Demo(1985)
		d.hello()
		version = 5
		abc = 10
		raise ValueError("state with version %s passed to "
                             "Random.setstate() of version %s" %
                             (version, abc)) #當有多個值需要被CALL的時候 就用%()
except Exception, WhatHappen:
	print WhatHappen