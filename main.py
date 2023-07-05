library_system = {
    '1': {'option': '도서 정보 조회'},
    '2': {'option': '도서 대출'},
    '3': {'option': '도서 반납'},
    '4': {'option': '대출 정보 조회'},
    '5': {'option': '종료'},
}


def print_system():
    print('\n-------------------------------\n '
          '도서관 관리 시스템 메인 메뉴 \n'
          '-------------------------------')
    for id, system in library_system.items():
        print(f"{id}. {system['option']}")


def book_info():
    pass


def book_loan():
    pass


def book_return():
    pass


def loan_info():
    pass


while True:
    print_system()
    choice = input('-------------------------------'
                   '\n사용할 시스템 메뉴를 선택하세요:')
    if choice == '1':
        book_info()

    elif choice == '2':
        book_loan()

    elif choice == '3':
        book_return()

    elif choice == '4':
        loan_info()

    elif choice == '5':
        print("시스템을 종료합니다. 이용해주셔서 감사합니다.")
        break
    else:
        print("\n잘못된 선택입니다. 다시 선택해주세요.")
