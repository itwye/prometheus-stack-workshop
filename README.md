> ## prometheus stack workshop

> ### 安装Vagrant环境

- 下载安装 [virtualbox 5.2 for OSX](https://download.virtualbox.org/virtualbox/5.2.18/VirtualBox-5.2.18-124319-OSX.dmg)
- 下载安装 [vagrant 2.1.2 for OSX](https://releases.hashicorp.com/vagrant/2.1.2/vagrant_2.1.2_x86_64.dmg) 

> ### 启动vagrant初始化VM

1. clone 代码仓库

```
git clone https://github.com/itwye/prometheus-stack-workshop.git

cd prometheus-stack-workshop
```

2. 使用vagrant 启动VM
```
# 在 prometheus-stack-workshop 目录下执行

vagrant up
```

因需要安装docker,docker-compose等，如网络下载速度慢，可能会执行很长时间,请耐心等待...！

> Notes： 如果vagrant 初始化中途网络中断
> 
> 在下载box阶段中断可以直接 `vagrant up` 重新下载 box
> 
> 在shell脚本安装初始化系统阶段中断，可以使用 `vagrant up --provision` 重新初始化


3. VM启动后,登录进入VM.

```
# -------------
# 查询VM状态
# -------------
$ vagrant status

Current machine states:

test-node                 running (virtualbox)

# -------------
# 登录test-node VM
# -------------
$ vagrant ssh test-node

Welcome to Ubuntu 16.04.5 LTS (GNU/Linux 4.4.0-116-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

# -------------
# 切换root用户
# -------------

vagrant@test-node:~$ sudo su -

# ------------
# 启动prometheus stack
# ------------

root@test-node:~# cd /home/vagrant/share/
root@test-node:~# docker-compose up -d

因需要拉取镜像，如网络下载速度慢，可能会执行很长时间，请耐心等待......！

# -----------
# 验证prometheus stack相关container是否启动成功
# -----------

root@test-node:/home/vagrant/share# docker ps
CONTAINER ID        IMAGE                        COMMAND                  CREATED             STATUS              PORTS                    NAMES
5e0d0de86d01        prom/alertmanager:v0.15.1    "/bin/alertmanager..."   About an hour ago   Up About an hour    0.0.0.0:9093->9093/tcp   alertmanager
0c0ea542dff0        itwye/prometheus_client      "python /app/order..."   About an hour ago   Up About an hour    0.0.0.0:8000->8000/tcp   order
652c583c41cc        grafana/grafana:5.2.2        "/run.sh"                About an hour ago   Up About an hour    0.0.0.0:3000->3000/tcp   grafana
5c7e45b7444c        prom/node-exporter:v0.16.0   "/bin/node_exporte..."   About an hour ago   Up About an hour    0.0.0.0:9100->9100/tcp   nodeexporter
378354dca276        prom/prometheus:v2.3.2       "/bin/prometheus -..."   About an hour ago   Up 55 minutes       0.0.0.0:9090->9090/tcp   prometheus
f4d6c073168d        prom/pushgateway             "/bin/pushgateway"       About an hour ago   Up About an hour    0.0.0.0:9091->9091/tcp   pushgateway

```

4. 在宿主机浏览器,确保测试环境是否已OK! (VM IP如你更改过了,下面请替换成你的IP)

```
(1) Prometheus:   http://192.168.33.118:9090

(2) Grafana:    http://192.168.33.118:3000/

(3) Alertmanager:    http://192.168.33.118:9093/

(4) Application metrics:   http://192.168.33.118:8000/

(5) Pushgateway:   http://192.168.33.118:9091/
```


> ### vagrant管理VM

1. 使用如下命令关闭VM
```
vagrant halt
```

2. 启动VM
```
vagrant up
```

3. 启动某个VM
```
vagrant up test-node
```

4. 摧毁VM
```
vagrant destroy
```

