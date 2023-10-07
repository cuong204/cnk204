ten_sach = []
tac_gia = []
the_loai = []
nam_xb = []
def add_book(ten_sach, tac_gia, the_loai, nam_xb):
    tensach = input("Nhap ten sach: ")
    ten_sach.append(tensach)
    tacgia = input("Nhap ten tac gia: ")
    tac_gia.append(tacgia)
    theloai = input("Nhap the loai: ")
    the_loai.append(theloai)
    namxb = int(input("Nhap nam xuat ban: "))
    nam_xb.append(namxb)
    print(f"{tensach} da duoc them.")

def delete_book(ten_sach, tac_gia, the_loai, nam_xb):
    xoa_sach = input("Nhap ten sach can xoa: ")
    for i in range(len(ten_sach)):
        if xoa_sach == ten_sach[i]:
            ten_sach.remove(ten_sach[i])
            tac_gia.remove(tac_gia[i])
            the_loai.remove(the_loai[i])
            nam_xb.remove(nam_xb[i])
    print(f"{xoa_sach} da duoc xoa.")

ten_sach = []
tac_gia = []
the_loai = []
nam_xb = []
def add_book(ten_sach, tac_gia, the_loai, nam_xb):
    tensach = input("Nhap ten sach: ")
    ten_sach.append(tensach)
    tacgia = input("Nhap ten tac gia: ")
    tac_gia.append(tacgia)
    theloai = input("Nhap the loai: ")
    the_loai.append(theloai)
    namxb = int(input("Nhap nam xuat ban: "))
    nam_xb.append(namxb)
    print(f"{tensach} da duoc them.")

def delete_book(ten_sach, tac_gia, the_loai, nam_xb):
    xoa_sach = input("Nhap ten sach can xoa: ")
    for i in range(len(ten_sach)):
        if xoa_sach == ten_sach[i]:
            ten_sach.remove(ten_sach[i])
            tac_gia.remove(tac_gia[i])
            the_loai.remove(the_loai[i])
            nam_xb.remove(nam_xb[i])
    print(f"{xoa_sach} da duoc xoa.")

def edit_book(ten_sach, tac_gia, the_loai, nam_xb):
    sua_sach = input("Nhap ten sach can sua: ")
    for i in range(len(ten_sach)):
        if sua_sach == ten_sach[i]:
            tac_gia[i] = input("Nhap ten tac gia moi: ")
            the_loai[i] = input("Nhap ten the loai moi: ")
            nam_xb[i] = int(input("Nhap nam xuat ban moi: "))
    print(f"{sua_sach} da duoc cap nhat")

def search_book(ten_sach, tac_gia, the_loai, nam_xb):
    loai_sach = input("Nhap the loai sach: ")
    for i in range(len(ten_sach)):
        if the_loai[i] == loai_sach:
            print(ten_sach[i])

def year_book(ten_sach, tac_gia, the_loai, nam_xb):
    for i in range(len(ten_sach) - 1):
        for j in range(i + 1, len(ten_sach)):
            if nam_xb[i] > nam_xb[j]:
                temp = nam_xb[i]
                nam_xb[i] = nam_xb[j]
                nam_xb[j] = temp
    for i in range(len(ten_sach)):
        print(f'"{ten_sach[i]}" cua tac gia {tac_gia[i]} ({nam_xb[i]})')


running = True

while (running):
    choice = input("Enter your choice: ")
    if choice == "1":
        add_book(ten_sach, tac_gia, the_loai, nam_xb)
        
    elif choice == "2":
        delete_book(ten_sach, tac_gia, the_loai, nam_xb)
        
    elif choice == "3":
        edit_book(ten_sach, tac_gia, the_loai, nam_xb)
        
    elif choice == "4":
        search_book(ten_sach, tac_gia, the_loai, nam_xb)
        
    elif choice == "5":
        year_book(ten_sach, tac_gia, the_loai, nam_xb)