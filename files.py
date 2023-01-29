import argparse
from pathlib import Path
from shutil import move
from multiprocessing import Process, current_process

parser = argparse.ArgumentParser(description='Sorting folder')
parser.add_argument('--source', '-s', required=True, help='Source folder')
parser.add_argument('--output', '-o', default='dist', help='Output folder')
args = vars(parser.parse_args())
source = args.get('source')
output = args.get('output')
output_folder = Path(output)  # dist


def read_folder(path: Path) -> None:
    print(f'Start: {current_process().name} in {path}')
    for el in path.iterdir():
        if el.is_dir():
            pr_rf = Process(target=read_folder, args=(el,))
            pr_rf.start()
        else:
            process_file(el)
    print(f'Finish: {current_process().name} in {path}')
    path.rmdir() # папка обработана, исходную пустую папку удаляем


def process_file(file: Path) -> None:
    ext = file.suffix.upper()
    if ext in ['JPEG', 'PNG', 'JPG', 'SVG']:
        move_to_folder = 'Images'
    elif ext == 'MP3':
        move_to_folder = 'audio'
    else:
        move_to_folder = 'MY_OTHER'
    new_path = output_folder / move_to_folder
    new_path.mkdir(exist_ok=True, parents=True)
    move(file, new_path / file.name) # перемещаем файл


if __name__ == '__main__':
    # read_folder(Path(source))
    pr_rf = Process(target=read_folder, args=(Path(source), ))
    pr_rf.start()
    pr_rf.join()
    print('Finished')