def egyik():
    for oszlop in range(4):
        print("+ - ",end="")
 
def masik ():   
    for sor in range(1):
        print()
        for oszlop in range(4):
            print("- + ",end="")
    print()
  
#A futtatáshoz kommenteld ki a 
#sorokat "ettől" "eddig" jelzések között. 
  
#ettől 
  
# for i in range(2,10):
#     if i%2==0:
#         egyik()
#     else:
#         masik()
    
#eddig


######################################################  
######################################################

def sor():
    karakterek=str()
    
    for oszlop in range(2,10):
        if oszlop%2==0:
            karakterek+="- "
        else:
            karakterek+="+ "
    print(karakterek)
    
def sor2():
    karakterek=str()
    
    for oszlop in range(2,10):
        if oszlop%2==0:
            karakterek+="+ "
        else:
            karakterek+="- "
    print(karakterek)
    

#A futtatáshoz kommenteld ki a 
#sorokat "ettől" "eddig" jelzések között. 

#ettől

# for i in range(2,10):
#     if i%2==0:
#         sor()
#     else:
#         sor2()
        
#eddig

    
    


            
            
            
               
