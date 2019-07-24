content = '''
# 所有用例模块配置
apis:
  #user模块
  user:
    # 登录 login_st.py
    login:
      className: TestUserLogin # 接口类名
      funName:
        # 接口方法名
        test_login:
          name: 登录 # 接口注释
          url: /api/login
          # 请求类型
          mode: post
          # 参数
          data:
            name: 15000000000
            password: 123
    # 获取所有用户 users_st.py
    users:
      className: TestUsers # 接口类名
      funName:
        # 接口方法名
        test_get_users:
          name: 登录 # 接口注释
          url: /api/get_users
          # 请求类型
          mode: get
    # 获取用户 user_st.py
    user:
      className: TestUser # 接口类名
      funName:
        # 接口方法名
        test_get_user:
          name: 登录 # 接口注释
          url: /api/get_user
          # 请求类型
          mode: get
          # 参数
          data:
            id: 1
'''


def get_config_apis_tpl():
    return content


if __name__ == '__main__':
    print(get_config_apis_tpl())
