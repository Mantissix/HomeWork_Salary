import salary


def pay():
    print(f"已发工资{salary.money}元")
    salary.money = salary.money + 1000