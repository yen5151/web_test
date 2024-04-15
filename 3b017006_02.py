import os
import json
def load_students_data(filename):
    if not os.path.isfile(filename):            #沒讀取到告知找無檔案
        raise FileNotFoundError(f"無法找到檔案：{filename}")
    with open(filename, 'r', encoding='utf-8') as f:        #讀取到傳回date
        return json.load(f)
def get_student_info(students,student_id):
    for student in students:      #用來再students一個一個拿出來比對
        if student['student_id'] == student_id:     #當比對到符合的id
             return student         #將此學生的資料欑送回去
    raise ValueError(f"找不到學號 {student_id} 的學生。")      #失敗回傳例外狀況
def add_course (students,student_id, course_name, course_score):
    student=get_student_info(students,student_id)       #先判斷是否有這個人
    if course_name and course_score is  None:           #再看課程名稱和成績是否為空的
        print("=>課程名稱或分數不可空白。")                #其中有一個空就不存
    else:
        student['courses'].append({'name': course_name, 'score': course_score})     #將課程和成績加入該學生裡
def calculate_average_score(student_data):          #計算並返回學生所有課程的平均分數，若無課程則返回0.0。
    courses = student_data['courses']
    if not courses:
        return 0.0
    total_score = sum(course['score'] for course in courses)
    return total_score / len(courses)

filename='students.json'        #json檔名
try:
    students=load_students_data(filename)       #確定是否能讀取到json檔
    while True:     #能一直重複執行
        print("\n***************選單***************")
        print("1. 查詢指定學號成績")
        print("2. 新增指定學號的課程名稱與分數")
        print("3. 顯示指定學號的各科平均分數")
        print("4. 離開")
        print("**********************************")
        number=input("請選擇操作項目：")        #選擇需要一個功能
        if number == "1":
            student_id=input("請輸入學號:")
            try:
                student_correct=get_student_info(students,student_id)       #再json中尋找有沒有這個學號的人
                print("=>學生資料:", json.dumps(student_correct, ensure_ascii=False, indent=2))         #將這學號的學生資料羅列出來
            except ValueError as e:
                 print(e)
        elif number == "2":
            student_id=input("請輸入學號:")
            course_name = input("請輸入要新增課程的名稱: ")
            try:
                course_score = float(input("請輸入要新增課程的分數: "))
                add_course(students, student_id, course_name, course_score)     #去新增新的課程和成績
                print("=>課程已成功新增。")
            except ValueError as e:
                print(e)
        elif number =="3":
            student_id = input("請輸入學號: ")
            try:
                student_info = get_student_info(students, student_id)       #先判斷是否有這個人
                average_score = calculate_average_score(student_info)       #再開始計算他的平均
                print(f"=>各科平均分數: {average_score:.2f}")
            except ValueError as e:
                print(e)

        elif number == "4":
            print("=>程式結束。")
            break
        else:
                print("=>請輸入有效的選項。")

except Exception as e:
            print(f"發生錯誤: {e}")
