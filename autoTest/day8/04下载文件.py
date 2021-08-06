import requests

url = 'https://img1.bitautoimg.com/bitauto/2013/01/23/854be0a2-ef1c-440a-926d-94e1e5051e18.jpg'

resp = requests.get(url)
with open('bmw.jpg', 'wb') as f:  # wb： write in bytes
    f.write(resp.content)  # resp.content 返回值是 bytes

# 思考： 如果下载的是一个4G的电影，该怎么办？
# 方案： 流式下载

def downloader(url,filename,size=1024*4):
    """
    下载大文件
    :param url: 下载地址
    :param filename: 保存的文件名
    :param size: 分块下载的大小，默认值是4KB
    :return: None
    """
    with requests.get(url,stream=True) as req:
        with open(filename,'wb') as f:
            for chunk in req.iter_content(chunk_size=size):
                # 如果没有下完，就继续下载
                if chunk:
                    f.write(chunk)


if __name__ == '__main__':
    downloader(url='https://img1.baidu.com/it/u=112214144,1044341636&fm=11&fmt=auto&gp=0.jpg',filename='2.jpg')
