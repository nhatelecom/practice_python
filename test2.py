book_list = [1,2,5]
book_list2 = []
counter = 0
a=4

for book in book_list:
    if a < book:
        book_list.insert(counter,a)
        break
    counter +=1

print(book_list)
print(book_list2==[])