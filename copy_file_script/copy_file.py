import os,sys,re

def inner_copyfiles(filename,srcPath,destPath):
    srcfile = srcPath+'/'+filename
    destfile = destPath + '/' + filename
    with open(srcfile,'rb') as fr:
        with open(destfile,'wb') as fw:
            for line in fr.readlines():
                fw.write(line)
    return True



def copyFile(srcPath):
    all_file_names = os.listdir(srcPath)
    destPath = srcPath + '-副本'

    while True:
        if not os.path.exists(destPath):
            try:
                os.mkdir(destPath)
                break
            except:
                print('mkdir wrong')
        else:
            destPath=destPath+'-副本'


    all_num = len(all_file_names)
    num=0
    for file in all_file_names:
        done= inner_copyfiles(file,srcPath,destPath)
        if done:
            num+=1

        print('copy %.1f'%((num/all_num)*100)+'%')


if __name__ == '__main__':
    while True:
        srcPath = input('请输入要拷贝的目录:')
        if not os.path.exists(srcPath):
            reply = input('目录不存在，重新输入（y/n）:')
            if reply == 'y' or reply =='Y':
                continue
            else:
                sys.exit()
        break

    copyFile(srcPath)

