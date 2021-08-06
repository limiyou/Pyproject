#尽量避免自己
def eat(food):
    print(f"这个人爱吃{food}")
    eat(food)
eat("辣条")

