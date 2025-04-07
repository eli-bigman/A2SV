no_cards = int(input())
cards = list(map(int, input().split()))

#initialize two pointers
left = 0
right = no_cards - 1

#initialize sum of cards of each player
sereja = 0
dima = 0

# flag to indicate when its sereja turn
sereja_turn  = True

while left <= right:
    # find the largest card and let it be the choosen card
    if cards[left] > cards[right]:
        choosen_card = cards[left]
        left += 1
    else:
        choosen_card = cards[right]
        right -= 1

    if sereja_turn:
        sereja += choosen_card
    else:
        dima += choosen_card

    sereja_turn = not sereja_turn

    

print(sereja, dima)


