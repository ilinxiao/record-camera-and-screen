import re


devices_txt = r'''
ffmpeg version N-90553-gbe502ec6cd Copyright (c) 2000-2018 the FFmpeg developers
  built with gcc 7.3.0 (GCC)
  configuration: --disable-static --enable-shared --enable-gpl --enable-version3 --enable-sdl2 --enable-bzlib --enable-fontconfig --enable-gnutls --enable-iconv --enable-libass --enable-libbluray --enable-libfreetype --enable-libmp3lame --enable-libopencore-amrnb --enable-libopencore-amrwb --enable-libopenjpeg --enable-libopus --enable-libshine --enable-libsnappy --enable-libsoxr --enable-libtheora --enable-libtwolame --enable-libvpx --enable-libwavpack --enable-libwebp --enable-libx264 --enable-libx265 --enable-libxml2 --enable-libzimg --enable-lzma --enable-zlib --enable-gmp --enable-libvidstab --enable-libvorbis --enable-libvo-amrwbenc --enable-libmysofa --enable-libspeex --enable-libxvid --enable-libaom --enable-libmfx --enable-amf --enable-ffnvcodec --enable-cuvid --enable-d3d11va --enable-nvenc --enable-nvdec --enable-dxva2 --enable-avisynth
  libavutil      56. 12.100 / 56. 12.100
  libavcodec     58. 16.100 / 58. 16.100
  libavformat    58. 10.100 / 58. 10.100
  libavdevice    58.  2.100 / 58.  2.100
  libavfilter     7. 13.100 /  7. 13.100
  libswscale      5.  0.102 /  5.  0.102
  libswresample   3.  0.101 /  3.  0.101
  libpostproc    55.  0.100 / 55.  0.100
[dshow @ 00000166634ef000] DirectShow video devices (some may be both video and audio devices)
[dshow @ 00000166634ef000]  "USB2.0 HD UVC WebCam"
[dshow @ 00000166634ef000]     Alternative name "@device_pnp_\\?\usb#vid_04f2&pid_b354&mi_00#7&30d7ad30&0&0000#{65e8773d-8f56-11d0-a3b9-00a0c9223196}\global"
[dshow @ 00000166634ef000]  "screen-capture-recorder"
[dshow @ 00000166634ef000]     Alternative name "@device_sw_{860BB310-5D01-11D0-BD3B-00A0C911CE86}\{4EA69364-2C8A-4AE6-A561-56E4B5044439}"
[dshow @ 00000166634ef000] DirectShow audio devices
[dshow @ 00000166634ef000]  "楹﹀厠椋?(Realtek High Definition Audio)"[dshow @ 00000166634ef000]     Alternative name "@device_cm_{33D9A762-90C8-11D0-BD43-00A0C911CE86}\wave_{571529B3-7DB3-42A3-ADEF-BBD82925C15D}"
[dshow @ 00000166634ef000]  "virtual-audio-capturer"
[dshow @ 00000166634ef000]     Alternative name "@device_sw_{33D9A762-90C8-11D0-BD43-00A0C911CE86}\{8E146464-DB61-4309-AFA1-3578E927E935}"
dummy: Immediate exit requested
'''

def get_device_info(text_list):
    device_list = []
    if text_list and len(text_list) % 2 == 0:
        i=0
        while i < len(text_list):
            step = 2 
            device = {}
            device_name = text_list[i].strip()
            device['Name'] = device_name.replace('"','')
            alternative_name_text = text_list[i+1]
            alter_re = re.search(r'"(.+)"',alternative_name_text)
            if alter_re:
                device_alternative_name = alter_re.group(1)
                device['Alternative'] = device_alternative_name
            device_list.append(device)
            i+=step
    return device_list
    
    
device_line = []
# print(dir(re))
results = re.findall(r'\[[^\]]+\]([^\[]+)',devices_txt)
# results.pop(0)
video_devices_spos=-1
voice_devices_spos=-1
for i in range(len(results)):
    txt = results[i]
    print(txt.strip())
    if txt.find('DirectShow video devices') >= 0:
        video_devices_spos = i
    if txt.find('DirectShow audio devices') >=0:
        voice_devices_spos = i  

video_devices = get_device_info(results[video_devices_spos+1:voice_devices_spos])     
voice_devices = get_device_info(results[voice_devices_spos+1:])   

print('视频设备列表:')
print(video_devices)
print('音频设备列表:')
print(voice_devices)

