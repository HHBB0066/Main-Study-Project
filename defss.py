import DB
def rpp():
    python = sys.executable
    os.execl(python, python, * sys.argv)
def add(x):
	DB.DB.append(x)
	print('Added')
def acss():
	x = int(input('num for DB: '))
	print(DB.DB[x])