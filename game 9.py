x=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
count =0


for i in range(0,len(x),1):
    print("player1")

    z=int (input("how many num:"))
    
    while (z>2):
        print("not valid")
        z=int(input("how many num:"))

    if (z==2) :
        n=int (input("enter first num:"))
        m =int (input("enter second num:"))
        for j in range(0,len(x),1):
            if (n==x[n-1]): 
                x[j]="-"
              
            elif (m==x[m-1]):
                  x[j]="-"
                  print(x)
                  count=count+2
        
                
             
    if(z==1):
        o=int(input("enter num:"))
        for a in range(0,len(x),1):
            if (a==o):
                 x[a]="-"
                 print(x)
                 count+=1
    if (count==20):
            print("player1 is winer")
                 
    
    print("player2")
    a=int (input("how many play:"))
        
    
    if a==2:
           
    
                p=int(input("enter first num:"))
                L=int(input("enter second num:"))
                for e in range(0,len(x),1):
                       if(p==x[p-1]):
                        
                    
                            
                            x[e]="-"
                       elif L==x[L-1]:
                            x[e]="-"
                            print(x)
                            count+=2
    if a==1: 
                 y=int (input("enter your num:"))

                            
                        
                    
                            
              
                 c=int (input("enter your num:"))
                 for r in range (0,len(x),1):
                        if (o==x[o-1]):
                            
                           
                        
                            print(x)
                            count+=1
                        
    if( count==20):       
                    print("player2 is winer") 

                        
                        
            
                       
                                
                        
                        
                                
                         
                                       
                            
                                
                                
                          
                    

            
                    
                



            
                    
            

              
              
    

