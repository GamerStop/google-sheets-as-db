from gspread.models import Cell
import gspread

gc = gspread.service_account(filename="creds.json")

t1 = gc.open_by_key('1UsRqPaA0L5KW6JBm1eA-DaR9T89L02JuMlbbd63GfGI')
t2 = gc.open_by_key('1d4HZame4LxveGQ5st78oyc3b41CprNMp9IisKXgZhK0')

table_1 = t1.sheet1
table_2 = t2.sheet1

id_ = 1
name_ = 2

def add_name(txt):
	changes = []
	global len_of_id, name_, id_
	len_of_id = len(table_1.col_values(id_))
	changes.append(Cell(row=len_of_id+1, col=id_, value=len_of_id))
	changes.append(Cell(row=len_of_id+1, col=name_, value=txt))
	table_1.update_cells(changes)

add_name('dolev swisa')
add_name('Jonathan Levy')
add_name('Aviv yaskil')
add_name('Yarin dashevski')