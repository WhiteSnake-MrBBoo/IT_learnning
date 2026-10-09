from lec09_phone_book import PhoneBook

addr_list = []
pb = PhoneBook()

while (True):
    print("_______________________________________________")
    print("1:등록 2:수정 3:삭제 4:조회 Q: 종료")
    menu = input("메뉴를 선택하세요")

    if (menu in ["Q", "q"]):
        print("종료")
        break  # ------------------------------
    elif (menu == "1"):
        addr_list = pb.save(addr_list)
    elif (menu == "2"):
        addr_list = pb.update(addr_list)
    elif (menu == "3"):
        addr_list = pb.delete(addr_list)
    elif (menu == "4"):
        pb.select(addr_list)
    else:
        print(f"잘못된 메뉴 번호를 선택하셨습니다.")