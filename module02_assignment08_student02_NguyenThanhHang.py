half = 7
for i in range(0, half-1):
    for j in range(i+1):
        print("*", end="")
    print()
print("(1) Half Pyramid")
print()
#Output:
#*                 
#**
#***             
#****          
#*****       
#******            
#(1) Half Pyramid

inverted_half = 7
for i in range(inverted_half):
    print('*'*(inverted_half-i), ' '*i)
print('(2) Inverted Half Pyramid')
print()
#Output:
#******           
#*****              
#****                
#***                 
#**                   
#*                    
#(2) Inverted Half Pyramid        
hollow_inverted_half = 6
for i in range(hollow_inverted_half,0,-1):
    if i == hollow_inverted_half:
          print((hollow_inverted_half-1)*'*', end = '')
    if  i > 1 and i <hollow_inverted_half:
        print('*'+(i-2)*' '+'*')
    else:
        print('*')
print('(3) Hollow Inverted Half Pyramid')
print()
#Output:
#******
#*   *
#*  *
#* *
#**
#*
#(3) Hollow Inverted Half Pyramid
print(' '*6, '*')
print(' '*5,'* '*2)
print(' '*4, '* '*3)
print(' '*3, '* '*4)
print(' '*2,'* '*5)
print(' ', '* '*6)
print('(4) Full Pyramid')
print()
#Output:
#     *           
#    * *             
#   * * *           
#  * * * *      
# * * * * *         
#* * * * * *      
#(4) Full Pyramid  

print(' ', '* '*6)
print(' '*2,'* '*5)
print(' '*3, '* '*4)
print(' '*4, '* '*3)
print(' '*5,'* '*2)
print(' '*6, '*')
print('(5) Inverted Full Pyramid')
print()
#Output:
#* * * * * *               
# * * * * *         
#  * * * *        
#   * * *         
#    * *            
#     *               
#(5) Inverted Full Pyramid      

print(' '*6, '* ')
print(' '*5, '*', '*')
print(' '*4, '*', ' ', '*')
print(' '*3, '* ', ' '*2, '*')
print(' '*2, '*', ' '*5, '*')
print(' ', '* '*6)
print('(6) Hollow Full Pyramid')
#Output: 
#     *
#    * *
#   *   *
#  *     *
# *       *
#* * * * * *
#(6) Hollow Full Pyramid