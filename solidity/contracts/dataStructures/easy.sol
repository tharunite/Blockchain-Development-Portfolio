// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;
contract SavingsTracker{
    mapping(address=>uint) public balances;
    function deposit() public payable{
        require(msg.value>0,"Amount should be greater than zero");
        balances[msg.sender]+=msg.value;
    }
    function withdraw(uint256 amount) public {
        require(amount<=balances[msg.sender],"Insufficient balance");
        balances[msg.sender]-=amount;
        payable(msg.sender).transfer(amount);
    }
    function check() view public returns(uint256){
        return balances[msg.sender];

    }

}