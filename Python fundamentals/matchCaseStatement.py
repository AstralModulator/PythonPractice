#match case
from operator import truediv


def which_day(day):
    match day:
        case 1:
            return f"Sunday"
        case 2:
            return f"Monday"
        case 3:
            return f"Tuesday"
        case 4:
            return f"Wednesday"
        case 5:
            return f"Thursday"
        case 6:
            return f"Friday"
        case 7:
            return f"Saturday"
        case _:
            return f"N/A"
print(which_day(1))

def is_weekend(day):
    match day:
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            return False
        case "Saturday" | "Sunday":
            return True
        case _:
            return "Not a valid day"
print(is_weekend("Pizza"))