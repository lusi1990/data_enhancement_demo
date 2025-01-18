import os

path = './class_image'


def rename_file():
    for name in os.listdir(path):
        if '(' in name:
            new_name = name.replace('(', '').replace(')', '').replace(' ', '')
            print(name, new_name)
            os.rename(os.path.join(path, name), os.path.join(path, new_name))


def remove_digit(name):
    """

    Args:
        name:

    Returns:

    """
    n_c = list()
    for c in name:
        if c.isdigit():
            continue
        n_c.append(c)
    return ''.join(n_c)


def check_class_not_exist():
    classes = open(r'D:\geetest\image0920\labels\classes.txt').read().strip().splitlines()
    for name in os.listdir(path):
        class_ = name.replace('.jpg', '')
        class_ = remove_digit(class_)
        if class_ not in classes:
            print(class_, 'not exist')


if __name__ == '__main__':
    rename_file()
    check_class_not_exist()
