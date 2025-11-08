//ELECTRICITY BILL 
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract ElectricityBill {
    function calculateBill(uint units) public pure returns (uint totalCost, string memory Usage) {
        uint totalcost;
        string memory usage;
        if (units == 0) {
            totalcost= 0;
        }
        else if (units <= 100) {
            totalcost= units * 1 wei;
        }
        else if (units <= 300) {
            totalcost= (100 * 1 wei) + ((units - 100) * 2 wei);
        }
        else {
            totalcost= (100 * 1 wei) + (200 * 2 wei) + ((units - 300) * 3 wei);
        }
        usage= billCategory(totalcost);
        return (totalcost,usage);
    }

    function billCategory(uint totalCost) internal pure returns (string memory usage) {
        if (totalCost == 0) {
            return "No Usage";
        }
        else if (totalCost < 200 wei) {
            return "Low Usage";
        }
        else if (totalCost < 600 wei) {
            return "Medium Usage";
        }
        else {
            return "High Usage";
        }
    }
}
