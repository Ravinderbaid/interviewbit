class A:
	def __init__(self,*args):
		args=args[0]
		self.name = args[0]
		self.height = args[1]
	def g(self):
		return self.height

class B:
	def __init__(self, *args):
		self.sex=args[0]
	def g2(self):
		return 2

if __name__ == '__main__':
	l={}
	while True:
		a=raw_input()
		if not a:
			break
		a=a.split(" ")
		if a[0]=="new":
			l[a[2]]=eval(a[1])(a[2:])
		if a[0]=="g":
			# import pdb;pdb.set_trace()
			f=getattr(l[a[2]],a[3])
			print(f())
	import pdb;pdb.set_trace()
	d=l
	for i in d:
		print(d[i])



	