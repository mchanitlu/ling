import sys

text = sys.stdin.read()

for c in text:
	if c == '.':
		sys.stdout.write(c + '\n')
	else:
		sys.stdout.write(c)
print(text)

