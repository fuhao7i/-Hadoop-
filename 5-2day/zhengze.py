import re
def main():
	string = "a123173875843759345098b"
	pattern = re.compile('a(.*)b')
	ret =pattern.findall(string)
	print ret


if __name__ == "__main__":
	main()
