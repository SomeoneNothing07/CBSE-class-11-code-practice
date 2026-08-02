def prime():
    for i in range (2,1001):
        is_prime=True
        
        for j in range (2,i):
            if i%j==0:
                is_prime=False
                break

        if is_prime :
            print (i,'is prime no.')
    
prime()