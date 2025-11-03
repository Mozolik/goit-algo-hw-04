
def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            sum_line = 0
            line_count = 0
            for string_line in file.readlines():
                content = string_line.split(",")
                sum_line += float(content[1].strip())
                line_count += 1
            try:
                average = sum_line/line_count
                return (sum_line, average)
            except ZeroDivisionError:
                print("Помика ділення на 0")
                return ()
    except FileNotFoundError:
        print("Файл не знайдено")
        return ()
    except Exception as data_eror:
        print(f"Сталася помилка: {data_eror}")
        return ()
