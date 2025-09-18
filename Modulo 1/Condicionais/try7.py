def divide(x,y):
    try:
        result= x/y
    except ZeroDivisionError:
        print("por favor, nao utilize zeros!")
    except:
        print("\033[91m algo deu errado...]")
    else:
        print(f"seu resultado e:{result}")
    finally:
        print("\033[92m vamos de novo?]")
#divide(13,0)
#divide("a",0)
#divide("s",0)
#divide(13,0)
print("---x----")
import random
value=random.randint(0,2)
match value:
    case 0:
        print("zero!")
    case 1:
        print("um!")
    case 2:
        print("dois!")