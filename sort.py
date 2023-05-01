from pathlib import Path
import re
# import sys


file_ext = {"Images": [".jpg", ".jpeg", ".png", ".svg", ".bmp", ".svg", ".gif", ".webp", ".tiff", ".ico", ".psd", ".eps", ".pict", ".pcx", ".cdr", ".ai", ".raw"], "Documents": [".txt", ".doc", ".docx", ".docm", ".pdf", ".md", ".epub", ".ods", ".dotx", ".odt", ".xml", ".ppt", ".pptx", ".csv", ".xls", ".xlsx", ".wpd", ".rtf", ".rtfd", ".rvg", ".dox"], "Audio": [".aac", ".m4a", ".mp3", "ogg", ".wav", ".wma", ".amr", ".midi", "flac", ".alac", ".aiff",
                                                                                                                                                                                                                                                                                                                                                                          ".mqa", ".dsd", ".asf", ".vqf", ".3ga"], "Video": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mpg", ".mpeg", ".3gp", ".mkv", ".swf", ".ifo", ".rm", ".ra", ".ram", ".m2v", ".m2p"], "Archives": [".zip", ".gz", ".tar", ".rar", ".7z", ".dmg", ".iso"], "HTML": [".html", ".htm", ".xhtml"], "EXE_MSI": [".exe", ".msi"], "PYTHON": [".py", ".pyw"], "APKS": [".apk", ".npbk"], "Torrent": [".torrent"], "Figma": [".fig"], "unknown": []}

CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r",
               "s", "t", "u", "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")
TRANS = {}

for c, l in zip(list(CYRILLIC_SYMBOLS), TRANSLATION):
    TRANS[ord(c)] = l
    TRANS[ord(c.upper())] = l.upper()


def normalize(name: str) -> str:
    trans_name = name.translate(TRANS)
    trans_name = re.sub(r'\W', '_', trans_name)
    return trans_name


def move_file(file: Path, root_dir: Path, category: str):
    target_folder = root_dir / category
    if not target_folder.exists():
        target_folder.mkdir()
    file.replace(target_folder / f"{normalize(file.stem)}{file.suffix}")


def get_category(item: Path):
    for category, exts in file_ext.items():
        if item.suffix.lower() in exts:
            return category
    return "unknown"


def rm_dir(dir: Path):
    try:
        dir.rmdir()
    except OSError as e:
        print(e)


def sort_dir(sub_dir: Path, root_dir: Path):
    for item in list(sub_dir.glob('**/*'))[::-1]:
        if item.is_file():
            category = get_category(item)
            move_file(item, root_dir, category)
        else:
            rm_dir(item)


def sort_func(path_dir: Path):
    for item in [p for p in path_dir.glob('*') if p.name.lower() not in file_ext.keys()][::-1]:
        if item.is_dir():
            sort_dir(item, path_dir)
            rm_dir(item)
        else:
            category = get_category(item)
            move_file(item, path_dir, category)


def main():
    try:
        print('===========Cleaning Folder===========\n')
        user_input = input('Enter the full path to the folder >>>> ')
        path = Path(user_input) 
        # path = Path(sys.argv[1])
        sort_func(path)
        print('OK. Process has been finished!')
        query = input('Want to repeat with another folder ? (yes/no)\n>>>> ')
        if query.lower() == 'yes':
            main()
    except:
        if not Path(user_input).exists():
            print('!!! The directory not found')
            return None
        # sort_func(path)
        # print('OK. Process has been finished!')
        query = input('Want to repeat with another folder ? (yes/no)\n>>>> ')
        if query.lower() == 'yes':
            main()
        else:
            return None
    # except IndexError:
    #     print("Type path to folder as parameter on call script")
    #     return None
    # if not Path(path).exists():
    #     print('!!! The directory not found')
    #     return None
    # sort_func(path)
    # print('OK. Process has been finished!')


if __name__ == "__main__":
    main()
