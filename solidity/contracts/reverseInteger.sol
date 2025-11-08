// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;
contract pali{
    function palindrome(uint256 _Number) public pure returns(bool){
        uint256 rev=0;
        uint256 given=_Number;
        while(_Number>0){
            rev=rev*10+_Number%10;
            _Number/=10;
        }
        if(given==rev){
            return  true;
        }
        else{
            return false;
        }

    }
}