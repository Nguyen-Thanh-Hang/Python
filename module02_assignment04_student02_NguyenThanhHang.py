vb = input('Enter text: ')
if 'Python' in vb:
    print('Yes, Python is in the docs')
else:
    print('No, Python is not in the docs')

if 'contains' in vb:
    print('Yes, contains is in the docs')
else:
    print('No, contains is not in the docs')

if 'experience' in vb:
    print('Yes, experience is in the docs') 
else:
    print('No, experience is not in the docs')   

if 'difficult' in vb:
    print('Yes, difficult is in the docs') 
else: 
    print('No, difficult is not in the docs')   

# Đếm số lần xuất hiện của giá trị Python trong danh sách
count_of_Python = vb.count('Python')
print("Number of occurrences of Python values:", count_of_Python)

#Sử dụng phương thức split() để đếm số từ trong chuỗi
a = len(vb.split())
#In ra kết quả
print("Number of words: ", a)

def capitalize_first_sentence(vb):
# Tách đoạn văn thành các câu
     sentences = vb.split('.')  
# Lấy câu đầu tiên và loại bỏ khoảng trắng thừa
     first_sentence = sentences[0].strip() 
# Viết hoa toàn bộ câu đầu
     capitalized_first_sentence = first_sentence.upper()
# Nối các câu còn lại
     rest_of_text = '. '.join(sentences[1:])
     return capitalized_first_sentence + '. ' + rest_of_text
# Gọi hàm để xử lý
result = capitalize_first_sentence(vb)
# In kết quả
print('Rewrite:', result)

#Output: Enter text: Python was designed to be easy to understand and fun to use (its name came from Monty Python so a lot of its beginner tutorials reference it). Fun is a great motivator, and since you’ll be able to build prototypes and tools quickly with Python, many find coding in Python a satisfying experience. Thus, Python has gained popularity for being a beginner-friendly language, and it has replaced Java as the most popular introductory language at Top U.S. Universities.
#Output: Yes, Python is in the docs
#Output: No, contains is not in the docs
#Output: Yes, experience is in the docs
#Output: No, difficult is not in the docs 
#Output: Number of occurrences of Python values: 5
#Output: Number of words: 78
#Output: Rewrite: PYTHON WAS DESIGNED TO BE EASY TO UNDERSTAND AND FUN TO USE (ITS NAME FROM MONTY PYTHON SO A LOT OF ITS BEGINNER TUTORIALS REFERENCE IT). Fun is a great motivator, and since you’ll be able to build prototypes and tools quickly with Python, many find coding in Python a satisfying experience. Thus, Python has gained popularity for being a beginner-friendly language, and it has replaced Java as the most popular introductory language at Top U.S. Universities.