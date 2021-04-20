# Blockchain_simulator

This a simple blockchain simulator to illustrate how blockhain works.
It uses structure to store the data of each block in memory and later writes it to a file in a json format to keep track of the longest chain.
It also validates newly added blocks and follows longest valid chain protocol.

To use it -
```
go run .
```

Go to localhost/8080 to view the blocks

Use postman to send a post request to localhost/8080 with {Key:(any integer value)} in the request body to add new blocks.
It automatically appends the newly added blocks to the file.

