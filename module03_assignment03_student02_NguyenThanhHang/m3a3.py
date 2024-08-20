value = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9, 'J':10, 'K':11, 'L':12, 'M':13, 'N':14, 'O':15, 'P':16, 'Q':17, 'R':18, 'S':19, 'T':20, 'U':21, 'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26}
f = open('names.txt', 'r')         #Mở file văn bản tên là names.txt ở chế độ đọc ('r').
names = f.read(100000)             #Đọc tối đa 100.000 ký tự từ file và lưu vào biến names
names = names.replace(' " ', '')   #Xóa bỏ các dấu ngoặc kép (") có khoảng trắng ở trước và sau trong chuỗi names
namelist = names.split(',')        #Tách chuỗi names thành một danh sách tên, mỗi tên là một phần tử trong danh sách namelist
namenum = 1                        
scores = []                        #Tạo một danh sách rỗng scores để lưu điểm của từng tên.
answer = 0
namelist = sorted(namelist)        #Sắp xếp danh sách namelist theo thứ tự bảng chữ cái tăng dần.

for name in namelist:
    score = 0
    for letter in name.upper():   #Lặp qua từng chữ cái trong tên hiện tại, chuyển thành chữ in hoa để tính điểm không phân biệt chữ hoa thường.
        if letter.isalpha():      #Kiểm tra xem chữ cái hiện tại có phải là chữ cái (từ A đến Z) hay không.
            score += value.get(letter, 0) #Tính điểm cho chữ cái hiện tại và cộng vào score.
    scores.append(score * namenum) #Thêm điểm của tên hiện tại nhân với namenum vào danh sách scores
    score = 0
    namenum += 1
for score in scores:
    answer += score
print(answer)

#Output: 871198282
