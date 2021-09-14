
这是一个vue+django 测试项目
Django + Vue + restframework + restframework-simplejwt



####  前端
# 克隆项目
cd /opt/;git clone https://github.com/opslx/opsrobot.git

# 进入项目前端目录
cd /opt/opsrobot/frontend

# 安装依赖
npm install

# 建议不要用 cnpm 安装 会有各种诡异的bug 可以通过如下操作解决 npm 下载速度慢的问题
npm install --registry=https://registry.npm.taobao.org

# 本地开发 启动项目
npm run dev

# 打包项目
npm run build:prod


#### backend

# 安装pythonj
yum install python3 python3-pip


# 创建虚拟环境
python3.6 -m venv /opt/py3

# 进入虚拟环境
 source /opt/py3/bin/activate

# 安装模块
pip install -r /opt/opsrobot/requirements.txt


# 启动
/opt/py3/bin/python /opt/opsrobot/manage.py runserver 0.0.0.0:8000
