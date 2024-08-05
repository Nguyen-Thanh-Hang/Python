A = [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]

# Thay thế giá trị tại vị trí thứ 3 (index là 2) bằng bình phương của nó
#A[2] = A[2] ** 2
# In ra list sau khi thay đổi
#print(A)
#Output: [70, 43, 49, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]

# sử dụng pop() để xóa phần tử 
#rs = A.pop(2)
#print("phần tử bị xóa :", rs)
#print(A)
#Output:
#phần tử bị xóa : 7
#[70, 43, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53]

#Dùng append() thêm 1 phần tử vào cuối danh sách
#A.append(A[14]**2)
#print(A)
#Output: [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53, 2809]

#Dùng len() đếm số phần tử trong 1 danh sách
#print(len(A))
#Output: 15

#Gán giá trị cho biến = 0
#total = 0
#Tạo vòng lặp, cộng dồn các phần tử trong list vào biến total.
#for value in A:
#    total += value
#In ra kết quả
#print("Tổng các phần tử trong list:", total)
#Output: Tổng các phần tử trong list: 559

#print('tổng của các phần tử có chỉ số (index) 1, 2, 3, 5:', A[1]+A[2]+A[3]+A[5])
#Output: tổng của các phần tử có chỉ số (index) 1, 2, 3, 5: 173

#reversed_A = A[::-1]
#print(reversed_A)  # Output: [53, 3, 53, 5, 1, 3, 49, 35, 80, 77, 34, 46, 7, 43, 70]
#A.reverse()
#print(A)
#Output: [53, 3, 53, 5, 1, 3, 49, 35, 80, 77, 34, 46, 7, 43, 70]

# Tạo hai list rỗng để chứa số chẵn và số lẻ
#chan = []
#le = []
#for number in A:
    #if number % 2 == 0:  # Nếu số chia hết cho 2 thì là số chẵn
    #    chan.append(number)  # Thêm vào list chứa số chẵn
    #else: #Ngược lại là số lẻ
    #    le.append(number)  # Thêm vào list chứa số lẻ
# In kết quả
#print("Các số chẵn:", chan)
#print("Các số lẻ:", le)

# Tạo một bản sao của list A
B = A.copy()
# Sắp xếp list B theo thứ tự giảm dần
B.sort(reverse=True)
# In kết quả
print('List sắp xếp giảm dần:', B) #Output: List sắp xếp giảm dần: [80, 77, 70, 53, 53, 49, 46, 43, 35, 34, 7, 5, 3, 3, 1]

#So sánh độ dài của hai list A và list B
print(len(A)==len(B)) #Output: True

#Tạo list C
C = []
#Dùng append thêm list A và list B vào list C
C = A + B
#In kết quả
print(C)
#Output: [70, 43, 7, 46, 34, 77, 80, 35, 49, 3, 1, 5, 53, 3, 53,80, 77, 70, 53, 53, 49, 46, 43, 35, 34, 7, 5, 3, 3, 1]
