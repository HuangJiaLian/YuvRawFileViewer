@echo off

set exePATH=.
set yuvPath=.
set width=1000
set height=800
set filename=out.yuv 

%exePATH%\yuvViewer.exe %yuvPath%\%filename% %width% %height% YUV420P


