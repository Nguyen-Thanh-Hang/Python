print('a')
while True:
    number = input("Nhập một chữ số từ 0 đến 9: ")
    print("Bạn đã nhập:", number)
    break
print()
#Output: Nhập một chữ số từ 0 đến 9: 2
#        Bạn đã nhập: 2

print('b')
import random
def rock_paper_scissors():
  while True:
    player1 = input("Bạn là người chơi số 1! Hãy chọn: Kéo / Búa / Bao | ").lower()
    player2 = input("Bạn là người chơi số 2! Hãy chọn: Kéo / Búa / Bao | ").lower()
    if player1 == player2:
          print("Hòa!")
    elif (player1 == "Kéo" and player2 == "Bao") or (player1 == "Búa" and player2 == "Kéo") or (player1 == "Bao" and player2 == "Búa"):
      print("Người chơi số 1 thắng!")
    else:
      print("Người chơi số 2 thắng!")
    play_again = input("Tiếp tục? (Có / Không): ").lower()
    if play_again.lower() != "có":
      break
if __name__ == "__main__":
  rock_paper_scissors()
print()
#Output: Bạn là người chơi số 1! Hãy chọn: Kéo / Búa / Bao | kéo
#        Bạn là người chơi số 2! Hãy chọn: Kéo / Búa / Bao | bao
#        Người chơi số 2 thắng!!
#        Tiếp tục? (Có / Không): Có
#        Bạn là người chơi số 1! Hãy chọn: Kéo / Búa / Bao | bao 
#        Bạn là người chơi số 2! Hãy chọn: Kéo / Búa / Bao | bao
#        Hòa!
#        Tiếp tục? (Có / Không): không
print('c')
import random
def rock_paper_scissors():
  while True:
    player1 = input("Bạn là người chơi số 1! Hãy chọn: Kéo / Búa / Bao | ").lower()
    player2_choices = ['kéo', 'búa', 'bao']
    player2 = random.choice(player2_choices)
    if player1 == player2:
      print("Hòa!")
    elif (player1 == "kéo" and player2 == "bao") or (player1 == "búa" and player2 == "kéo") or (player1 == "bao" and player2 == "búa"):
      print(f"Người chơi số 1 thắng! Người chơi số 2 chọn: {player2}")
    else:
      print(f"Người chơi số 1 thua! Người chơi số 2 chọn: {player2}")
    play_again = input("Tiếp tục? (Có / Không): ").lower()
    if play_again != "Có":
      break
if __name__ == "__main__":
  rock_paper_scissors()
print()

#Output: Bạn là người chơi số 1! Hãy chọn: Kéo / Búa / Bao | kéo
#        Người chơi số 1 thua! Người chơi số 2 chọn: búa
#        Tiếp tục? (Có / Không): không