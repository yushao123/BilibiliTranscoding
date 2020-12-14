import json
import os
import danmaku2ass
import sys


ffmpeg = 'ffmpeg\\ffmpeg.exe'
fontsize = 50

def FindAllVideo(file_root):
    videolist = []
    for root, dirs, files in os.walk(file_root, topdown=False):
        for name in files:
            if name == 'entry.json':
                with open(os.path.join(root, name), 'r', encoding='utf-8') as f:
                    videoinfo = json.loads(f.read())
                    title = videoinfo['title'].replace(' ','').replace('\\','-').replace('/','-')
                videofile = root + r'\80\video.m4s'
                audiofile = root + r'\80\audio.m4s'
                danmufile = root + r'\danmaku.xml'
                if os.path.isfile(videofile) and os.path.isfile(audiofile):
                    onevideo = {'videofile': videofile, 'audiofile': audiofile, 'title': title,
                                'width': videoinfo['page_data']['width'], 'height': videoinfo['page_data']['height']}
                    if os.path.isfile(danmufile):
                        onevideo['danmu'] = danmufile
                videolist.append(onevideo)
    return videolist


def CodeVideo(videolist, outputdir, codetype='.mp4'):
    if outputdir[-1] != '\\':
        outputdir += '\\'
    if codetype[0] != '.':
        codetype = '.'+ codetype
    for onevideo in videolist:
        title = onevideo['title']
        # 处理弹幕
        if 'danmu' in onevideo:
            try:
                danmaku2ass.Danmaku2ASS(input_format='Bilibili',input_files=onevideo['danmu'], output_file=outputdir + title + '.ass',
                                        stage_width=onevideo['width'], stage_height=onevideo['height'],
                                        reserve_blank=480,
                                        font_size=fontsize, text_opacity=0.6, duration_marquee=12.0, duration_still=6.0)
            except Exception as e:
                return '错误[弹幕转换失败]因为:\n' + str(e)
        # 处理视频
        # ffmpeg -i video2.avi -i audio.mp3 -vcodec copy -acodec copy output.avi
        cmd = r'.\"%s" -i "%s" -i "%s" -vcodec copy -acodec copy "%s"' % (
            ffmpeg, onevideo['videofile'], onevideo['audiofile'], outputdir + title + codetype)
        os.system(cmd)
        #res = os.popen(cmd)
        return '编码完成'

if __name__ == '__main__':
    CodeVideo(FindAllVideo(r'\\Desktop\\新建文件夹'), '\\Desktop\\新建文件夹\\75801774')
