def try_cap_phan_tu(tuple_data):
    first_element = tuple_data[0]
    last_element = tuple_data[-1]
    return first_element, last_element

input_tuple = eval(input("Nhap tuple:"))
first, last = try_cap_phan_tu(input_tuple)

print("Phan tu dau tien: ",first)
print("_______ cuoi cung: ",last)