# -*- mode: ruby -*-
# vi: set ft=ruby :

hosts = {"test-node" => "192.168.33.118"}

$script = <<SCRIPT

apt-get update -y
apt-get install -y apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"

apt-get update -y
apt-get install docker-ce=17.03.2~ce-0~ubuntu-xenial -y --allow-downgrades

curl -L "https://github.com/docker/compose/releases/download/1.22.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose

rm -f /etc/docker/daemon.json && curl -sSL https://get.daocloud.io/daotools/set_mirror.sh | sh -s https://azxnenh6.mirror.aliyuncs.com
systemctl daemon-reload
systemctl restart docker

docker version
docker-compose --version

SCRIPT


Vagrant.configure("2") do |config|
  hosts.each do |name, ip|
    config.vm.define name do |machine|
      machine.vm.box = "bento/ubuntu-16.04"
      machine.vm.hostname = name
      machine.vm.network :private_network, ip: ip
      machine.vm.synced_folder "share/" , "/home/vagrant/share"
      machine.vm.provision "shell", inline: $script
      machine.vm.provider "virtualbox" do |v|
          v.name = name
          v.customize ["modifyvm", :id, "--memory", 2048]
      end
    end
  end
end
