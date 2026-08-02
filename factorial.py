#Taking input from 
a= int(input('Enter the no. for finding the factorial : ')) 

#Initialize the variable to be strored in result
f=1

#loop for printing the no. 
for i in range (a,0,-1) :
        f=f*i
        
#multiplying the current results by loop variable     
print(f)