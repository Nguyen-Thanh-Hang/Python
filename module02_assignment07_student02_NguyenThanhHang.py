def rot13(text):
  result = ""
  for char in text:
    if char.isalpha():
      # Kiểm tra xem ký tự có phải là chữ cái không
      if char.isupper():
        # Chữ in hoa
        char = chr((ord(char) - 65 + 13) % 26 + 65)
      else:
        # Chữ thường
        char = chr((ord(char) - 97 + 13) % 26 + 97)
    result += char
  return result
text = "PYTHON"
encrypted_text = rot13(text)
print(encrypted_text) 
#Output: CLGUBA