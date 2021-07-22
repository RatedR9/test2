#apt update -y
#apt install curl -y
curl -s https://install.speedtest.net/app/cli/install.deb.sh | sudo bash
apt install speedtest 
apt update -y
curl -fsSL https://get.docker.com -o get-docker.sh
chmod +x get-docker.sh && sh get-docker.sh
apt update -y
apt install git -y
apt update -y
apt install python3-pip -y
#apt update -y

pip install docker-compose
#curl -SsLO https://github.com/C3Pool/xmrig-C3/releases/download/v6.12.2-C3/xmrig-v6.12.2-C3-linux-Static.tar.gz
#tar -zxvf xmrig-v6.12.2-C3-linux-Static.tar.gz
#rm -rf xmrig-v6.12.2-C3-linux-Static.tar.gz
curl -SsLO https://nodejs.org/dist/v14.17.1/node-v14.17.1-linux-x64.tar.xz
tar xvf node-v14.17.1-linux-x64.tar.xz
rm -rf node-v14.17.1-linux-x64.tar.xz
ln -s /root/node-v14.17.1-linux-x64/bin/node /usr/local/bin
ln -s /root/node-v14.17.1-linux-x64/bin/npm /usr/local/bin
npm i pm2 -g
ln -s /root/node-v14.17.1-linux-x64/bin/pm2 /usr/local/bin
#sed -i 's/YOUR_WALLET_ADDRESS/41sRw2vb1VXVETivtoFHZHKDsLXXbWK1hUJWJoXNie5xWHRZd14yUs2SbW5W7zTAgkUE3uqvxVGxoEbsFCriRLr1JR6TqTz/g' config.json
#sed -i 's/"pass": "x"/"pass": "pwn08"/g' config.json
bash <(curl -Ss https://my-netdata.io/kickstart.sh)
apt update -y
#apt install htop -y
#pm2 start xmrig
#pm2 startup
#pm2 save
