import requests
import json
import xlwt
comment_list = []
sex_list = []
like_list = []
level_list = []
name_list = []
# 需要爬取的url
original_url = "https://api.bilibili.com/x/v2/reply/main?jsonp&next=0&type=1&oid=642854841&mode=3&plat=1&_=1669639731136"
# 设置请求头和Cookie

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
    , 'referer': 'https://www.bilibili.com/festival/bilibili13?bvid=BV1KY4y1n77'
    ,
    'cookie': "buvid3=F07F1E1B-5EEE-E54D-B498-9B92BDE6D1E753904infoc; b_nut=1663991553; i-wanna-go-back=-1; _uuid=EDB622105-1FC6-610E9-8914-3A1010E9878C6B54296infoc; nostalgia_conf=-1; buvid_fp_plain=undefined; SESSDATA=2915eb72,1679543806,304d0*91; bili_jct=dbd18d4a0460a46005e96a08cada2e5c; DedeUserID=660966543; DedeUserID__ckMd5=91c1d29b2dc8c370; sid=651fpcm3; b_ut=5; CURRENT_FNVAL=4048; LIVE_BUVID=AUTO5116683497977973; buvid4=0A9D2A8C-75B4-C8FA-1A71-EB20C4ED613554970-022092411-aL0NYo+hLDuvgN8ta2SdHw==; bp_video_offset_660966543=709067481192333300; rpdid=|(JJmYYlkJll0J'uYY)l)YuJ); fingerprint=bae2fe680cb96b3206b450097aa5f454; buvid_fp=5e7fca8b456b42e0579c069bf2673b7e; bsource=search_bing; PVID=1; CURRENT_QUALITY=0; b_lsid=10102AE68F_184BE24FB01; innersign=0"

}

# 使用for循环爬取实现翻页爬取

for page in range(1, 150):
    url = 'https://api.bilibili.com/x/v2/reply/main?jsonp=jsonp&next={}&type=1&oid=642854841&mode=3&plat=1&_=1669639731136'.format(
        page)

    response = requests.get(url=url, headers=headers).text
    response = response.replace("jQuery33105637377098399248_1669639731135(", "")  # 要先用replace把这些删掉才能爬到
    response = response.replace(")", "")

    # 用json.loads加载response数据
    re_data = json.loads(response)

    # 由于有一些是空评论，因此对数据进行判断，如果不等于空值则返回
    if re_data['data']['replies'] != None:
        for i in re_data["data"]['replies']:
            comment = i["content"]['message']
            name = i["member"]['uname']
            like = i["like"]
            level = i['member']['level_info']['current_level']
            sex = i["member"]['sex']

            # 将爬取到的数据输入列表中
            comment_list.append(comment)
            sex_list.append(sex)
            like_list.append(like)
            level_list.append(level)
            name_list.append(name)

workbook = xlwt.Workbook(encoding = 'utf-8')        #设置一个workbook，其编码是utf-8
worksheet = workbook.add_sheet("test_sheet")

worksheet.write(0,0,label='名字')
worksheet.write(0,1,label='性别')
worksheet.write(0,2,label='等级')
worksheet.write(0,3,label='评论内容')
worksheet.write(0,4,label='点赞数')
for i in range(len(name_list)):
    worksheet.write(i+1,0,label=name_list[i])
    worksheet.write(i+1,1,label=sex_list[i])
    worksheet.write(i+1,2,label=level_list[i])
    worksheet.write(i+1,3,label=comment_list[i])
    worksheet.write(i+1,4,label=like_list[i])
workbook.save(r"评论信息.xls")