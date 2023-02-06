# 工具脚本，将多个目录下的文件合并到一个目录之中
# 为了保证工具的准确性，需要将合并的目录的放在同一级目录之中，并且在该目录运行本脚本。
# 另外，或许需要在上一级目录中创建target文件夹，保证所有的文件放在那里。
import os
import shutil
list_dir = os.listdir('./')
# current_folder = os.getcwd()
for sub_dir in list_dir:
    print(sub_dir)
    for contents in os.listdir(sub_dir):
        print("contents----------" + contents)

        source_content = './' + sub_dir +'/'+ contents
        

        destination_move = os.path.join('../', 'target')
        print(source_content,'to',destination_move)


        if os.path.exists(destination_move + '/' + contents):
            pass
        else:
            shutil.move(source_content, destination_move)
