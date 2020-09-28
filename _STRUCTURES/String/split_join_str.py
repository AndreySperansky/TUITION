

def make_cell(cells_in_row, cell):
	cell = '*' * cell
	chunks = [cell[x: x + cells_in_row]  for x in range(0, len(cell), cells_in_row)]    # разбираем
	res = r"\n".join(chunks)            #собираем
	return print(res)

make_cell(7, 51)