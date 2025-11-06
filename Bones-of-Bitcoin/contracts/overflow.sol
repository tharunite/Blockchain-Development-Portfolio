// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract OverandUnderflowDemo {
    uint8 public bigNum = 255;
    uint8 public smallNum = 0;

    function overflowPreview() public pure returns (uint8 beforeValue, uint8 afterValue) {
        uint8 temp = 255;
        unchecked {
            uint8 overflowed = temp + 1; 
            return (temp, overflowed);
        }
    }
    function underflowPreview() public pure returns (uint8 beforeValue, uint8 afterValue) {
        uint8 temp = 0;
        unchecked {
            uint8 underflow = temp - 1; 
            return (temp, underflow);
        }
    }
}
