import salary


def search():
    if salary.money == 1000:
        print("工资未到账，请等待")
    else:
        print(f"工资已到账{salary.money}元,请注意查收")