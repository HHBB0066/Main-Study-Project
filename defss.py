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
	if x not in DB.DB:
		print("sorry this number isn't in DB")
def remove():
        x = int(input('num for remove in DB: '))
        rmv = DB.DB[x]
        DB.DB.remove(rmv)
        print('removed')
