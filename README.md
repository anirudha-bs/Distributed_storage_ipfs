# Distributed_storage_ipfs
A secure way of adding files and retriving them from the IPFS network.
This application also supports one to add newly generated blocks of data using the inbuilt blockchain simulator to add the longest chain to the IPFS network

To use file storage application- 
```
pip install requirements.txt
ipfs daemon
python main.py
```
To use blockchain simulator application- 
Go to blockcchain simulator directory
```
mv blockchain.env .env
go get github.com/davecgh/go-spew/spew
go get github.com/gorilla/mux
go get github.com/joho/godotenv
go run .
```

Now you can run main.py to see changes being commited when new blocks are added via post requests.
