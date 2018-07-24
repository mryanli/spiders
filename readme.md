# 网络爬虫



### 什么是网络爬虫

    网络爬虫，是一段程序。该程序将网页内容（html）文件下载下来，从网页中提取有价值的数据，存储起来。

###爬虫主要的结构

 1. 列表项爬虫调度模块
 2. url管理模块
 3. 网页下载模块
 4. 网页解析模块

我们的浏览器也可以理解为是一个大型的功能单一的爬虫。他通过网址，将网址所对应的网页爬取下来，并将该网页存储在内存中，通过浏览器窗口渲染出来，呈现给我们的就是网页内容。

当点击页面的超链接时，浏览器就会去‘爬取’对应的网页，并呈现给用户。用户实现了手动调度url模块。网页下载和网页解析则由浏览器完成。


 1. url的管理
    `内存`、`关系数据库`、`缓存数据库`都可以用来保存要爬取的列表，在大型互联网公司一般都用缓存数据库，因为快。

 2. 网页下载
     `urllib2`、`requests` 两个库都可以，前者是python自带，下面代码以urllib2为例：
    ```python
    import urllib2
    #第一种
    url = 'http://www.baidu.com'
    response1 = urllib2.urlopen(url)
    #第二种
    request = urllib2.Request(url)
    request.add_header('user-agent','Mozilla/5.0')
    response2 = urllib2.urlopen(request)
    #第三种方法
    import cookielib
    cj = cookielib.cookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProceesor(cj))
    urllib2.install_opener(opener)
    response3 = urllib2.urlopen(url)
    code3 = response3.getcode()     #状态码
    content3 = response3.read()
    ```
 3. 网页解析
    `正则表达式` `BeatifulSoup` `html.parser` `lxml`,都可以用来解析网页。前者是以字符串匹配方式解析网页，后三者是以DOM树为基础，进行结构化解析，比较推荐 [BeatifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html)

    **bs(beatifulsoup)使用方法：**
针对
`<a href='123.html' class='article'>Python</a>`
>1.创建bs对象
>2.搜索节点（find_all,find）
>3.获取节点的内容、属性

    ```python
    import bs4

    html_doc = "<a href='123.html' class='article'>Python</a>"
    #1,创建文档对象
    soup = bs4.BeautifulSoup(
        html_doc,                       #html文档字符
        'html.parser',                  #html解析器
        from_encoding='utf8'            #html文档的编码
    )
    #2.搜索节点  find_all(name[,attrs][,string]) ,其中attrs可以等于一个正则表达式对象，查找单个节点find(name[,attrs][,string])
    nodes1 = doc.find_all('a',class_='',string = '')  #注意class加下划线是为了避免和python关键字冲突
    nodes2 = doc.find_all('a',href='',string = '')

    node = doc.find('a')

    #3.访问节点信息
    node.name

    node['href']

    node.get_text()

    ```

##爬虫开发的一般步骤
 1. 确定目标
 百度百科***爬虫*** 词条的相关1000个词条的 *标题*  和 *简介*
 2. 分析目标网页的结构格式
入口页、url格式、数据格式、字符编码（utf8）
 3. 编写代码
 4. 执行爬虫
