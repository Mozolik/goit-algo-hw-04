
def get_cats_info(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            cats_info = [] 
            for StringLine in file.readlines():
                content = StringLine.split(",")  
                cats_info.append({"id":content[0].strip(),"name":content[1].strip(),"age":content[2].strip()})  

            return cats_info 
    except FileNotFoundError:
        print("Файл не знайдено")
        return []
    except Exception as dataEror:
        print(f"Сталася помилка: {dataEror}")
        return []

