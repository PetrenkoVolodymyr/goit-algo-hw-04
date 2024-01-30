def total_salary(path):
    try:
        with open(path) as file:
            sum = 0
            lines = file.readlines()
            for line in lines:
                salary = float(line.split(',')[1])
                sum += salary
            average = sum / len(lines)
            outcome = (sum, average)
    except Exception as error:
        outcome = type(error).__name__
    return(outcome)




path = r"D:\Projects\HTML_CSS\HWks\goit-algo-hw-04\task_one\salaries.txt"
total_salary(path)