##调用的模块

import tarfile     # 压缩模块
import os          # 系统
import hashlib     # 哈希加密模块
import pickle as p # 可以在一个文件中储存任何python对象,之后又可以把它完整无缺地取出来
from time import  strftime   #调用是是时间模块的strftime函数


#######################################################################
# 定义md5校验码
def check_md5(fname):          #
    m = hashlib.md5()           #定义一个便变量m用的方法是hashlibmd5

    with open(fname, 'rb') as fobj:
        while True:
            data = fobj.read(4096)
            if not data:
                break
            m.update(data)
        return  m.hexdigest()

#######################################################################
# 定义全备函数
def full_backup(src_dir, dst_dir,md5file):
    fname = '%s_full_%s.tar.gz' % (os.path.basename(src_dir.rstrip('/')), strftime('%Y%m%d'))
    fname = os.path.join(dst_dir, fname)
    tar = tarfile.open(fname, 'w:gz')
    tar.add(src_dir)
    tar.close()

    md5_dict = {}
    for path, folders, files  in  os.walk(src_dir):        #可以先分析os.walk(),
        for each_file in files:
            key = os.path.join(path,each_file)
            md5_dict[key] = check_md5(key)

        with open(md5file, 'wb') as fobj:            #打开md5file为文件赋值给fobj
            p.dump(md5_dict, fobj)                   #将md5_dict变量写入fobj变量

#######################################################################
# 定义增量备份函数
def incr_backup(src_dir,dst_dir,md5file):
    fname = '%s_incr_%s.tar.gz' % (os.path.basename(src_dir.rstrip('/')), strftime('%Y%m%d'))
    fname = os.path.join(dst_dir, fname)

    new_md5 = {}
    with open(md5file, 'rb') as fobj:
        old_md5 = p.load(fobj)

    for path, folders, files in os.walk(src_dir):   #去除子目录
        for each_file in files:
            key = os.path.join(path, each_file)
            new_md5[key] = check_md5(key)

    with open(md5file, 'wb') as fobj:
        p.dump(new_md5, fobj)

    tar = tarfile.open(fname, 'w:gz')
    for key in new_md5:
        if old_md5.get(key) != new_md5[key]:
            tar.add(key)
    tar.close()

#######################################################################
# 主程序
if __name__ == '__main__':
    # cp -r /etc/security  /tmp
    # os.makedirs('/tmp/backup')# mkdir  /tmp/backup
    src_dir = '/tmp/security/'    # /tmp/security/原路径，
    dst_dir = '/tmp/backup'       # /tmp/security/目标路径
    md5file = '/tmp/backup/md5.data'
    if strftime('%a') == 'Thu':
        full_backup(src_dir,dst_dir,md5file)
    else:
        incr_backup(src_dir,dst_dir,md5file)

