// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract toggle{
    bool public locked = true; 
    
    function toggleLock() public {
        locked = !locked; 
    }
}