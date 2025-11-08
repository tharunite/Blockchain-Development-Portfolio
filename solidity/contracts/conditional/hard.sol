//Insurance Claim
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Insurance{
    function claim(uint delayHours,bool isVIP,uint dayAfterFlight) pure public returns(uint,string memory){
        if (delayHours <= 3) {
            return (0, "No payout - Delay too short");
        }

        if (dayAfterFlight > 7) {
            return (0, "Claim invalid - submitted too late");
        }
        uint payoutPercent;
        string memory status;
        
        if(delayHours < 6){
            payoutPercent=25;
            status="Approved";
        }
        else if (delayHours<12){
            payoutPercent=50;
            status="Approved";
        }
        else{
            payoutPercent=100;
            status="Approved";
        }

        if(isVIP && payoutPercent!=0 ){
            payoutPercent+=10;
            if(payoutPercent>110){
                payoutPercent=110;
            }
            status=string.concat(status," - VIP bonus applied");
        }
        return(payoutPercent,status);
    }
}