# one-hour-tenement
使用python查看在自己一小时路程之内的58出租屋信息
1. 使用python爬取自己想要查看城市的出租房屋信息，运行crawl.py文件，即可爬取信息，信息保存在rent.csv文件。
 ![image](https://github.com/ButBueatiful/dotvim/raw/master/screenshots/vim-screenshot.jpg)
2. 在python运行index.html页面。
  使用python -m http.server = 3000  命令来启动一个服务器。然后访问 http://127.0.0.1:3000
 ![image](https://github.com/ButBueatiful/dotvim/raw/master/screenshots/vim-screenshot.jpg)
3. 首先输入自己的工作地点，会规划出一小时之内能够到达的地方。然后导入第一步爬取的csv文件，即可查看。
 ![image](https://github.com/ButBueatiful/dotvim/raw/master/screenshots/vim-screenshot.jpg)
4. 点击标出的房屋信息，可以查看线路规划，点击租房名称，可以调到该房屋出租信息链接
 ![image](https://github.com/ButBueatiful/dotvim/raw/master/screenshots/vim-screenshot.jpg)
