import psycopg2

def db_connect():
    connection = psycopg2.connect(
        host='localhost',
        port='5433',
        dbname='library',
        user='postgres',
        password='jkhldh940411',
    )
    return connection

def add_book_to_db():
    print('-------------')
    print('도서입력')
    print('-------------')
    title = input("제목 : ")
    author = input("저자 : ")
    publisher = input("출판사 : ")
    print(f"입력값 : {title},{author},{publisher}")
    connection = db_connect()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO books1 (title, author, publisher) VALUES (%s, %s, %s)", (title, author, publisher))
    connection.commit()
    cursor.close()
    connection.close()
    # 커서는 커넥션에 기반


def get_book_info():
    id = input("조회 할 아이디를 입력하세요 : ")
    connection = db_connect()
    cursor = connection.cursor()
    cursor.execute("SELECT id, title, author, publisher, borrowed FROM books1 WHERE id = %s", (id,))
    result = cursor.fetchone()
    if result:
        print(f"ID: {result[0]}, 제목: {result[1]}, 저자: {result[2]}, 출판사: {result[3]}", end='')
        print("도서상태: 대출중" if result[4] else "도서상태: 대출가능")
    else:
        print("해당 도서를 찾을 수 없습니다.")
    cursor.close()
    connection.close()

def borrow_book():
    book_id = input("대출할 도서의 ID를 입력하세요: ")
    connection = db_connect()
    cursor = connection.cursor()
    cursor.execute("UPDATE books1 SET borrowed = True WHERE id = %s", (book_id,))
    connection.commit()
    print("도서가 성공적으로 대출되었습니다.")
    input("계속하려면 아무키나 입력하세요")
    cursor.close()
    connection.close()

def return_book():
    book_id = input("반납할 도서의 ID를 입력하세요: ")
    connection = db_connect()
    cursor = connection.cursor()
    cursor.execute("UPDATE books1 SET borrowed = False WHERE id = %s", (book_id,))
    connection.commit()
    print("도서가 성공적으로 반납되었습니다.")
    input("계속하려면 아무키나 입력하세요")
    cursor.close()
    connection.close()


def view_borrowed_books():
    connection = db_connect()
    cursor = connection.cursor()
    cursor.execute("SELECT id, title, author, publisher, borrowed FROM books1 WHERE borrowed = True")
    result_list = cursor.fetchall()
    for result in result_list:
        print(f"ID: {result[0]}, 제목: {result[1]}, 저자: {result[2]}, 출판사: {result[3]}", end=' ')
        print("도서상태: 대출중" if result[4] else "도서상태: 대출가능")
    if len(result_list) == 0:
        print("대출중인 도서가 없습니다.")
    cursor.close()
    connection.close()



def exit_program():
    print("프로그램을 종료합니다.")


menu_options = {
    1: add_book_to_db,
    2: get_book_info,
    3: borrow_book,
    4: return_book,
    5: view_borrowed_books,
    6: exit_program
}

def main_menu():
    while True:
        print('-------------')
        print('도서관 메뉴')
        print('-------------')
        print('1. 도서 정보 입력')
        print('2. 도서 정보 조회')
        print('3. 도서 대출')
        print('4. 도서 반납')
        print('5. 대출 도서 조회')
        print('6. 종료')
        print('-------------')
        try:
            selected_menu = int(input("메뉴를 선택하세요 : "))
            menu_action = menu_options.get(selected_menu)
            menu_action()

            print(selected_menu)
            if selected_menu == 6:
                break
        except ValueError:
            print("잘못된 입력입니다. 숫자를 입력해주세요.")
        except Exception as e:
            print(f"오류가 발생했습니다. {e}")



if __name__ == '__main__':
    main_menu()

# import psycopg2
#
# conn = psycopg2.connect(
#     host='localhost',
#     port='5433',
#     dbname='postgres',
#     user='postgres',
#     password='jkhldh940411'
# )
#
# cursor = conn.cursor()
#
#
# library_system = {
#     '1': {'option': '도서 정보 조회'},
#     '2': {'option': '도서 대출'},
#     '3': {'option': '도서 반납'},
#     '4': {'option': '종료'},
# }
#
#
# def print_system():
#     print('\n-------------------------------\n '
#           '    도서관 관리 시스템 메인 메뉴\n'
#           '-------------------------------')
#     for id, system in library_system.items():
#         print(f"{id}. {system['option']}")
#
#
# def book_info():
#     while True:
#         print('\n-------------------------------\n'
#             '        도서 정보 조회\n'
#             '-------------------------------')
#         info_input = input('\n조회 할 도서의 id를 입력하세요(이전메뉴:exit): ')
#         cursor.execute("SELECT * FROM books WHERE book_id = info_input;")
#         result = cursor.fetchall()
#         print(result)
#
#         if info_input == 'exit':
#             break
#
#     choice_system()
#
#
# def book_loan():
#     while True:
#         print('\n-------------------------------\n'
#             '      도서 대출 서브 메뉴\n'
#             '-------------------------------')
#         loan_input = input('\n대출 할 도서의 id를 입력하세요(이전메뉴:exit): ')
#         cursor.execute("UPDATE books SET is_available = FALSE WHERE is_available = TRUE;")
#         print("대출이 완료 되었습니다.")
#
#         if loan_input == 'exit':
#             break
#
#     choice_system()
#
#
#
# def book_return():
#     while True:
#         print('\n-------------------------------\n'
#             '      도서 반납 서브 메뉴\n'
#             '-------------------------------')
#         return_input = input('\n반납 할 도서의 id를 입력하세요(이전메뉴:exit): ')
#         cursor.execute("UPDATE books SET is_available = TRUE WHERE is_available = FALSE;")
#         print("반납이 완료 되었습니다.")
#
#         if return_input == 'exit':
#             break
#
#     choice_system()
#
# def choice_system():
#     while True:
#         print_system()
#         choice = input('-------------------------------'
#                     '\n사용할 시스템 메뉴를 선택하세요:')
#         if choice == '1':
#             book_info()
#             break
#
#         elif choice == '2':
#             book_loan()
#             break
#
#
#         elif choice == '3':
#             book_return()
#             break
#
#
#         elif choice == '4':
#             print("시스템을 종료합니다. 이용해주셔서 감사합니다.")
#             break
#
#         else:
#             print("\n잘못된 선택입니다. 다시 선택해주세요.")
#
# choice_system()
#
# cursor.close()
# conn.close()
