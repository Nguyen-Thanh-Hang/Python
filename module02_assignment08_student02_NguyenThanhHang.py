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
full = 6
for i in range(full):
    for j in range(full-1-i): #Tạo khoảng trắng
        print(' ', end="")
    for j in range(i+1): #In các dấu *
        print('*', end = ' ')
    print()
print("(4) Full Pyramid")
print()
#Output:
#     *           
#    * *             
#   * * *           
#  * * * *      
# * * * * *         
#* * * * * *      
#(4) Full Pyramid  

inverted_full = 7
for i in range(inverted_full):
    for j in range(i+1): #Tạo các khoảng trắng cho từng dòng
        print(' ', end="")
    for j in range(inverted_full-i-1): #In các dấu * 
        print('*', end = ' ')
    print() 
print("(5) Inverted Full Pyramid")
print()
#Output:
#* * * * * *               
# * * * * *         
#  * * * *        
#   * * *         
#    * *            
#     *               
#(5) Inverted Full Pyramid      

hollow_full = 6
for i in range(hollow_full):
    if i == 0:
        print(' '*(hollow_full-1)+'* ')
    elif i > 0 and i < (hollow_full - 1):
        print(' '*(hollow_full-i-1)+'* '+'  '*(i-1)+'* ')
    else: 
        print('* '*hollow_full)
print("(6) Hollow Full Pyramid")
print()
#Output: 
#     *
#    * *
#   *   *
#  *     *
# *       *
#* * * * * *
#(6) Hollow Full Pyramid
