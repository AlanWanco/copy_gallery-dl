import json, os, subprocess, sys, chardet, win32clipboard
from ctypes import *
from plyer import notification

urls = sys.argv[1:]
dl_list = ['gallery-dl']
path = os.path.dirname(os.path.abspath(__file__))
os.chdir(path) 

class DROPFILES(Structure):
    _fields_ = [
        ("pFiles", c_uint),
        ("x", c_long),
        ("y", c_long),
        ("fNC", c_int),
        ("fWide", c_bool),
    ]

def setClipboardFiles(paths):
  files = "\0".join(paths).encode('utf-16le')
  
  pDropFiles = DROPFILES()
  pDropFiles.pFiles = sizeof(pDropFiles)
  pDropFiles.fWide = True
  
  data = bytes(pDropFiles) + files + b"\0\0"
  paths_str = str(paths)
  try:
        if len(paths) > 0 and len(paths_str) > 3:
            win32clipboard.OpenClipboard()
            win32clipboard.EmptyClipboard()
            win32clipboard.SetClipboardData(win32clipboard.CF_HDROP, data)
            win32clipboard.CloseClipboard()
            print('Files copied!')
        else:
            print('请输入正确的地址.')
  except Exception as e:
        print('复制过程中发生错误:', str(e))

def readClipboardFilePaths():
    win32clipboard.OpenClipboard()
    try:
        return win32clipboard.GetClipboardData(win32clipboard.CF_HDROP)
    finally:
        win32clipboard.CloseClipboard()

def load_config():
    try:
        with open('config.json', 'r', encoding='utf-8') as f:
            config = json.load(f)
            if not config:
                gallery_path = ['gallery-dl']
            else:
                gallery_path = config.get('gallery_path', '')
                if not isinstance(gallery_path, list):
                    gallery_path = [gallery_path]
    except (FileNotFoundError, json.JSONDecodeError):
        gallery_path = ['gallery-dl']  

    return gallery_path

if os.path.exists('config.json'):
    dl_list = load_config()

if os.path.exists('gallery-dl.exe'):
    dl_list = [f'{path}/gallery-dl.exe']

dl_list = dl_list + urls
process = subprocess.Popen(dl_list, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=path)
stdout, stderr = process.communicate()

if stdout:
    detected_encoding = chardet.detect(stdout)['encoding']
    output_list = stdout.decode(detected_encoding).split('\r\n')
    output_list = [s.lstrip('# ') for s in output_list]
    output_list = [x for x in output_list if x]

    for line in output_list:
        print(line)

    setClipboardFiles(output_list)
    readClipboardFilePaths()
    notification.notify(title='复制程序', message='图片下载完成')

if stderr:
    detected_encoding = chardet.detect(stderr)['encoding']
    output_list = stderr.decode(detected_encoding).split('\r\n')
    output_list = [x for x in output_list if x]

    for line in output_list:
        print(line)

    notification.notify(title='复制程序', message='图片下载失败！')



