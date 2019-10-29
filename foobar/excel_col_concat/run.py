import getopt
import sys
import xlrd
import xlwt


def read():
    dict = {}
    for row in range(1, sheet1.nrows):
        key = (sheet1.cell(row, left_index).value, sheet1.cell(row, right_index).value)
        if (key[1], key[0]) in dict:
            try:
                dict[(key[1], key[0])] += int(sheet1.cell(row, sum_index).value)
            except:
                pass
            continue
        if dict.get(key):
            dict[key] += int(sheet1.cell(row, sum_index).value)
        else:
            try:
                dict[key] = int(sheet1.cell(row, sum_index).value)
            except IndexError:
                print('索引值不正确！分别在123列就用-c参数指定123。')
                exit()
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
    font.name = font_name  # 指定“宋体”
    font.height = int(size) * 20
    style.font = font
    rows = handle_rows()
    workbook = xlwt.Workbook()
    worksheet = workbook.add_sheet('sheet1')
    for index, x in enumerate(head):
        worksheet.write(0, index, x, style)
    for row_index, row in enumerate(rows):
        for x in range(ncols):
            worksheet.write(row_index + 1, x, row[x], style)
    workbook.save(object_file)
    print('Success.')


def main(argv):
    global index_file, object_file, font_name, size, left_index, right_index, sum_index
    try:
        options, args = getopt.getopt(argv, "hi:o:f:s:c:")
    except getopt.GetoptError as e:
        print(e)
        sys.exit()

    for option, value in options:
        if option in ("-h", "--help"):
            print('=================参数说明=================\n-i：指定原xls/xlsx文件\n-o：指定输出的新的xls/xlsx文件\n-f：指定字体，默认{font_name}\n-s：指定字体大小，默认{size}\n-c：指定三列的索引值'.format(font_name=font_name, size=size))
            quit()
        if option == "-i":
            index_file = value
            object_file = '_1.'.join(os.path.basename(index_file).split('.'))
        if option == "-o":
            object_file = value
        if option == "-f":
            font_name = value
        if option == "-s":
            size = value
        if option == "-c":
            try:
                left_index, right_index, sum_index = map(lambda x: int(x) - 1, value)
            except ValueError:
                print('只能指定三个索引值！')
                exit()


if __name__ == '__main__':
    # default settings, modify it if needed
    index_file = ''
    import os
    object_file = ''
    font_name = '宋体'
    size = 12
    left_index = 1
    right_index = 2
    sum_index = 3

    main(sys.argv[1:])
    try:
        book = xlrd.open_workbook(index_file)
        sheet1 = book.sheets()[0]
        ncols = sheet1.ncols # 读取文件总列数
        head = sheet1.row_values(0)
        write()
    except FileNotFoundError:
        print('请使用-i参数指定原xls/xlsx文件\n例：python run.py -i example.xls\n\n其他参数说明请输入python run.py -h')

