//Escrow Contract
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;
contract Escrow{
    address immutable seller;
    address immutable buyer;
    address constant arbiter=0x5B38Da6a701c568545dCfcB03FcB875f56beddC4;
    uint immutable amount;
    enum state {Funded,Shipped,Released,Refunded}
    state public currentState;
    event Funded(address from,uint amount);
    event Shipped(address from,address to);
    event Released(address from,address to);
    event Refunded(address from,address to);
    modifier onlyArbiter(){
        require(msg.sender==arbiter,"Only arbiter can call this function");
        _;
    }
    constructor(address _seller,address _buyer) payable {
        require(msg.value > 0, "Must send Ether to fund");
        seller=_seller;
        buyer=_buyer;
        amount=msg.value;
        currentState=state.Funded;
        emit Funded(msg.sender,msg.value);
    }
    function ship() external{
        require(currentState == state.Funded, "Must be funded before shipping");
        require(msg.sender==seller,"Only sender can ship");
        currentState=state.Shipped;
        emit Shipped(seller,buyer);
    }
    function received() external {
        require(currentState == state.Shipped, "Item not shipped yet");
        require(msg.sender==buyer,"Only buyer can confirm recieving");
        currentState=state.Released;
        payable(seller).transfer(amount);
        emit Released(buyer,seller);
    }
    function refund() external onlyArbiter {
        require(currentState != state.Released, "Already released");
        payable(buyer).transfer(amount);
        currentState=state.Refunded;
        emit Refunded(arbiter, buyer);

    }
    function getState() public view returns (string memory) {
    if (currentState == state.Funded) return "Funded";
    if (currentState == state.Shipped) return "Shipped";
    if (currentState == state.Released) return "Released";
    if (currentState == state.Refunded) return "Refunded";
    return "Unknown";
}




    }

