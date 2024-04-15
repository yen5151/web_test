def get_even_squares(numbers):
    even_squares = []                                               #建立一個list儲存運算後的值
    for num in numbers:                                             #取得numbers裡的參數
        if num % 2 == 0:                                            #將奇數去除
             even_squares.append(num ** 2)                          #將偶數平方後加入到even_squares裡
    return format_numbers(even_squares)                             #將運算後的值傳送到format_numbers做顯示

def  get_odd_cubes(numbers):
    odd_cubes = []                                                  #建立一個list儲存運算後的值
    for num in numbers:                                             #取得numbers裡的參數
        if num % 2 != 0:                                            #將偶數去除
            odd_cubes.append(num ** 3)                              #將奇數三次方後 新增到odd_cubes裡
    return format_numbers(odd_cubes)                                #將運算後的值傳送到format_numbers做顯示

def get_sliced_list(numbers):
    sliced_list = numbers[4:]                                       #使用切片獲取從第 5個元素到最後一個元素
    return format_numbers(sliced_list)                              #將運算後的值傳送到format_numbers做顯示

def format_numbers(numbers):                                        #傳送來的list以numbers命名
    formatted_numbers = []                                          #建立一個list
    for num in numbers:                                             #取得numbers裡的參數
        formatted_numbers.append(f"{num:>{8}}")                     #使用列表推導式格式化數字，並保持靠右對齊到8個字符的寬度
        formatted_string = "，".join(formatted_numbers)             #使用join()將格式化後的數字列表連接成一個字符串
    print(formatted_string)                                         #將轉換後的值輸出顯示

num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = get_even_squares(num_list)                                 #將num_list傳輸到get_even_squares函數裡執行
result =  get_odd_cubes(num_list)                                   #將num_list傳輸到 get_odd_cubes 函數裡執行
result = get_sliced_list(num_list)                                  #將num_list傳輸到get_sliced_list函數裡執行
