import time
file = open("pokemon.txt", "r")
text = file.read()
text = text.split("\n")
#print(text)
while True:
    search = input("Enter a letter or phrase to search for.")
    print(f'Search results for \"{search}\": ')
    start = time.time()
    count = 0
    if " OR " in search:
        searches = search.split(" OR ")
        for i in searches:
            for j in text:
                if i in j.lower():
                    print(j)
                    count += 1
                    text.remove(j)
    else:
        for i in text:
            if search in i.lower():
                print(i)
                count += 1
                text.remove(j)
    end = time.time()
    duration = end - start
    print(f'----------\n{count} search results found in {duration} seconds\n')
