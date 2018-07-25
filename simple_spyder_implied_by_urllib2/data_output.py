#!/usr/bin/python
# -*- coding:UTF-8 -*-

class DataOutput(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        with open('output.html','w') as f:
            f.write('<html>')
            f.write('<head>')
            f.write("<meta charset = 'utf-8'>")
            f.write('</head>')

            f.write('<body>')
            f.write('<table>')

            f.write('<th>')
            f.write('<td>url</td><td>title</td><td>digest</td>')
            f.write('</th>')
            for data in self.datas:
                f.write('<tr>')
                f.write('<td>')
                f.write(data['url'])
                f.write('</td>')
                f.write('<td>')
                f.write(data['title'].encode('utf8'))
                f.write('</td>')
                f.write('<td>')
                f.write(data['digest'].encode('utf8'))
                f.write('</td>')
                f.write('</tr>')
            f.write('</table>')
            f.write('</body>')
            f.write('</html>')

