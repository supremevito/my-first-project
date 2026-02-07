import re


def get_douyin_url(text):
    """简单提取抖音分享链接"""
    # 匹配抖音分享链接
    pattern = r'https?://(?:v\.)?douyin\.com/[\w/]+'

    # 查找匹配
    match = re.search(pattern, text)

    if match:
        return match.group(0)
    return None


# 使用示例
text = "9.99 r@R.xS nda:/ 08/31 24小时火车前往印度第一大城市孟买，这里真的能比肩上海？离谱 来到孟买感觉像出国了，比印度其他城市好太多了，小资生活杠杠滴！# 印度 # 孟买 # 交换世界计划 # 青年创作者成长计划 # 环球旅行  https://v.douyin.com/MQihkD90VEk/ 复制此链接，打开Dou音搜索，直接观看视频！！"

url = get_douyin_url(text)
if url:
    print(f"提取的抖音链接: {url}")
else:
    print("未找到抖音链接")