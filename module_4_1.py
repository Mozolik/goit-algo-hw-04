
def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            SumLine = 0
            line_count = 0
            for StringLine in file.readlines():
                content = StringLine.split(",")
                SumLine += int(content[1].strip())
                line_count += 1
            
            average = SumLine//line_count
            print(f"Загальна сума заробітної плати: {SumLine}, Середня заробітна плата: {average}") 
    except FileNotFoundError:
        print("Файл не знайдено")
    except Exception as dataEror:
        print(f"Сталася помилка: {dataEror}")
