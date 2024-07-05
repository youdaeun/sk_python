import openpyxl as excel

book = excel.Workbook()

sheet = book.active
cell = sheet["A1":"E7"]

for row in sheet["AI":"E7"]:
#리스트 컴프리헨션으로 결과를 리스트로 저장
    values = [cell.value for cell in row]

    for cell in row:
        values.append[cell.value]
    print(values)