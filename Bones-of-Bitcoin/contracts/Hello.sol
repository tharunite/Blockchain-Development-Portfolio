// SPDX-License-Identifier: MIT
pragma solidity ^0.8.13;
contract Hello{
    string public greet;
    constructor()  {
        greet = "Hello";
    }

    function customGreet(string memory _greet) public {
        greet = _greet;
    }

    function greets() public view returns (string memory) {
        return greet;
    }
}