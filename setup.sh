wget https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh
bash script.deb.sh
apt-get update
apt-get install git-lfs
apt-get install -y git wget curl
apt-get install tmux
rm script.deb.sh
mkdir -p ~/miniconda3
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm ~/miniconda3/miniconda.sh
cd ~
source miniconda3/bin/activate
conda init --all