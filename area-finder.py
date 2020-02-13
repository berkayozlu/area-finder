while True:
	print ("The Great Formula Of Recipient")
	a = int(input("Birinci kenar:\n"))
	b = int(input("İkinci kenar:\n"))
	c = int(input("Ucuncu kenar:\n"))
	u = (a + b + c ) / 2
	alan = (u*(u-a)*(u-b)*(u-c))**0.5
	print ("Ucgenin alani: {}".format(alan))