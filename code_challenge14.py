statement = True
anime_list = []

while statement is True:
    anime_title = input('Enter the title of an anime (Enter "0" to finish): ')

    if anime_title.lower() == "0":
        break
    else:
        anime_list.append(anime_title)
        continue
print("You have exited the anime entry program")
print("Your anime list include:")
print("============")
for i in anime_list:
    print(f"- {i}")
print("============")