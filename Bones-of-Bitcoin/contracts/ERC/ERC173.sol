// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;
interface IERC173{
    event ownershipTransfered(address indexed previousOwner,address indexed  newOwner);

    function owner() view external returns(address);
    function transferOwnership(address newOwner) external ;
}

contract Ownership is IERC173{
    address private _owner;

    constructor(){
        _owner=msg.sender;
        emit ownershipTransfered(address(0), _owner);
    }


    function owner() view external override returns(address){
        return _owner;
    }


    modifier onlyOwner(){
        require(msg.sender==_owner,"Only Owner can call this function");
        _;
    }


    function transferOwnership(address newOwner) external override  onlyOwner{
        require(newOwner!=address(0),"address(0) is the null address");
        emit ownershipTransfered(_owner, newOwner);
        _owner=newOwner;
    }
    
}