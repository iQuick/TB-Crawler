# TB-Crawler

淘宝联盟数据抓取，自动登录淘宝联盟并抓去商品信息。智能的为每一个抓取到的商品打上标签，进行分类整理。

## 使用

### Help
```bash
The output  configuration file contents.

Usage: run.py [-d|--debug] [-h|--help] [-v|--version] [output, =[argument]]

Description
            -d,--debug      debug mode.
            -h,--help       help doc.
            -v,--version    software version.
for example:
    python run.py -d
```

### Example
`python run.py`

## 文件
```bash

|--- api      # 后台接口
|--- run      # 主程序
|--- tb_api   # 淘宝抓取接口
|--- tb_login # 淘宝自动登录

```


## 配置
配置文件 `config.py`
```py
_DEBUG = False          # 调试
_VERSION = 'v0.8.0'     # 版本信息
_USERNAME = 'xxxx'      # 淘宝帐号用户名
_PASSWORD = 'xxxx'      # 淘宝帐号密码
```

## libs
* [jieba]()

## 相关文章
* [简书-抓取淘宝联盟优惠券](https://www.jianshu.com/p/d2545ab42ab2)
* [简书-淘宝联盟自动登录](https://www.jianshu.com/p/5b11cbdde038)