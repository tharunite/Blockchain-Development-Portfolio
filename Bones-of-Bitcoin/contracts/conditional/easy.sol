// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Grade {
    function getGrade(uint marks) public pure returns (string memory) {
        if (marks >= 90 && marks <= 100) {
            return "A";
        } else if (marks >= 80 && marks < 90) {
            return "B";
        } else if (marks >= 70 && marks < 80) {
            return "C";
        } else if (marks >= 60 && marks < 70) {
            return "D";
        } else if (marks >= 40 && marks < 60) {
            return "E";
        } else if (marks < 40) {
            return "F";
        } else {
            return "Invalid"; 
        }
    }
}
