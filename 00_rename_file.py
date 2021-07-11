import os
import sys


def switch_folder(folder: str) -> None:
    print(f'Switching to folder [{folder}]')
    try:
        os.chdir(folder)
    except OSError as e:
        print('Unable to open folder:', e)
        sys.exit(0)


def rename_files_in_cur_dir(str_old: str, str_new: str) -> None:
    dont_prompt: bool = False
    for fn_old in os.listdir():
        if str_old not in fn_old:
            continue                # Current file is not a match.  Go to next one.
        fn_new: str = fn_old.replace(str_old, str_new)
        if dont_prompt:
            print(f'Rename:\n{fn_old}\n{fn_new}')
        else:
            resp = input(f'{fn_old}\n{fn_new}\nRename? [Yes:default No All Reset Quit]?\t')
            if resp == 'n':
                continue
            if resp == 'a':
                dont_prompt = True
            if resp == 'r':     # Reset search/replace
                break
            if resp == 'q':
                sys.exit(0)

        if os.path.isfile(fn_new):
            print(fn_new, ' already exists! ********************')
            continue

        try:
            os.rename(fn_old, fn_new)
        except OSError as e:
            print('Error: Rename failed:', e)
            sys.exit(0)


def rename_files() -> None:
    """ Based on how this Python script is executed, cwd can be C:\\Windows\\System32, or
    C:\\Users\\BabBa, or the correct folder.  Get to folder where target files are located.
    NOTE: We rename files in current folder and its subfolder before asking for new str_old str_new.
    """
    cwd = os.getcwd()
    resp = input(f'Enter home dir:\n{cwd}\n')
    if len(resp) > 1:
        cwd = resp

    while 1:
        switch_folder(cwd)

        if (str_old := input('\nEnter old string [Quit]:\t')) == 'q':
            sys.exit(0)

        if (str_new := input('Enter new string [Quit]:\t')) == 'q':
            sys.exit(0)

        rename_files_in_cur_dir(str_old, str_new)
        switch_folder(cwd+'\\000_Seen')
        rename_files_in_cur_dir(str_old, str_new)


def y2_y4_digit() -> None:
    """Change [yymmdd] to [yyyy-mm-dd]"""
    print('In y2_y4_digit()')


if __name__ == '__main__':
    if (resp := input(  "\na: Change [yymmdd] to [yyyy-mm-dd]"
                        "\nb: Rename files (default)"
                        "\nEnter option (q to quit):\t : ")) == 'q':
        print()
        sys.exit(0)
    if resp == 'a':
        y2_y4_digit()
    else:
        rename_files()
    print("\n")