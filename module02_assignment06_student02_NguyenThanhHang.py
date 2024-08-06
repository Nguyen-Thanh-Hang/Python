def foo(a, b, c):
    if a == 0:
            raise ValueError("Hệ số a phải khác 0")
    delta = b**2 - 4*a*c
    if delta < 0: #Phương trình vô nghiệm
        return []
    elif delta == 0: #Phương trình có 2 nghiệm kép
        x = -b/(2*a)
        return [x]
    elif delta > 0 and a != 0: #Phương trình có hai nghiệm phân biệt
        x1 = (-b + delta**0.5)/(2*a)
        x2 = (-b - delta**0.5)/(2*a)
        return[x1, x2]
nghiem = foo(1, -3, 2)
print(nghiem)

#Output: [2.0, 1.0]
