// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract simpleStorage{
    uint number;
    
    function set(uint _num) public{
        number = _num;
    }  
     function get() public view returns (uint){
        return number;
    }
}