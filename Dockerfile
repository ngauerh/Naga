FROM ubuntu:16.04
MAINTAINER Aaron <ngauer@gmail.com>


#安装python
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        ca-certificates \
        vim \
        gcc\
        libpython3-dev\
        libsqlite3-dev\
        libbz2-dev\
        libxml2-dev\
        libffi-dev\
        libssl-dev\
        libxslt1-dev\
        python3 \
        curl\
        python3-setuptools\
        python-setuptools\
        git\
        nginx\
        supervisor\
    && rm -rf /var/lib/apt/lists/*


# 安装pip
RUN curl -s https://bootstrap.pypa.io/get-pip.py | python
RUN curl -s https://bootstrap.pypa.io/get-pip.py | python3


# nginx 配置
COPY . /home/www-data/Naga/
COPY conf/naga.conf /etc/nginx/conf.d/
COPY conf/s_naga.conf /etc/supervisor/conf.d/

# 安装依赖
RUN pip3 install uwsgi
RUN pip3 install -r /home/www-data/Naga/requirements.txt


# 暴露端口
EXPOSE 8000




