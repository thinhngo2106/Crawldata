import scrapy


class ZingNewsSpider(scrapy.Spider):
    name = "zingnews"
    links_list =[]
    dem = 0
    start_urls = ['https://zingnews.vn/']

    id = 1115947

    def parse(self, response):
        if response.status == 200 and response.css('meta[property="og:url"]::attr("content")').get() != '' and response.css('meta[http-equiv="REFRESH"]::attr("content")').get() is not None:

            f = open('C:/Users/Thinh/PycharmProjects/untitled1/tutorial/tutorial/spiders/output/output.txt','a+',  encoding='utf-8')
            print(ZingNewsSpider.dem)
            url = response.url
            f.write(url + '\n')
            topic = response.css('p.the-article-category a::text').get()
            f.write("Chủ đề: " + topic.strip() + '\n')
            content = '\n'.join([
                    ''.join(c.css('*::text').getall())
                        for c in response.css('div.the-article-body p')
                ])
            f.write(content + '\n')
            title = response.css("h1.the-article-title::text").get()
            f.write("Tiêu đề: " + title.strip() + '\n')
            summary = response.css('p.the-article-summary::text').get()
            f.write("Tóm tắt: " + summary.strip() + '\n')
            date = response.css('li.the-article-publish::text').get()
            f.write("Thòi gian: " + date.strip() + '\n')


        link = 'https://zingnews.vn/zingnews-post' + str(ZingNewsSpider.id) + '.html'
        if ZingNewsSpider.id > 0:
            yield response.follow(link, callback=self.parse,dont_filter=True)
            ZingNewsSpider.id -= 1
            ZingNewsSpider.dem += 1

