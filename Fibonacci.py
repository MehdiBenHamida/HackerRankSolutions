def F(n):
    computed = {0: 0, 1: 1}
    def fib_inner_x(n):
        try:
            computed[n]
        except KeyError:
            computed[n] = fib_inner_x(n-1) + fib_inner_x(n-2)
        return computed[n]

    return fib_inner_x(n)


n = int(raw_input().strip())
x = []
for i in xrange(n):
	l = int(raw_input().strip())
	x.append(F(l+1)%10)
for i in x:
	print (i)
