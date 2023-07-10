import psycopg2

conn = psycopg2.connect(
    host='localhost',
    port='5433',
    dbname='postgres',
    user='postgres',
    password='jkhldh940411'
)

cursor = conn.cursor()


library_system = {
    '1': {'option': '도서 정보 조회'},
    '2': {'option': '도서 대출'},
    '3': {'option': '도서 반납'},
    '4': {'option': '종료'},
}


def print_system():
    print('\n-------------------------------\n '
          '    도서관 관리 시스템 메인 메뉴\n'
          '-------------------------------')
    for id, system in library_system.items():
        print(f"{id}. {system['option']}")


def book_info():
    while True:
        print('\n-------------------------------\n'
            '        도서 정보 조회\n'
            '-------------------------------')
        choice = input('\n조회 할 도서의 id를 입력하세요(이전메뉴:exit): ')
        cursor.execute("SELECT id FROM library;")
        result = cursor.fetchall()
        print(result)

        if choice == 'exit':
            print_system()


def book_loan():
    while True:
        print('\n-------------------------------\n'
            '      도서 대출 서브 메뉴\n'
            '-------------------------------')
        choice = input('\n대출 할 도서의 id를 입력하세요(이전메뉴:exit): ')
        cursor.execute("UPDATE library SET is_available = '0' WHERE is_available = '1';")
        cursor.commit()
        print("대출이 완료 되었습니다.")

        if choice == 'exit':
            print_system()



def book_return():
    while True:
        print('\n-------------------------------\n'
            '      도서 반납 서브 메뉴\n'
            '-------------------------------')
        choice = input('\n반납 할 도서의 id를 입력하세요(이전메뉴:exit): ')
        cursor.execute("UPDATE library SET is_available = '1' WHERE is_available = '0';")
        cursor.commit()
        print("반납이 완료 되었습니다.")

        if choice == 'exit':
            print_system()


while True:
    print_system()
    choice = input('-------------------------------'
                   '\n사용할 시스템 메뉴를 선택하세요:')
    if choice == '1':
        book_info()
        break

    elif choice == '2':
        book_loan()
        break


    elif choice == '3':
        book_return()
        break


    elif choice == '4':
        print("시스템을 종료합니다. 이용해주셔서 감사합니다.")
        break

    else:
        print("\n잘못된 선택입니다. 다시 선택해주세요.")

cursor.close()
conn.close()
