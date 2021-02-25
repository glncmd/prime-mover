def enumerate_primes():
    
    def primes():
        n = 1
        while True:
            factors = [x for x in range(1,n+1) if not n%x]
            if len(factors) == 2:
                yield n
            n += 2
    
    prime_gen = primes()
    
    while True:
        choice = 'null'
        
        while choice not in ['y', 'n']:
            choice = input('y/n: ')

        if choice == 'y':
            print(next(prime_gen))
        else:
            break