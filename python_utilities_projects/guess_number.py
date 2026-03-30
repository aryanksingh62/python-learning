# guess number game
corr_num=243
for i in range(1,5):
    guess=int(input(f"attempt{i}:"))
    if guess<corr_num:
        print("its too low")
        # i+=1
        continue
    elif guess>corr_num:
        print("its too high")
        # i+=1
        continue
    elif guess==corr_num:
        print("your guess is coorect")
        break
else:
        print("your attempts finished")
