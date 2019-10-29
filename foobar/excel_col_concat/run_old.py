import xlrd
import xlwt

book = xlrd.open_workbook(r'./od.xls')

sheet1 = book.sheets()[0]
head = sheet1.row_values(0)

left_index = 1
right_index = 2
sum_index = 3


def read():
    dict = {}
    rows = []

    for row in range(1, sheet1.nrows):
        key = (sheet1.cell(row, left_index).value, sheet1.cell(row, right_index).value)
        if (key[1], key[0]) in dict:
            dict[(key[1], key[0])] += int(sheet1.cell(row, sum_index).value)
            continue
        if dict.get(key):
            dict[key] += int(sheet1.cell(row, sum_index).value)
        else:
            dict[key] = int(sheet1.cell(row, sum_index).value)
    return dict


def handle_rows():
    row_values = []
    dict = read()
    for row in range(1, sheet1.nrows):
        row_value = sheet1.row_values(row)
        key = (row_value[left_index], row_value[right_index])
        if dict.get(key):
            row_value[sum_index] = dict.get(key)
            dict.pop(key)
        else:
            row_value[sum_index] = ''
        row_values.append(row_value)
    return row_values


def write():
    style = xlwt.XFStyle()

    font = xlwt.Font()

    font.name = '宋体'  # 指定“宋体”
    font.height = 240
    style.font = font
    rows = handle_rows()
    workbook = xlwt.Workbook()
    worksheet = workbook.add_sheet('test')
    for index, x in enumerate(head):
        worksheet.write(0, index, x, style)
    for index, row in enumerate(rows):
        worksheet.write(index + 1, left_index, row[left_index], style)
        worksheet.write(index + 1, right_index, row[right_index], style)
        worksheet.write(index + 1, sum_index, row[sum_index], style)
    workbook.save('od_1.xls')


if __name__ == '__main__':
    write()
