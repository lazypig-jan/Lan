from setuptools import setup

setup(
    name="lan",
    version='0.0.1',
    description="Lan(懒)是一套测试套装脚手架 .",
    long_description="Lan(懒)是一套测试套装脚手架 .",
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Build Tools',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
    ],
    keywords='lan python test',
    author='BIJ',
    author_email='bobofpl@gmail.com',
    url='https://github.com/bbfpl/Lan',
    license='MIT',
    packages=[
        'lan',
        'lan.commands',
        'lan.commands.it',
        'lan.commands.sm',
        'lan.commands.st'
    ],
    package_data={
        '': ['*.txt', '*.html'],
    },
    entry_points=dict(console_scripts=['lan=lan.cli:main']),
    install_requires=[
        'requests',
        'TinyDB',
        'logzero',
        'jinja2',
        'flask',
        # 'locust',
        'unittest2'
    ],
    zip_safe=False)
