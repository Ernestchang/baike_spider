class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        file = open('output.html', 'w', encoding='utf-8')

        file.write('<html>')
        file.write('<body>')
        file.write('<table>')

        i = 1
        for data in self.datas:
            file.write('<tr>')
            file.write('<td>%d</td>' % i)
            i += 1
            file.write('<td>%s</td>' % data['title'])
            file.write('<td>%s</td>' % data['url'])
            file.write('<td>%s</td>' % data['summary'])
            file.write('</tr>')

        file.write('</table>')
        file.write('</body>')
        file.write('</html>')

        file.close()