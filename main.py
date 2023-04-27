# coding=utf-8
import requests
import json
import re
from urllib.parse import unquote


#你的cookie
cookie=''




def huoqu(url,type):
    if type=='视频':
        #print(url)
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'referer': url,
            'cookie': cookie
            }
        response = requests.get(url, headers=headers)
        response = response.text
        response = re.findall('type="application/json">(.*)</script><script nonce', response)[0]
        response = unquote(response)
        response = re.sub('</script>(.*)</script>(.*)', '', response)
        response = json.loads(response)
        print('video')
        print(response)
        s=0
        for i in response:
            if s==1:
                response=response[i]
                break
            else:
                s+=1
        print('https:'+response["aweme"]["detail"]["video"]["playApi"])
        i = requests.head('https:'+response["aweme"]["detail"]["video"]["playApi"])
        print(i)
        i = str(i.headers.get('location'))
        print('无水印视频链接：'+i)
    else:

        print(url)
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'cookie': cookie
        }
        response = requests.get(url, headers=headers)
        response = response.text
        response = re.findall('type="application/json">(.*)</script><script nonce', response)[0]
        response = unquote(response)
        response = re.sub('</script>(.*)</script>(.*)', '', response)
        response = json.loads(response)
        print('picture')
        s=0
        for i in response:
            if s==1:
                response=response[i]
                break
            else:
                s+=1
        for i in response["aweme"]["detail"]['images']:
            s = i['urlList'][3]
            print(s)


def main():
    url=input('输入url')
    url = requests.head(url)
    url = str(url.headers.get('location'))
    headers={
        'cookie':cookie
    }
    url = requests.head(url,headers=headers).headers['Location']
    print(url)
    if 'note' in url:
        type_1='图文'
        print(url)
        print(type_1)
        #print(huoqu(url, '视频'))
    elif 'video' in url:
        type_1='视频'
    #print(url)

    huoqu(url,type_1)

def main_handler(event, context):
    return main()


if __name__ == '__main__':
    main()

