
def sum_digits(n):
   r = 0
   while n:
       r, n = r + n % 10, n / 10
   return r

def allowed_move(x, y):
	return (sum_digits(abs(x)) + sum_digits(abs(y))) <= 19


def moves(x,y):
	possible_moves = [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]
	return [valid_move for valid_move in possible_moves if (allowed_move(*valid_move) and valid_move not in has_visited)]
		 

has_visited = {(0,0): 1}
new_moves = [(0,0)]
while(len(new_moves) != 0):
	x,y = new_moves.pop()
	for valid_move in moves(x,y):
		has_visited[valid_move] = 1
		new_moves.append(valid_move)

print len(has_visited)
