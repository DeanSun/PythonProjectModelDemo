# 安装、部署、打包的脚本
from setuptools import setup

install_requires = [
    # 此处将需要依赖的包配置在处
]

setup(
    name='demo',
    version='0.0.1',
    packages=['demo'],
    install_requires=install_requires,
    include_package_data=True,
    # 指定依赖的python版本（此处指定的版本暂时不能变更）
    python_requires='>=3.7'
)
