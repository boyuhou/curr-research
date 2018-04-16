import click
import os
import datetime
from PIL import Image

DATE_FORMAT = '%Y%m%d'
TICKERS = ['AUDCAD', 'AUDCHF', 'AUDJPY', 'AUDNZD', 'AUDUSD', 'CADCHF', 'CADJPY', 'CHFJPY', 'EURAUD', 'EURCAD', 'EURCHF',
           'EURGBP', 'EURJPY', 'EURNZD', 'EURUSD', 'GBPAUD', 'GBPCAD', 'GBPCHF', 'GBPJPY', 'GBPNZD', 'GBPUSD', 'NZDCAD',
           'NZDCHF', 'NZDJPY', 'NZDUSD', 'USDCAD', 'USDCHF', 'USDJPY']


@click.command()
@click.option('--date', default=None, help='particualrt time in yyyymmdd')
def main(date):
    weekly_folder = os.path.join('.', 'weekly')
    snap_folder = os.path.join('.', 'snap_history')
    if None is date:
        today = datetime.date.today()
        idx = (today.weekday() + 1) % 7
        date = today - datetime.timedelta(7 + idx - 6)  # last satursday
    else:
        date = datetime.datetime.strptime(date, DATE_FORMAT)

    start_date = date.strftime(DATE_FORMAT)
    end_date = (date + datetime.timedelta(7)).strftime(DATE_FORMAT)
    for ticker in TICKERS:
        weekly_path = find_weekly_file(start_date, weekly_folder, ticker)
        snap_paths = find_snap_files(start_date, end_date, snap_folder, ticker)
        review_file_path = os.path.join('.', 'review', '{0}_{1}_{2}.png'.format(ticker, start_date, end_date))
        merge_files(weekly_path, snap_paths, review_file_path)


def merge_files(weekly_file_path, snap_file_paths, output_path):
    total_files = [weekly_file_path]
    total_files.extend(snap_file_paths)
    images = map(Image.open, total_files)
    widths, heights = zip(*(i.size for i in images))

    max_width = max(widths)
    total_height = sum(heights)

    new_image = Image.new('RGB', (max_width, total_height))

    y_offset = 0
    for f in total_files:
        im = Image.open(f)
        new_image.paste(im, (0, y_offset))
        y_offset += im.size[1]

    new_image.save(output_path)


def find_weekly_file(date, weekly_folder, ticker):
    return os.path.join(weekly_folder, '{0}_{1}.png'.format(ticker, date))


def find_snap_files(start_date, end_date, snap_folder, ticker):
    result = []
    for f in os.listdir(snap_folder):
        if f.startswith(ticker):
            snap_date = f[7:15]
            if start_date <= snap_date <= end_date:
                result.append(os.path.join(snap_folder, f))
    result.sort()
    return result


if __name__ == '__main__':
    main()
