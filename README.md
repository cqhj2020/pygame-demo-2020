# pygame-demo-2020
a python pygame demo collection

<h3>1、pygame常用模块</h3>

<table><thead><tr><th align="left">模块名</th><th align="left">功能</th></tr></thead><tbody><tr><td align="left">pygame.cdrom</td><td align="left">访问光驱</td></tr><tr><td align="left">pygame.cursors</td><td align="left">加载光标</td></tr><tr><td align="left">pygame.display</td><td align="left">访问显示设备</td></tr><tr><td align="left">pygame.draw</td><td align="left">绘制形状、线和点</td></tr><tr><td align="left">pygame.event</td><td align="left">管理事件</td></tr><tr><td align="left">pygame.font</td><td align="left">使用字体</td></tr><tr><td align="left">pygame.image</td><td align="left">加载和存储图片</td></tr><tr><td align="left">pygame.joystick</td><td align="left">使用游戏手柄或者类似的东西</td></tr><tr><td align="left">pygame.key</td><td align="left">读取键盘按键</td></tr><tr><td align="left">pygame.mixer</td><td align="left">声音</td></tr><tr><td align="left">pygame.mouse</td><td align="left">鼠标</td></tr><tr><td align="left">pygame.movie</td><td align="left">播放视频</td></tr><tr><td align="left">pygame.music</td><td align="left">播放音频</td></tr><tr><td align="left">pygame.overlay</td><td align="left">访问高级视频叠加</td></tr><tr><td align="left">pygame.rect</td><td align="left">管理矩形区域</td></tr><tr><td align="left">pygame.scrap</td><td align="left">本地剪贴板访问</td></tr><tr><td align="left">pygame.sndarray</td><td align="left">操作声音数据</td></tr><tr><td align="left">pygame.sprite</td><td align="left">操作移动图像</td></tr><tr><td align="left">pygame.surface</td><td align="left">管理图像和屏幕</td></tr><tr><td align="left">pygame.surfarray</td><td align="left">管理点阵图像数据</td></tr><tr><td align="left">pygame.time</td><td align="left">管理时间和帧信息</td></tr><tr><td align="left">pygame.transform</td><td align="left">缩放和移动图像</td></tr></tbody></table>

<h3>2、pygame.display.set_mode</h3>

<p><strong>set_mode</strong>会返回一个Surface对象，代表了在桌面上出现的那个窗口，三个参数第一个为元祖，代表分辨率（必须）；第二个是一个标志位，具体意思见下表，如果不用什么特性，就指定0；第三个为色深。</p>
<table>
<thead>
<tr>
<th>标志位</th>
<th>功能</th>
</tr>
</thead>
<tbody>
<tr>
<td>FULLSCREEN</td>
<td>创建一个全屏窗口</td>
</tr>
<tr>
<td>DOUBLEBUF</td>
<td>创建一个“双缓冲”窗口，建议在HWSURFACE或者OPENGL时使用</td>
</tr>
<tr>
<td>HWSURFACE</td>
<td>创建一个硬件加速的窗口，必须和FULLSCREEN同时使用</td>
</tr>
<tr>
<td>OPENGL</td>
<td>创建一个OPENGL渲染的窗口</td>
</tr>
<tr>
<td>RESIZABLE</td>
<td>创建一个可以改变大小的窗口</td>
</tr>
<tr>
<td>NOFRAME</td>
<td>创建一个没有边框的窗口</td>
</tr>
</tbody>
</table>
<p><strong>convert</strong>函数是将图像数据都转化为Surface对象，每次加载完图像以后就应该做这件事件（事实上因为 它太常用了，如果你不写pygame也会帮你做）；<strong>convert_alpha</strong>相比convert，保留了Alpha 通道信息（可以简单理解为透明的部分），这样我们的光标才可以是不规则的形状。</p>

<h3>3、screen.blit</h3>

<strong>blit</strong>是个重要函数，第一个参数为一个Surface对象，第二个为左上角位置。画完以后一定记得用<strong>update</strong>更新一下，否则画面一片漆黑。