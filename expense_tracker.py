def show_guide():
    print("\n" + "="*50)
    print("\t=== HƯỚNG DẪN SỬ DỤNG CHƯƠNG TRÌNH ===")
    print("="*50)
    print("\t1. Xem hướng dẫn:\tĐọc các quy tắc nhập liệu và chức năng.")
    print("\t2. Xem danh sách:\tHiển thị toàn bộ các khoản chi tiêu hiện có.")
    print("\t3. Thêm khoản chi:\tNhập tên, số tiền (phải là số nguyên > 0) và danh mục.")
    print("\t4. Tìm kiếm:\t\tTìm theo tên hoặc danh mục (không phân biệt hoa/thường).")
    print("\t5. Xóa khoản chi:\tNhập tên khoản chi để loại bỏ khỏi danh sách.")
    print("\t6. Thống kê:\t\tTổng hợp tổng tiền và chi tiết theo từng danh mục.")
    print("\t7. Thoát:\t\tĐóng chương trình.")
    print("="*50 + "\n")


def show_expenses(expenses):
    print("\n" + "-"*65)
    print("\tDANH SÁCH CÁC KHOẢN CHI TIÊU HIỆN TẠI")
    print("-"*65)
    
    if len(expenses) == 0:
        print("\t[Thông báo] Hiện tại chưa có khoản chi tiêu nào trong danh sách!\n")
        return

    print("STT\tTên khoản chi\t\tSố tiền\t\tDanh mục")
    print("-"*65)
    for index, item in enumerate(expenses, start=1):
        name = item["name"]
        amount = item["amount"]
        category = item["category"]
        
        tab_name = "\t\t" if len(name) < 8 else "\t"
        print(f"{index}\t{name}{tab_name}{amount:,} VND\t{category}")
    print("-"*65 + "\n")


def add_expense(expenses):
    print("\n" + "-"*40)
    print("\tTHÊM KHOẢN CHI TIÊU MỚI")
    print("-"*40)

    while True:
        name_input = input("Nhập tên khoản chi (ví dụ: Cơm trưa, Giáo trình): ").strip()
        if len(name_input) == 0:
            print("Lỗi: Tên khoản chi không được để trống! Vui lòng nhập lại.\n")
            continue
        break
    
    while True:
        amount_input = input("Nhập số tiền (VND): ").strip()
        
        if not amount_input.isdigit() or int(amount_input) <= 0:
            print("Lỗi: Số tiền phải là số nguyên dương (> 0)! Vui lòng nhập lại.\n")
            continue
        
        amount = int(amount_input)
        break

    while True:
        category_input = input("Nhập danh mục (Ăn uống, Học tập, Nhà ở, Đi lại...): ").strip()
        if len(category_input) == 0:
            print("Lỗi: Danh mục không được để trống! Vui lòng nhập lại.\n")
            continue
        category = category_input.capitalize()
        break

    new_expense = {
        "name": name_input,
        "amount": amount,
        "category": category
    }
    expenses.append(new_expense)
    print(f"\n=> Đã thêm thành công: '{name_input}' ({amount:,} VND - {category}) vào danh sách!\n")


def search_expense(expenses):
    print("\n" + "-"*40)
    print("\tTÌM KIẾM KHOẢN CHI TIÊU")
    print("-"*40)
    
    keyword = input("Nhập tên hoặc danh mục cần tìm: ").strip()
    if len(keyword) == 0:
        print("Lỗi: Bạn chưa nhập từ khóa tìm kiếm!\n")
        return

    found = False
    keyword_lower = keyword.lower()

    print("\nKết quả tìm kiếm:")
    print("STT\tTên khoản chi\t\tSố tiền\t\tDanh mục")
    print("-"*65)

    count = 0
    for item in expenses:
        if keyword_lower in item["name"].lower() or keyword_lower in item["category"].lower():
            count = count + 1
            tab_name = "\t\t" if len(item["name"]) < 8 else "\t"
            print(f"{count}\t{item['name']}{tab_name}{item['amount']:,} VND\t{item['category']}")
            found = True

    if not found:
        print(f"\t[Không tìm thấy khoản chi nào phù hợp với từ khóa '{keyword}']")
    print("-"*65 + "\n")


def delete_expense(expenses):
    print("\n" + "-"*40)
    print("\tXÓA KHOẢN CHI TIÊU")
    print("-"*40)

    if len(expenses) == 0:
        print("[Thông báo] Danh sách đang trống, không có gì để xóa!\n")
        return

    target_name = input("Nhập chính xác tên khoản chi cần xóa: ").strip()
    target_lower = target_name.lower()
    
    item_to_remove = None
    found = False

    for item in expenses:
        if item["name"].lower() == target_lower:
            item_to_remove = item
            found = True
            break

    if found and item_to_remove is not None:
        expenses.remove(item_to_remove)
        print(f"\n=> Đã xóa thành công khoản chi: '{item_to_remove['name']}' ({item_to_remove['amount']:,} VND)!\n")
    else:
        print(f"\nLỗi: Không tìm thấy khoản chi nào có tên là '{target_name}' để xóa.\n")


def show_summary(expenses):
    print("\n" + "="*50)
    print("\tBÁO CÁO THỐNG KÊ CHI TIÊU SINH VIÊN")
    print("="*50)

    total_count = len(expenses)
    if total_count == 0:
        print("\tChưa có dữ liệu chi tiêu để thống kê.\n")
        print("="*50 + "\n")
        return

    total_amount = 0
    category_summary = {}

    for item in expenses:
        amount = item["amount"]
        category = item["category"]

        total_amount = total_amount + amount

        if category in category_summary:
            category_summary[category] = category_summary[category] + amount
        else:
            category_summary[category] = amount

    print(f"\tTổng số khoản chi tiêu:\t{total_count} khoản")
    print(f"\tTỔNG TIỀN ĐÃ CHI:\t{total_amount:,} VND")
    print("-"*50)
    print("\tCHI TIẾT THEO DANH MỤC:")

    for cat_name, cat_total in category_summary.items():
        percentage = (cat_total / total_amount) * 100
        print(f"\t- {cat_name}:\t\t{cat_total:,} VND\t({percentage:.1f}%)")

    print("="*50 + "\n")


def main():
    expenses = [
        {"name": "Cơm trưa canteen", "amount": 35000, "category": "Ăn uống"},
        {"name": "Tiền phòng trọ", "amount": 1500000, "category": "Nhà ở"},
        {"name": "Giáo trình CSDL", "amount": 75000, "category": "Học tập"},
        {"name": "Đổ xăng xe máy", "amount": 60000, "category": "Đi lại"}
    ]

    while True:
        print("\n" + "="*45)
        print("\tQUẢN LÝ CHI TIÊU SINH VIÊN")
        print("="*45)
        print("1.\tXem hướng dẫn sử dụng")
        print("2.\tXem danh sách chi tiêu")
        print("3.\tThêm khoản chi tiêu mới")
        print("4.\tTìm kiếm khoản chi tiêu")
        print("5.\tXóa khoản chi tiêu")
        print("6.\tBáo cáo thống kê chi tiêu")
        print("7.\tThoát chương trình")
        print("="*45)

        choice = input("Vui lòng chọn chức năng (1-7): ").strip()

        if choice == "1":
            show_guide()
        elif choice == "2":
            show_expenses(expenses)
        elif choice == "3":
            add_expense(expenses)
        elif choice == "4":
            search_expense(expenses)
        elif choice == "5":
            delete_expense(expenses)
        elif choice == "6":
            show_summary(expenses)
        elif choice == "7":
            print("\n" + "*"*45)
            print("\tCẢM ƠN BẠN ĐÃ SỬ DỤNG CHƯƠNG TRÌNH!")
            print("\tCHÚC BẠN CHI TIÊU HỢP LÝ VÀ TIẾT KIỆM!")
            print("*"*45 + "\n")
            break
        else:
            print("\n[Lỗi] Lựa chọn không hợp lệ! Vui lòng chỉ nhập số từ 1 đến 7.\n")


if __name__ == "__main__":
    main()
