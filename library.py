books = []
issued_books = []
def add_book():
    name = input('enter the name of the books:')
    books.append(name)
    print(name,'is added')

def show_books():
    if len(books)== 0:
        print('no books availaible')
    else:
        print('availaible books')
        for b in books:
            print(b)

def borrow_book():
    name = input('enter the book you want to borrow')
    if name in books:
       issued_books.append(name)
       books.remove(name)
       print(name,'is issued')
    else:
        print(name,'book is not availaible')   

def return_book():
    name = input('enter the book name you want to return')
    if name in issued_books: 
        issued_books.remove(name)
        books.append(name)
        print(name,'is returned')
    else:
        print(name,'is not issued')    
def library():
    while True:
        print('menu')
        print('1.Add book')
        print('2.Show books')
        print('3.Borrow books')
        print('4. Return books')
        print('5.Exit')

        choice = int(input('Enter the choice'))
        if choice == 1:
            add_book()
        elif choice == 2:
            show_books()  
        elif choice == 3:
            borrow_book()
        elif choice == 4:
            return_book()
        elif choice == 5:
            print('Thank You!visit again')              
            break
        else:
            print('Invalid choice')

library()
            