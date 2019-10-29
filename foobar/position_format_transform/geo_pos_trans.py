import sys

import xlrd
import xlwt
from position_format_transform.pair_transform import gcj02towgs84
print(sys.path)


def read():
    rows, cols = old_sheet.nrows, old_sheet.ncols
    for row in range(rows):
        row_values = []
        for col in range(cols):
            row_values.append(old_sheet.cell(row, col).value)
        row_values[LEFT], row_values[RIGHT] = FUNC(row_values[LEFT], row_values[RIGHT])
        yield row_values


def write():
    style = xlwt.XFStyle()
    font = xlwt.Font()
    font.name = '宋体'
    font.height = 220
    style.font = font

    for row_index, row_values in enumerate(read()):
        for col_index, cell_value in enumerate(row_values):
            new_sheet.write(row_index, col_index, cell_value, style)
    try:
        write_wb.save(OUTPUT_FILE)
    except PermissionError as e:
        print('Write failed! Please close it first in your excel.')


if __name__ == '__main__':
    FUNC = gcj02towgs84
    # FUNC = wgs84togcj02

    # left and right index of geo position
    LEFT = 0
    RIGHT = 1

    # input and output file
    INPUT_FILE = 'od.xls'
    OUTPUT_FILE = 'sz_population_new.xls'

    # create workbook sheet for reading
    read_wb = xlrd.open_workbook(INPUT_FILE)
    old_sheet = read_wb.sheets()[0]

    # create workbook sheet for writing
    write_wb = xlwt.Workbook()
    new_sheet = write_wb.add_sheet('new')

    write()
