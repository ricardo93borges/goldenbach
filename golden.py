#CONJECTURA DE GOLDENBACH
#TODO NUMERO PAR MAIOR OU IGUAL A 4 E A SOMA DE DOIS NUMEROS PRIMOS

def is_prime(n):
	d=2
	prime=True
	while d<n:
		if n%d == 0 and n>2:
			prime=False
			break
		d=d+1
	return prime

def get_primes(n):
	d=2
	primes=[]
	while d<n:
		if is_prime(d):
			primes.append(d)
		d=d+1
	return primes

def get_sum(n):
	primes = get_primes(n)
	print "numeros primos ate ", n, ":", primes
	for a in primes:
		for b in primes:
			if a+b == n:
				return a, "+", b, "=", n

print get_sum(32)

