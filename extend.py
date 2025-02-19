import json
import shutil
import os
import sys
from collections import defaultdict
from datetime import datetime

#存储键为拓展名（由于os.path.splitext返回的是'.ext'，所以加了.开头），值为目录的字典
#由于后面日志要获取每个子目录的名称，所以这里的值用tuple
ext_dir={'.quantum':('quantum_core','SECTOR-7G'),'.holo':('hologram_vault','CHAMBER-12F'),'.exo':('exobiology_lab','POD-09X'),'.chrono':('temporal_archive','VAULT-00T')}

#未知文件存储目录，也用tuple存储
unknownFile_dir=('quantum_quarantine',)#加个,防止认为是括号

#处理文件，传入路径，根据题意知存放在incoming_data下，所以用默认变量
def process_files(directory='./incoming_data/',time=None):
    #新建一个空列表，存储已经处理好的文件
    #这里为了可视化将未知文件放到最后一个，所以用两个列表
    knownFile_processed_files = []
    unKnownFile_processed_files = []

    #遍历目录下的所有文件
    for filename in os.listdir(directory):
        #缓存文件路径，利用os.path.isfile()来判断是否是合法文件
        filepath=os.path.join(directory, filename)

        #如果说不是合法文件或者文件以.开头（即如果是隐藏文件），就跳过该文件并判断下一个文件
        if not os.path.isfile(filepath) or filename.startswith('.'):
            continue

        #利用os.path.splitext记录拓展名。
        #os.path.splitext返回的是一个列表且拓展名在第二个元素，所以利用filename[1]
        #由于题目没说是否考虑大写，这里就用lower()统一小写好了
        ext=os.path.splitext(filename)[1].lower()

        #如果拓展名是在拓展名字典中已知的，则文件存储的目录就是对应键值对的值，文件名称不变，isUnknown=False
        if ext in ext_dir:
            cat_dir=ext_dir[ext]
            new_filename=f'{time}_{filename}'
            isUnknown=False#这里isUnknown是为了给后面日志输出用的
            #把相同后缀加入到一个字典列表里面
            pass
        #否则的话，文件存储的目录是unknownFile_dir，新名字要加前缀，isUnknown=True
        else:
            cat_dir=unknownFile_dir
            #如果说原来就有ENCRYPTED前缀，那么名字就不用变（这里是我猜测的，题目没说我也不知道要不要qwq）
            if filename.split('_')[0]=='ENCRYPTED':
                new_filename=f'{time}_{filename}'
            else:
                new_filename=f'{time}_ENCRYPTED_{filename}'#用f-string进行格式化
            isUnknown=True
            #把相同后缀加入到一个字典列表里面
            pass

        #缓存最终的目录路径
        desDir_path=os.path.join(directory,*cat_dir)#解包tuple

        #利用os.makedirs创建目录，如果已经创建，则不需要再创建，所以应是exist_ok=True
        os.makedirs(desDir_path, exist_ok=True)

        #缓存最终的文件路径
        desFile_path=os.path.join(desDir_path,new_filename)

        #利用shutil.move移动文件
        shutil.move(filepath, desFile_path)

        #这里为了可视化将未知文件放到最后一个，所以用两个列表
        if not isUnknown:
            knownFile_processed_files.append({'cat_dir':cat_dir,'new_filename':new_filename})
        else:
            unKnownFile_processed_files.append({'cat_dir': cat_dir, 'new_filename': new_filename})

    #循环结束之后返回处理过的文件信息列表
    return knownFile_processed_files,unKnownFile_processed_files

#生成全息日志文件hologram_log.txt，传入路径，已处理过的文件信息，log存放的路径（根据题意知存放在incoming_data下，所以用默认变量）
#可以选择文本，1代表纯文本，2代表json格式
def generate_hologram_log(files,time,format_mode=1,directory='./incoming_data/'):
    #如果是纯文本
    if format_mode==1:
        #log_path记录存放日志的文件路径
        log_path=os.path.join(directory,'hologram_log.txt')

        #按目录分组文件
        #这里用defaultdict来存储文件信息，不用普通的字典，因为普通的字典初始化很麻烦，且不能动态分配空间
        cat_groups=defaultdict(list)

        #遍历processed_files的文件信息，并以目录名称为键，存储标志和文件名称
        #先遍历已知文件
        for file_info in files[0]:
            dir=file_info['cat_dir']
            file=file_info['new_filename']
            symbol='🔮'
            cat_groups[dir].append({'symbol':symbol,'file':file})

        #再遍历未知文件
        for file_info in files[1]:
            dir = file_info['cat_dir']
            file = file_info['new_filename']
            symbol = '⚠️'
            cat_groups[dir].append({'symbol': symbol, 'file': file})

        #打印起始信息和根目录
        lines = [
            "┌───────────────────────────────────────────┐",
            "│ 🛸 Xia-III 空间站数据分布全息图 │             ",
            "└───────────────────────────────────────────┘",
            "",
            f"├─🚀 {os.path.basename(os.path.normpath(directory))}"#os.path.normpath是规范化目录，os.path.basename是取目录的最后一个部分即incoming_data
        ]

        #用一个列表记录每一行
        dir_lines=[]

        #存储目录和文件信息到列表
        for dir in cat_groups:
            #子目录的起始缩进
            dir_start = f'│   '

            #存储目录
            for child_dir in dir:
                dir_lines.append(f'{dir_start}├─🚀 {child_dir}')
                dir_start+=f'│   '

            #记录标志和文件名称
            for filename in cat_groups[dir]:
                #存储文件
                dir_lines.append(f'{dir_start}├─{filename['symbol']} {filename["file"]}')

        #加入lines
        lines.extend(dir_lines)

        #添加时间和警告
        timeAndClaim = [
            "",
            f"🤖 SuperNova · 地球标准时 {time}",
            "⚠️ 警告：请勿直视量子文件核心"
        ]

        lines.extend(timeAndClaim)

        #写入日志
        #用utf-8编码，确保能处理中文和Unicode符号
        with open(log_path,'w',encoding='utf-8') as f:
            f.write('\n'.join(lines))#用\n连接列表的每一个字符串

    #否则如果是JSON格式
    elif format_mode==2:
        #log_path记录存放日志的文件路径
        log_path = os.path.join(directory, 'hologram_log.json')

        #按目录分组文件
        #这里用defaultdict来存储文件信息，不用普通的字典，因为普通的字典初始化很麻烦，且不能动态分配空间
        json_data = defaultdict(list)

        #遍历processed_files的文件信息，并以目录名称为键，存储标志和文件名称
        #先遍历已知文件
        for file_info in files[0]:
            dir_tuple=file_info['cat_dir']

            #获取最上层的目录
            #由于题目没说子目录，所以这里应该是取最上层目录
            top_dir=dir_tuple[0]

            #获取文件名
            file=file_info['new_filename']

            #添加到json_data中
            json_data[top_dir].append(file)

        #再遍历未知文件
        for file_info in files[1]:
            dir_tuple=file_info['cat_dir']

            #获取最上层的目录
            #由于题目没说子目录，所以这里应该是取最上层目录
            top_dir=dir_tuple[0]

            #获取文件名
            file=file_info['new_filename']

            #添加到json_data中
            json_data[top_dir].append(file)

        #写入json文件中
        with open(log_path,'w',encoding='utf-8') as f:
            #indent是缩进，这里缩进4格
            #ensure_ascii=False代表允许非ascii码的字符如中文
            #利用json.dump序列化列表为json格式，并写入文件
            json.dump(dict(json_data),f,indent=4,ensure_ascii=False)

#如果在交互器中运行，可以有个重置已经处理过的incoming_data
#直接复制incoming_data_copy成incoming_data
def Reset():
    #用try语句判断当前是否存在incoming_data
    if os.path.exists('incoming_data/'):
        shutil.rmtree('incoming_data')
        shutil.copytree('incoming_data_copy', 'incoming_data')
        print('已重置')
    else:
        print('还没有incoming_data文件夹')


#文件分类测试，供在交互器使用
def testFile(path='./incoming_data/'):
    # 生成时间戳（精确到毫秒）
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')

    # 处理文件,并返回用列表存储的处理文件的信息（包括文件拓展名对应的目录，文件的新名字，文件是否是未知文件，文件的最终存储目录）
    processed_files = process_files(path,timestamp)
    print(processed_files)

#日志输出测试，供在交互器使用
def testLog(format_mode=1):
    # 生成时间戳（精确到毫秒）
    # 用于最后log
    timestampLog = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')

    # 传入随便一个列表
    test_files = ([{'cat_dir': ('knowntest1', 'knowntest2'), 'new_filename': 'knowntest'}],[{'cat_dir': ('unKnowntest1', 'unKnowntest2'), 'new_filename': 'unknowntest'}])

    generate_hologram_log(test_files,timestampLog,format_mode)

#主程序，供在交互器使用
def main(path='./incoming_data/',format_mode=2):
    # 生成时间戳（精确到毫秒）
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    # 用于最后log
    timestampLog = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')

    # 处理文件,并返回用列表存储的处理文件的信息（包括文件拓展名对应的目录，文件的新名字，文件是否是未知文件，文件的最终存储目录）
    processed_files = process_files(path,timestamp)
    generate_hologram_log(processed_files,timestampLog,format_mode)

#如果在命令行或者直接在软件运行而非作为导入模块在交互器使用
if __name__=='__main__':
    #默认路径，不在命令行运行或者在命令行运行且格式是python base.py时默认目录是default_path
    default_path= 'incoming_data/'
    test_flag=False#初始化状态
    text_flag=1#初始化文档状态

    #这里是在命令行输入参数进行各个函数运行调试
    #如果在命令行运行，并且格式是python base.py directory则切换目录
    #如果格式是python base.py test_file或者test_log，则目录是默认目录，而且进行文件分类或日志输出的调试
    #如果格式是python base.py directory test_file或者test_log，则既改变目录又进行调试
    if len(sys.argv)>=2:
        #如果说第一个参数是test_file或者test_log的话，路径为默认路径
        if sys.argv[1] in ['test_file','test_log']:
            #用test_flag来缓存状态
            test_flag=sys.argv[1]
            if len(sys.argv)>=3 and sys.argv[1]=='test_log':
                if sys.argv[2] in ['1','2']:
                    text_flag=int(sys.argv[2])
        #如果说第一个参数是数字的话
        elif sys.argv[1] in ['1','2']:
            text_flag=int(sys.argv[1])
        #否则是目录的话，默认路径变为参数
        else:
            default_path=sys.argv[1]
            #如果说还输入了test_file或者test_log
            if len(sys.argv)>=3:
                if sys.argv[2] in ['test_file','test_log']:
                    test_flag=sys.argv[2]
                    if len(sys.argv)>=4:
                        if sys.argv[3] in ['1','2']:
                            text_flag=int(sys.argv[3])
                elif sys.argv[2] in ['1','2']:
                    text_flag=int(sys.argv[2])

        # 如果是文件测试
        if test_flag == 'test_file':
            testFile()
        # 如果是日志测试
        elif test_flag == 'test_log':
            testLog(text_flag)
        else:
            main(default_path,text_flag)
    #否则如果直接在pycharm或者vscode运行，直接输出内容
    else:
        main(default_path)




