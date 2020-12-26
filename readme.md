
clone the git repo:
---------------------------
git clone https://github.com/nitinawathare/RenoirExperiment.git
git clone https://github.com/sourav1547/go-renoir.git


Install python3, go version 1.9.3, solidity version 0.4.25, web3 version 4.9.0, py-solc, etc:
---------------------------------------------------------------------------------------------
sh installGo.sh
sh installpy3.sh


Compile and install geth:
-------------------------
cd go-renoir
git checkout Renoir_Implementation_VaryingSimilarity
make clean
make
cd ..


For local 10 node setup : 
---------------------------------------------
mv RenoirExperiment RenoirExperiment10Nodes
cd RenoirExperiment10Nodes
git checkout artifactLocalSetup
sh runExperiment.sh


For 50 node setup on different machine
---------------------------------------------
cd RenoirExperiment
git checkout artifact

sh copyScripts.sh
sh installGoLocal.sh
sh downloadEVDCodeLocal.sh
sh setupEthereumLocal.sh
sh initGenesis.sh
sh runExperiment.sh
