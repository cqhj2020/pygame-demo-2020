# pygame-demo-2020
a python pygame demo collection

<h3>1��pygame����ģ��</h3>

<table><thead><tr><th align="left">ģ����</th><th align="left">����</th></tr></thead><tbody><tr><td align="left">pygame.cdrom</td><td align="left">���ʹ���</td></tr><tr><td align="left">pygame.cursors</td><td align="left">���ع��</td></tr><tr><td align="left">pygame.display</td><td align="left">������ʾ�豸</td></tr><tr><td align="left">pygame.draw</td><td align="left">������״���ߺ͵�</td></tr><tr><td align="left">pygame.event</td><td align="left">�����¼�</td></tr><tr><td align="left">pygame.font</td><td align="left">ʹ������</td></tr><tr><td align="left">pygame.image</td><td align="left">���غʹ洢ͼƬ</td></tr><tr><td align="left">pygame.joystick</td><td align="left">ʹ����Ϸ�ֱ��������ƵĶ���</td></tr><tr><td align="left">pygame.key</td><td align="left">��ȡ���̰���</td></tr><tr><td align="left">pygame.mixer</td><td align="left">����</td></tr><tr><td align="left">pygame.mouse</td><td align="left">���</td></tr><tr><td align="left">pygame.movie</td><td align="left">������Ƶ</td></tr><tr><td align="left">pygame.music</td><td align="left">������Ƶ</td></tr><tr><td align="left">pygame.overlay</td><td align="left">���ʸ߼���Ƶ����</td></tr><tr><td align="left">pygame.rect</td><td align="left">�����������</td></tr><tr><td align="left">pygame.scrap</td><td align="left">���ؼ��������</td></tr><tr><td align="left">pygame.sndarray</td><td align="left">������������</td></tr><tr><td align="left">pygame.sprite</td><td align="left">�����ƶ�ͼ��</td></tr><tr><td align="left">pygame.surface</td><td align="left">����ͼ�����Ļ</td></tr><tr><td align="left">pygame.surfarray</td><td align="left">�������ͼ������</td></tr><tr><td align="left">pygame.time</td><td align="left">����ʱ���֡��Ϣ</td></tr><tr><td align="left">pygame.transform</td><td align="left">���ź��ƶ�ͼ��</td></tr></tbody></table>

<h3>2��pygame.display.set_mode</h3>

<p><strong>set_mode</strong>�᷵��һ��Surface���󣬴������������ϳ��ֵ��Ǹ����ڣ�����������һ��ΪԪ�棬����ֱ��ʣ����룩���ڶ�����һ����־λ��������˼���±��������ʲô���ԣ���ָ��0��������Ϊɫ�</p>
<table>
<thead>
<tr>
<th>��־λ</th>
<th>����</th>
</tr>
</thead>
<tbody>
<tr>
<td>FULLSCREEN</td>
<td>����һ��ȫ������</td>
</tr>
<tr>
<td>DOUBLEBUF</td>
<td>����һ����˫���塱���ڣ�������HWSURFACE����OPENGLʱʹ��</td>
</tr>
<tr>
<td>HWSURFACE</td>
<td>����һ��Ӳ�����ٵĴ��ڣ������FULLSCREENͬʱʹ��</td>
</tr>
<tr>
<td>OPENGL</td>
<td>����һ��OPENGL��Ⱦ�Ĵ���</td>
</tr>
<tr>
<td>RESIZABLE</td>
<td>����һ�����Ըı��С�Ĵ���</td>
</tr>
<tr>
<td>NOFRAME</td>
<td>����һ��û�б߿�Ĵ���</td>
</tr>
</tbody>
</table>
<p><strong>convert</strong>�����ǽ�ͼ�����ݶ�ת��ΪSurface����ÿ�μ�����ͼ���Ժ��Ӧ��������¼�����ʵ����Ϊ ��̫�����ˣ�����㲻дpygameҲ�����������<strong>convert_alpha</strong>���convert��������Alpha ͨ����Ϣ�����Լ����Ϊ͸���Ĳ��֣����������ǵĹ��ſ����ǲ��������״��</p>

<h3>3��screen.blit</h3>

<strong>blit</strong>�Ǹ���Ҫ��������һ������Ϊһ��Surface���󣬵ڶ���Ϊ���Ͻ�λ�á������Ժ�һ���ǵ���<strong>update</strong>����һ�£�������һƬ��ڡ�