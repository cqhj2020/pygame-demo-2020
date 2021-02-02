# pygame-demo-2020
a python pygame demo collection

1、pygame.display.set_mode

<p><strong>set_mode</strong>会返回一个Surface对象，代表了在桌面上出现的那个窗口，三个参数第一个为元祖，代表分 辨率（必须）；第二个是一个标志位，具体意思见下表，如果不用什么特性，就指定0；第三个为色深。</p>
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
