import glob
import os
from datetime import datetime

import xlrd
import xlwt
from tqdm import tqdm
import tushare as ts


def is_tariff(tariff, hs_code):
    hs_code = set(hs_code)
    return bool(tariff & hs_code)


def get_period(date):
    period = datetime(2018, 3, 22)
    for i in range(len(date)):
        time = datetime.strptime(date[i], '%Y/%m/%d')
        if time < period:
            return i
    return len(date)


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
    # compute
    code = file.replace('company data/', '').replace('.xls', '')
    n = len(date)
    j = get_period(date)
    cif_0 = [0 if x == '' else x for x in cif]
    transaction_2nd_period_with_cif = sum(1 if x != '' else 0 for x in cif[:j])
    transaction_2nd_period = j
    cif_2nd_period = sum(cif_0[:j])
    transaction_1st_period_with_cif = sum(1 if x != '' else 0 for x in cif[j:])
    transaction_1st_period = n - j
    cif_1st_period = sum(cif_0[j:])
    ###
    ts_code = code + '.SZ'
    start1 = end1 = start2 = end2 = total_mv1 = circ_mv1 = total_mv2 = circ_mv2 = None
    try:
        ind = df1[df1.ts_code == ts_code].index.tolist()[0]
        start1 = df1.ix[ind]['open']
        end1 = df1.ix[ind]['close']
        total_mv1 = df3.ix[ind]['total_mv']
        circ_mv1 = df3.ix[ind]['circ_mv']
        ind = df2[df2.ts_code == ts_code].index.tolist()[0]
        start2 = df2.ix[ind]['open']
        end2 = df2.ix[ind]['close']
        total_mv2 = df4.ix[ind]['total_mv']
        circ_mv2 = df4.ix[ind]['circ_mv']
    except:
        print(code)
    return hs_code, code, transaction_1st_period, transaction_2nd_period, transaction_1st_period_with_cif, transaction_2nd_period_with_cif, cif_1st_period, cif_2nd_period,start1,end1,start2,end2,total_mv1, circ_mv1,total_mv2,circ_mv2


def main():
    # reading tariff data
    tariff = read_tariff_data('tariff list adjusted.xlsx')

    # ready to write
    workbook = xlwt.Workbook(encoding='utf-8')
    tariff_sheet = workbook.add_sheet('tariff')
    non_tariff_sheet = workbook.add_sheet('non tariff')
    title = ['code', 'No. of Transaction in 1st priod',
             'No. of Transaction in 2nd priod',
             'No. of Transaction in 1st priod with cif data',
             'No. of Transaction in 2nd priod with cif data',
             'total CIF in 1st period',
             'total CIF in 2nd period',
             '3.21start','3.21end','3.22start','3.22end',
             '3.21total_mv','3.21circ_mv','3.22total_mv', '3.22circ_mv']
    for i, value in enumerate(title):
        tariff_sheet.write(0, i, value)
        non_tariff_sheet.write(0, i, value)
    # reading and dealing with the company data
    company_list = glob.glob(os.path.join('company data', '*.xls'))
    # company_list = [os.path.join('company data', '000333.xls')]
    i = j = 1
    for company in tqdm(company_list):
        result_list = deal_company_data(company)
        if is_tariff(tariff, result_list[0]):
            for k, value in enumerate(result_list[1:]):
                tariff_sheet.write(i, k, value)
            i += 1
        else:
            for k, value in enumerate(result_list[1:]):
                non_tariff_sheet.write(j, k, value)
            j += 1
    workbook.save('transaction data2.xls')


if __name__ == '__main__':
    pro = ts.pro_api()
    df1 = pro.daily(trade_date='20180321')
    df2 = pro.daily(trade_date='20180322')
    df3 = pro.daily_basic(ts_code='', trade_date='20180321', fields='ts_code,total_mv,circ_mv')
    df4 = pro.daily_basic(ts_code='', trade_date='20180322', fields='ts_code,total_mv,circ_mv')
    main()
