# coding=utf-8
import requests
import json
import re
from urllib.parse import unquote



cookie='ttwid=1|TEF980arSw1Py-04RUozSPrlObqFHN8icl1_zd6_7XI|1676889448|8b16d32ae94536a037c4a5dacba1c07f7e436f41f2e11bd9992e7c3174e66f52; passport_csrf_token=5a61d251879ce4cc32c523a208abd5f1; passport_csrf_token_default=5a61d251879ce4cc32c523a208abd5f1; s_v_web_id=verify_lfjq3ikx_bLu7UZZi_fKnD_4ODv_9T1B_WVLcC3LuerKE; ttcid=be5a2e53baae4d2e87ef80dd58d64e7213; n_mh=EFJOdGSkX4fI8Dz7lTGDAZSvqbdIpcjFdyLnD2821HY; sso_uid_tt=c5115e0ccbe6dde3fcad98c44e32909d; sso_uid_tt_ss=c5115e0ccbe6dde3fcad98c44e32909d; toutiao_sso_user=737eb353c659d1d5d85a494dfe12eaf9; toutiao_sso_user_ss=737eb353c659d1d5d85a494dfe12eaf9; passport_auth_status=480aea08b1b61561f2a1a295c26e62aa,; passport_auth_status_ss=480aea08b1b61561f2a1a295c26e62aa,; uid_tt=da8cd6273e67281f12dde41daae14685; uid_tt_ss=da8cd6273e67281f12dde41daae14685; sid_tt=fb752205f85dcda6db48d122e124f35f; sessionid=fb752205f85dcda6db48d122e124f35f; sessionid_ss=fb752205f85dcda6db48d122e124f35f; odin_tt=99dead142ad82eaf9945dd8414519fa3b389822d1e19e99a33434e3cfa15f4a761a63668925a2e74496b9de7b83a43ebe7a43e52aabb1303e92cd63160bfdf48; passport_assist_user=Cj2TQi3R0OXqkR9Xb1uUQK7qLbJHyKlGsCnVHfp4NmoUdthJ4a3TlnWLQb3fsORLGyOUJAX7GvhOUt0s-N5RGkgKPBSKjFvKDc6Nfn1lQ936-CokTBtvbdscXIya-ji4v52wz88xzcwLoOPWBXBh4BtldGLxI_wy65wkLjxJgRD6uawNGImv1lQiAQMy8BAt; sid_ucp_sso_v1=1.0.0-KGQxYjYyMzk1MmNmZDhlNmZiNjBiMmNiZTAwZWI2OWI0N2Y0YTBlODkKHQjYt-_p_QIQpIfsoAYY7zEgDDCW5pbbBTgGQPQHGgJscSIgNzM3ZWIzNTNjNjU5ZDFkNWQ4NWE0OTRkZmUxMmVhZjk; ssid_ucp_sso_v1=1.0.0-KGQxYjYyMzk1MmNmZDhlNmZiNjBiMmNiZTAwZWI2OWI0N2Y0YTBlODkKHQjYt-_p_QIQpIfsoAYY7zEgDDCW5pbbBTgGQPQHGgJscSIgNzM3ZWIzNTNjNjU5ZDFkNWQ4NWE0OTRkZmUxMmVhZjk; _tea_utm_cache_2018=undefined; LOGIN_STATUS=1; store-region=cn-ah; store-region-src=uid; sid_guard=fb752205f85dcda6db48d122e124f35f|1679492020|5183983|Sun,+21-May-2023+13:33:23+GMT; sid_ucp_v1=1.0.0-KDlhY2M4YzU4NjE1N2VhNDk3ODE2MzUyMzhlMWNkMWUwYWM2M2QwMjgKGQjYt-_p_QIQtIfsoAYY7zEgDDgGQPQHSAQaAmxmIiBmYjc1MjIwNWY4NWRjZGE2ZGI0OGQxMjJlMTI0ZjM1Zg; ssid_ucp_v1=1.0.0-KDlhY2M4YzU4NjE1N2VhNDk3ODE2MzUyMzhlMWNkMWUwYWM2M2QwMjgKGQjYt-_p_QIQtIfsoAYY7zEgDDgGQPQHSAQaAmxmIiBmYjc1MjIwNWY4NWRjZGE2ZGI0OGQxMjJlMTI0ZjM1Zg; SEARCH_RESULT_LIST_TYPE="single"; download_guide="3/20230322"; strategyABtestKey="1679632107.149"; FOLLOW_NUMBER_YELLOW_POINT_INFO="MS4wLjABAAAAF7wQCb471uHInlIu-oidHDY0hMZh78fsE8MvnhleykQ/1679673600000/0/1679632107590/0"; __ac_nonce=0641d3b2600feea11ec39; __ac_signature=_02B4Z6wo00f01lAfWvwAAIDDpWCwY-o2Fv5QP15AAPApXvLfTIwbbWuovReKqM7N9vFc7pn.CqTUzKcRk4u4QObn6nNjGtRilaWRyukG85YkWv-FDvLpnOPcZIu.245AB2Zj9OjlWWoOnEqA41; douyin.com; VIDEO_FILTER_MEMO_SELECT={"expireTime":1680242088899,"type":1}; csrf_session_id=e684c0385fe9b9677961379b94090942; FOLLOW_LIVE_POINT_INFO="MS4wLjABAAAAF7wQCb471uHInlIu-oidHDY0hMZh78fsE8MvnhleykQ/1679673600000/0/1679637289808/0"; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWNsaWVudC1jZXJ0IjoiLS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0tXG5NSUlDRkRDQ0FicWdBd0lCQWdJVU1oUklCam5mY2trTmErUnBGMDdCRkhGVlN5RXdDZ1lJS29aSXpqMEVBd0l3XG5NVEVMTUFrR0ExVUVCaE1DUTA0eElqQWdCZ05WQkFNTUdYUnBZMnRsZEY5bmRXRnlaRjlqWVY5bFkyUnpZVjh5XG5OVFl3SGhjTk1qTXdNekl5TVRNek16STBXaGNOTXpNd016SXlNakV6TXpJMFdqQW5NUXN3Q1FZRFZRUUdFd0pEXG5UakVZTUJZR0ExVUVBd3dQWW1SZmRHbGphMlYwWDJkMVlYSmtNRmt3RXdZSEtvWkl6ajBDQVFZSUtvWkl6ajBEXG5BUWNEUWdBRW56bTlyOU9XV0N1bDN1bUl6K01XZWUzRmN0K2VrWWpPM2UvdWdBamlQUHViQXIxOXlIVE90NUR0XG4wVVZCWGM1ZHpHNTRLVE5VN0xnQ3FwQ0pYQTNPcTZPQnVUQ0J0akFPQmdOVkhROEJBZjhFQkFNQ0JhQXdNUVlEXG5WUjBsQkNvd0tBWUlLd1lCQlFVSEF3RUdDQ3NHQVFVRkJ3TUNCZ2dyQmdFRkJRY0RBd1lJS3dZQkJRVUhBd1F3XG5LUVlEVlIwT0JDSUVJTUtnbXFTdGhudXJ2a2RiT2xleVhXWW5QaDlkUHNKT20wYktvMVRJSERVQk1Dc0dBMVVkXG5Jd1FrTUNLQUlES2xaK3FPWkVnU2pjeE9UVUI3Y3hTYlIyMVRlcVRSZ05kNWxKZDdJa2VETUJrR0ExVWRFUVFTXG5NQkNDRG5kM2R5NWtiM1Y1YVc0dVkyOXRNQW9HQ0NxR1NNNDlCQU1DQTBnQU1FVUNJUURUd3dpL0lUZ1ovb1phXG5EU2NzK0VhK1dkSW1FdzdFYmx0RFlhdTE5Wjg4WXdJZ0hKNHRhMFBKSzRSV2xHOERXbVFxbkFrUGJ2RjVIclZZXG5rTkxEWExyRUQwZz1cbi0tLS0tRU5EIENFUlRJRklDQVRFLS0tLS1cbiJ9; msToken=qcHdipfueA71yQ-vUF0VPZijGeMB1sC0A8VahVvHVeFIRux2Ll0Cq7iqgfdxrGQMXWqGhNfmCIcysmD3kd4ibue_KhkhyGs6YeX9FtkZ85uHl9L8lClv; publish_badge_show_info="0,0,0,1679637292742"; tt_scid=7uJ9LzDtmRGk6F3975reBHkPXnWQ.aHqjvc1CP3Jmhq3nm7a-tdWTGJvclQCZpGlabc4; passport_fe_beating_status=false; msToken=1eHuRX8SGkHFZQhq0N-su_p1-80oq-FrRh8ZGV6z7G45jCUVrCv23jXxcsgK6cLUCNrAK8dwkGJSKZL27yg9pgs6LoiL-g21ilSgQfgtwlMpGfIpVnPm; home_can_add_dy_2_desktop="0"'




def huoqu(url,type):
    if type=='视频':
        url = 'https://www.douyin.com/' + url + '?previous_page=app_code_link'
        #print(url)
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'referer': 'https://www.douyin.com/' + url+'?previous_page=app_code_link',
            'cookie': cookie
            }
        response = requests.get(url, headers=headers)
        response = response.text
        response = re.findall('type="application/json">(.*)</script><script nonce', response)[0]
        response = unquote(response)
        response = re.sub('</script>(.*)</script>(.*)', '', response)
        response = json.loads(response)
        print('video')
        print('https:'+response['44']["aweme"]["detail"]["video"]["playApi"])
        i = requests.head('https:'+response['44']["aweme"]["detail"]["video"]["playApi"])
        i = str(i.headers.get('location'))
        print('无水印视频链接：'+i)
    else:
        url = 'https://www.douyin.com/' + url + '?previous_page=app_code_link'
        #print(url)
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'referer': 'https://www.douyin.com/' + url+'?previous_page=app_code_link',
            'cookie': cookie
        }
        response = requests.get(url, headers=headers)
        response = response.text
        response = re.findall('type="application/json">(.*)</script><script nonce', response)[0]
        response = unquote(response)
        response = re.sub('</script>(.*)</script>(.*)', '', response)
        response = json.loads(response)
        print('picture')
        for i in response['29']["aweme"]["detail"]['imgBitrate'][0]['images']:
            print('无水印图片链接：'+i['urlList'][0])


def main():
    url=input('输入url:')
    url = requests.head(url)
    url = str(url.headers.get('location'))
    #print(url)
    if 'note' in url:
        url = re.findall(r'https://www.iesdouyin.com/share/(.*)/?region=', url)[0]
        len_n=len(url)-2
        url=url[0:len_n]
        type_1='图文'
    elif 'video' in url:
        print('video')
        url = re.findall('https://www.iesdouyin.com/share/(.*)/?region=', url)[0]
        len_n=len(url)-2
        url=url[0:len_n]
        type_1='视频'
    huoqu(url,type_1)


def main_handler(event, context):
    return main()


if __name__ == '__main__':
    main()
