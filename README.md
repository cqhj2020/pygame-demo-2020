# pygame-demo-2020
a python pygame demo collection

<h3>1��pygame.display.set_mode</h3>

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

<h3>2��screen.blit</h3>

<strong>blit</strong>�Ǹ���Ҫ��������һ������Ϊһ��Surface���󣬵ڶ���Ϊ���Ͻ�λ�á������Ժ�һ���ǵ���<strong>update</strong>����һ�£�������һƬ��ڡ�