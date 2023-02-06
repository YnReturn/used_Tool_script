import os
import shutil
list_dir = os.listdir('./')
current_folder = os.getcwd()
for sub_dir in list_dir:
    print(sub_dir)
    for contents in os.listdir(sub_dir):
        print("contents----------" + contents)
        # make the path of the content to move
        source_content = './' + sub_dir +'/'+ contents
        
        # make the path with the current folder
        destination_move = os.path.join('../', 'target')
        print(source_content,'to',destination_move)
        # move the filex

        if os.path.exists(destination_move + '/' + contents):
            pass
        else:
            shutil.move(source_content, destination_move)
