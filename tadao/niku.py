import glob
import os
from datetime import datetime

import xlrd
import xlwt
from tqdm import tqdm


def is_tariff(tariff, hs_code):
    hs_code = set(hs_code)
    return bool(tariff & hs_code)


def read_tariff_data(file):
    tariff_data = xlrd.open_workbook(file)
    tariff_table = tariff_data.sheets()[0]
    return set([str(int(x)) for x in tariff_table.col_values(0)])


def deal_company_data(file):
    # read
    company_data = xlrd.open_workbook(file)
    company_table = company_data.sheets()[0]
    date = company_table.col_values(1)[1:]
    hs_code = company_table.col_values(4)[1:]
    cif = company_table.col_values(36)[1:]
    transaction = [0]*24
    ncif = [0] * 24
    for i in range(len(date)):
        time = datetime.strptime(date[i], '%Y/%m/%d')
        d = 1 if time.day > 22 else 0
        k = (time.year-2017)*12 + (time.month - 4) + d
        transaction[k] += 1
        if cif[i] != '':
            ncif[k] += cif[i]

    return hs_code, transaction, ncif


def main():
    # reading tariff data
    tariff = read_tariff_data('tariff list adjusted.xlsx')

    # ready to write
    workbook = xlwt.Workbook(encoding='utf-8')
    transaction_sheet = workbook.add_sheet('transaction')
    cif_sheet = workbook.add_sheet('cif')
    title = ['month', 'tariff',
             'non tariff']
    for i, value in enumerate(title):
        transaction_sheet.write(0, i, value)
        cif_sheet.write(0, i, value)
    # reading and dealing with the company data
    company_list = glob.glob(os.path.join('company data', '*.xls'))
    # company_list = [os.path.join('company data', '000333.xls')]
    i = j = 1
    tariff_transaction = [0]*24
    tariff_cif = [0] * 24
    non_tariff_transaction = [0]*24
    non_tariff_cif = [0] * 24
    for company in tqdm(company_list):
        result_list = deal_company_data(company)
        if is_tariff(tariff, result_list[0]):
            tariff_transaction = [tariff_transaction[i] + result_list[1][i] for i in range(24)]
            # tariff_transaction = [x + y for x in tariff_transaction for y in result_list[1]]
            tariff_cif = [tariff_cif[i] + result_list[2][i] for i in range(24)]
            # tariff_cif = [x + y for x in tariff_cif for y in result_list[2]]
        else:
            non_tariff_transaction = [non_tariff_transaction[i] + result_list[1][i] for i in range(24)]
            non_tariff_cif = [non_tariff_cif[i] + result_list[2][i] for i in range(24)]
            # non_tariff_transaction = [x + y for x in non_tariff_transaction for y in result_list[1]]
            # non_tariff_cif = [x + y for x in non_tariff_cif for y in result_list[2]]
    for i in range(1, 25):
        transaction_sheet.write(i, 0, period[i - 1].strftime('%Y/%m/%d -'))
        transaction_sheet.write(i, 1, tariff_transaction[i - 1])
        transaction_sheet.write(i, 2, non_tariff_transaction[i - 1])
        cif_sheet.write(i, 0, period[i - 1].strftime('%Y/%m/%d -'))
        cif_sheet.write(i, 1, tariff_cif[i - 1])
        cif_sheet.write(i, 2, non_tariff_cif[i - 1])
    workbook.save('niku_data.xls')


if __name__ == '__main__':
    period = []
    for i in range(3, 13):
        period.append(datetime(2017, i, 22))
    for i in range(1, 13):
        period.append(datetime(2018, i, 22))
    for i in range(1, 3):
        period.append(datetime(2019, i, 22))
    main()
