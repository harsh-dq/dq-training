### 



### Run Polkadot Node
sudo docker run -p 9944:9944 parity/polkadot:v0.8.24 --name "calling_home_from_a_docker_container" --rpc-external --ws-external --unsafe-ws-external --rpc-cors=all

Enable kusama

 sudo docker run -p 9944:9944 parity/polkadot:v0.8.24 --name "calling_home_from_a_docker_container" --rpc-external --ws-external --unsafe-ws-external --rpc-cors=all --chain=kusama


### Run UI for network

sudo docker run --rm -it --net host --name polkadot-ui -e WS_URL=ws://127.0.0.1:9944 -p 80:80 jacogr/polkadot-js-apps:latest



