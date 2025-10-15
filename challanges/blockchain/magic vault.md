// convert age of the /rpc endpoint to timestand 
date -d "$(cast age 1 --rpc-url http://94.237.57.1:42801/rpc )" +%s


//deploy 

``forge create src/Middleman.sol:Middleman --rpc-url http://94.237.49.73:36209/rpc --private-key 0xd3984677af36a4e5b95808bb51f8cb31c9a8e0f367e5168ccde53cba87be5385 --no-cache --broadcast ``