def get_cats_info(path):
    try:
        list = []
        with open(path, encoding='utf-8') as file:
            lines = file.readlines()
            for line in lines:
                id = {"id": line.split(',')[0], 
                      "name":line.split(',')[1], 
                      "age":line.split(',')[2].rstrip("\n")}
                list.append(id)
            return(list)
    except Exception as error:
        return(type(error).__name__)


path = r"D:\Projects\HTML_CSS\HWks\goit-algo-hw-04\task_two\text.txt"
get_cats_info(path)