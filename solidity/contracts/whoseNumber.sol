// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;
contract largest{
    uint256 a=0;
    address whose;
    function putNum(uint given) public {
        if(given>a){
            a=given;
            whose=msg.sender;
    }
    }
      
    function gethighest() public view returns(uint256,address ){
        return(a,whose);
    }
    
    }
    
