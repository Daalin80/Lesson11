win = int(input("Please enter numbers of win: "))
draw = int(input("Please enter numbers of draw: "))
loss = int(input("Please enter numbers of loss: "))

def count_points(win, draw, loss):
    counted_points = win * 3 + draw * 1 + loss * 0
    return counted_points


print(count_points(win, draw, loss))
