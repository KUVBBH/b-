import os 
import glob
import time
import shutil
import subprocess
from tqdm import tqdm

def ffmpeg_run (video_path,audio_path,out_path,up_path,title):
    try :
        ffmpeg='ffmpeg -i "'+video_path+'" -i "'+audio_path+'" -vcodec copy -acodec copy "'+out_path+repr(title)+str(time.time())+'.mp4"'
        #print(ffmpeg)
        subprocess.getoutput(ffmpeg)
    except :
        pass
    else :
        shutil.rmtree(up_path)
        
        
if __name__ == '__main__' :
    path_list=[]
    ffmpeg_list=[]
    sss=False
    while sss == False :
        input_str=input('''
\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n
*请输入需要合并视频的文件夹 (就是b站视频
 缓存文件夹路径)和导出文件夹中间用 - 隔开

*如果保存在默认文件夹,请先复制或者剪切出来
 默认路径为:
 /storage/emulated/0/Android/data/tv.danmaku.bili/download

*如果无法找到文件,请使用ES文件浏览器

*输入路径为绝对路径

*例如 :

/storage/emulated/0/blibli/-/storage/emulated/0/ok

>>>请输入:''').split('-')
        if len(input_str) == 2 and os.path.isdir(input_str[0].replace(' ','')) and os.path.isdir(input_str[1].replace(' ','')) :
            sss=True
        else :
            print('输入错误!请重新输入')
            time.sleep(1)
    in_path=input_str[0]
    out_path=input_str[1]
    if in_path[-1:] != '/' :
        in_path+='/'
    if out_path[-1:] != '/' :
        out_path+='/'      
    #print(in_path,out_path)
    sss=False
    while sss==False :
        a=glob.iglob(in_path,recursive=False)
        for i in a :
            if 'entry.json' in i:
                #print(i)
                path_list.append(i)
                sss=True
        in_path=in_path[0:-1]+'/**'
    print(len(path_list))
    for p in path_list :
        #print(p)
        up_path=p.replace('entry.json','')
        with open (p,'r') as f :
            a=f.read().replace('{','').replace('}','').replace('"','').split(',')
        for i in a :
            if 'prefered_video_quality' in i:
                prefered_video_quality=i.split(':')[1]
            elif 'title' in i :
                title=i.split(':')[1]
        video_path=up_path+prefered_video_quality+'/video.m4s'
        audio_path=up_path+prefered_video_quality+'/audio.m4s'
        #print(video_path)
        #print(audio_path)
        #print(title)
        ffmpeg_list.append((video_path,audio_path,out_path,up_path,title))
    #print(len(ffmpeg_list))
    for i in tqdm(ffmpeg_list) :
        ffmpeg_run(i[0],i[1],i[2],i[3],i[4])
    print('----------全部完成----------')
    
        




