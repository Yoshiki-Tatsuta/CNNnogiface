from icrawler.builtin import BingImageCrawler


keyword = input("検索したいこと入力：")
pic_num = input("取得枚数の指定：")


crawler = BingImageCrawler(storage = {"root_dir" : "./image"})
crawler.crawl(keyword = keyword, max_num = int(pic_num))
