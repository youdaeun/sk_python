from openpyxl import Workbook
wb = Workbook()

ws = wb.active
ws.title = "New Title"

for row in ws['A1:D4']:
    print(f"row:{row}")
    for cell in row:
        print(f"cell:{cell}")
        cell.value = 'Hello World'

wb.save('test_ex1.xlsx')
