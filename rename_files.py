import os
import shutil

TICKERS = ['AUDCAD', 'AUDCHF', 'AUDJPY', 'AUDNZD', 'AUDUSD', 'CADCHF', 'CADJPY', 'CHFJPY', 'EURAUD', 'EURCAD', 'EURCHF',
           'EURGBP', 'EURJPY', 'EURNZD', 'EURUSD', 'GBPAUD', 'GBPCAD', 'GBPCHF', 'GBPJPY', 'GBPNZD', 'GBPUSD', 'NZDCAD',
           'NZDCHF', 'NZDJPY', 'NZDUSD', 'USDCAD', 'USDCHF', 'USDJPY']


def process_file(processing_folder):
    for d in [_dir for _dir in os.listdir(processing_folder) if os.path.isdir(_dir)]:
        if len(d) >= 8 and str.isnumeric(d[0:8]):
            rename_files(processing_folder, d)


def rename_files(processing_folder, sub_dir):
    dir = os.path.join(processing_folder, sub_dir)
    dir_files = os.listdir(dir)
    dir_files.sort()
    for i in range(0, len(dir_files)):
        old_file = os.path.join(dir, dir_files[i])
        new_file = os.path.join(processing_folder, 'weekly', '{0}_{1}.png'.format(TICKERS[i], sub_dir))
        shutil.move(old_file, new_file)


if __name__ == '__main__':
    process_file('.')
