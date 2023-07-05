library_system = {
    '1': {'option':'도서 정보 조회'},
    '2': {'option':'도서 대출'},
    '3': {'option':'도서 반납'},
    '4': {'option':'대출 정보 조회'},
    '5': {'option':'종료'},
}

def print_system():
    print('\n-------------------------------\n '
          '도서관 관리 시스템 메인 메뉴 \n'
          '-------------------------------')
    for id, system in library_system.items():
        print(f"{id}. {system['option']}")




