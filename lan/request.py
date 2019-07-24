import requests


def _request(api='', method="get", data={}, headers={}, stream=True):
    timeout = 5
    can_request = False
    r_data = {
        'status_code': 0,
        'status': 'error',
        'response': {},
        'time': 0,  # 时间
        'msg': ''  # 错误提示
    }

    try:
        if method == 'get':
            r = requests.get(api, params=data, headers=headers, stream=stream, timeout=timeout)
            can_request = True
        elif method == 'post':
            r = requests.post(api, data=data, headers=headers, stream=stream, timeout=timeout)
            can_request = True
        elif method == 'put':
            r = requests.put(api, data=data, headers=headers, stream=stream, timeout=timeout)
            can_request = True
        elif method == 'delete':
            r = requests.delete(api, headers=headers, stream=stream, timeout=timeout)
            can_request = True
        else:
            r_data['msg'] = '没有找到'
    except requests.ConnectTimeout:
        r_data['msg'] = '超时！'
    except requests.HTTPError:
        r_data['msg'] = 'http状态码非200'
    except Exception as e:
        r_data['msg'] = '打不开 或者 未进行容错处理的情况'

    if can_request is True:
        if r.status_code == 200:
            if r.headers.get('Content-Type') == 'text/html':
                # 获取html
                r_data['response'] = r.text.encode(r.encoding).decode()
            else:
                # 获取json
                r_data['response'] = r.json()

            r_data['status'] = 'success'
        else:
            r_data['status'] = 'error'
            r_data['msg'] = r.text

        r_data['time'] = r.elapsed.total_seconds()
        r_data['status_code'] = r.status_code

    return r_data


class Request:

    @staticmethod
    def get(api='', data={}, headers={}, stream=True):
        return _request(api, 'get', data, headers, stream)

    @staticmethod
    def post(api='', data={}, headers={}, stream=True):
        return _request(api, 'post', data, headers, stream)

    @staticmethod
    def put(api='', data={}, headers={}, stream=True):
        return _request(api, 'put', data, headers, stream)

    @staticmethod
    def delete(api='', headers={}, stream=True):
        return _request(api, 'delete', {}, headers, stream)


if __name__ == '__main__':
    r = Request.get('http://baidu.com')
    print(r)
