class PhoneBook :
    def save(self, addr_list):
        name = input("이름을 입력하세요")
        tel = input("전화번호을 입력하세요")

        addr_list.append([name, tel])
        print(f"{name},{tel} 저장되었습니다")
        return addr_list

    def update(self, addr_list):
        print("수정")
        search_name = input("수정하려는 사람의 이름을 입력하세요")
        update_tel = input("변경될 전화번호을 입력하세요")
        for v in addr_list:
            if v[0] == search_name:
                v[1] = update_tel
        return addr_list

    def delete(self, addr_list) :
        print("삭제")
        search_name = input("삭제하려는 사람의 이름을 입력하세요")
        for v in addr_list:
            if v[0] == search_name:
                addr_list.remove(v)
        return addr_list

    def select(self, addr_list):
        print(f"{len(addr_list)}건 조회")
        for v in addr_list:
            print(v[0], v[1])
