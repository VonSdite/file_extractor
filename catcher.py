import os
import sys
import shutil

TARGET_PATH = './SAVE_FILES'          # 保存目标文件的目录

def usb_copy(extension, usb_path):
    usb_walk = list(os.walk(usb_path))                  # os.walk()是目录遍历函数
    for file_walk in usb_walk:
        file_root = file_walk[0].replace('\\', '/')     # 当前文件的目录
        file_files = file_walk[2]                       # 当前目录内所有文件

        for file in file_files:
            file = file_root + '/' + file               # 文件名

            if os.path.splitext(file)[-1] == extension:
                # 判断是否是目标扩展名文件
                # 是则copy一份
                
                # save_path 保持文件原来的目录结构
                save_path = TARGET_PATH + os.path.splitdrive(file_root)[-1]
                save_path_split = save_path.split('/')
                path = save_path_split[0]
                for tmp in save_path_split[1:]:
                    path += '/' + tmp
                    if not os.path.isdir(path):
                        os.mkdir(path)

                shutil.copy(file, save_path)

if __name__ == '__main__':
    try:
        extension = sys.argv[1]         # 扩展名, 如 .ppt
    except IndexError as e:
        print('[Error]: 请输入要获取的文件扩展名', e)
        sys.exit()

    roots = sys.argv[2:]        # 从sys.argv中获取所要遍历的目录

    for root in roots:
        usb_copy(extension, root)

