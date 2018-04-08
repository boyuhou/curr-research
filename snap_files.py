import click
import os
import datetime
import shutil


@click.command()
@click.option('--folder', default='snap', help='Folder with the files')
@click.option('--archive_folder', default='snap', help='Folder with the files')
@click.option('--time', default=None, help='particualrt time in yyyymmdd_hhmmss')
def main(folder, archive_folder, time):
    if time is None:
        time = datetime.datetime.now().strftime('%Y%m%d_%H%M00')
    for f in os.listdir(folder):
        curr_dir = os.path.join('.', folder)
        archive_dir = os.path.join('.', archive_folder)
        new_file = os.path.join(archive_dir, '{0}_{1}.png'.format(f[0:6], time))
        shutil.move(os.path.join(curr_dir, f), new_file)


if __name__ == '__main__':
    main()

