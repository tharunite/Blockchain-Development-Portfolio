// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title HelloWorld
 * @author Your Name
 * @notice A sophisticated Hello World contract with multiple features
 * @dev This contract demonstrates advanced Solidity features including events, modifiers, and structs
 */
contract HelloWorld {
    // State variables
    address public owner;
    string public currentGreeting;
    uint256 public greetingCount;
    uint256 public constant MAX_GREETING_LENGTH = 100;
    
    // Custom errors
    error Unauthorized();
    error InvalidGreeting();
    error GreetingTooLong();
    error NoHistory();
    
    // Struct to store greeting history
    struct GreetingRecord {
        string message;
        address setBy;
        uint256 timestamp;
        uint256 blockNumber;
    }
    
    // Mappings and arrays
    mapping(address => string) public personalizedGreetings;
    mapping(string => uint256) public greetingFrequency;
    GreetingRecord[] public greetingHistory;
    
    // Events
    event GreetingUpdated(
        address indexed setBy,
        string newGreeting,
        uint256 timestamp,
        uint256 greetingNumber
    );
    
    event PersonalizedGreetingSet(
        address indexed user,
        string greeting,
        uint256 timestamp
    );
    
    event OwnershipTransferred(
        address indexed previousOwner,
        address indexed newOwner
    );
    
    // Modifiers
    modifier onlyOwner() {
        if (msg.sender != owner) revert Unauthorized();
        _;
    }
    
    modifier validGreeting(string memory _greeting) {
        bytes memory greetingBytes = bytes(_greeting);
        if (greetingBytes.length == 0) revert InvalidGreeting();
        if (greetingBytes.length > MAX_GREETING_LENGTH) revert GreetingTooLong();
        _;
    }
    
    /**
     * @dev Constructor sets the initial greeting and owner
     */
    constructor() {
        owner = msg.sender;
        currentGreeting = "Hello, World!";
        greetingCount = 1;
        
        greetingHistory.push(GreetingRecord({
            message: currentGreeting,
            setBy: msg.sender,
            timestamp: block.timestamp,
            blockNumber: block.number
        }));
        
        greetingFrequency[currentGreeting] = 1;
        
        emit GreetingUpdated(msg.sender, currentGreeting, block.timestamp, greetingCount);
    }
    
    /**
     * @notice Set a new global greeting
     * @param _greeting The new greeting message
     * @dev Only owner can set global greeting, with validation
     */
    function setGreeting(string memory _greeting) 
        public 
        onlyOwner 
        validGreeting(_greeting) 
    {
        currentGreeting = _greeting;
        greetingCount++;
        
        greetingHistory.push(GreetingRecord({
            message: _greeting,
            setBy: msg.sender,
            timestamp: block.timestamp,
            blockNumber: block.number
        }));
        
        greetingFrequency[_greeting]++;
        
        emit GreetingUpdated(msg.sender, _greeting, block.timestamp, greetingCount);
    }
    
    /**
     * @notice Get the current greeting
     * @return The current greeting string
     */
    function getGreeting() public view returns (string memory) {
        return currentGreeting;
    }
    
    /**
     * @notice Set a personalized greeting for the caller
     * @param _greeting Personalized greeting message
     */
    function setPersonalizedGreeting(string memory _greeting) 
        public 
        validGreeting(_greeting) 
    {
        personalizedGreetings[msg.sender] = _greeting;
        emit PersonalizedGreetingSet(msg.sender, _greeting, block.timestamp);
    }
    
    /**
     * @notice Get personalized greeting for a specific address
     * @param _address Address to query
     * @return Personalized greeting or empty string if not set
     */
    function getPersonalizedGreeting(address _address) 
        public 
        view 
        returns (string memory) 
    {
        return personalizedGreetings[_address];
    }
    
    /**
     * @notice Get greeting for caller (personalized if available, otherwise global)
     * @return The appropriate greeting for the caller
     */
    function getMyGreeting() public view returns (string memory) {
        bytes memory personal = bytes(personalizedGreetings[msg.sender]);
        if (personal.length > 0) {
            return personalizedGreetings[msg.sender];
        }
        return currentGreeting;
    }
    
    /**
     * @notice Get the full greeting history
     * @return Array of all greeting records
     */
    function getGreetingHistory() public view returns (GreetingRecord[] memory) {
        return greetingHistory;
    }
    
    /**
     * @notice Get the latest greeting record
     * @return Latest greeting record with all details
     */
    function getLatestGreeting() public view returns (GreetingRecord memory) {
        if (greetingHistory.length == 0) revert NoHistory();
        return greetingHistory[greetingHistory.length - 1];
    }
    
    /**
     * @notice Get total number of greeting changes
     * @return Total count of greetings set
     */
    function getGreetingCount() public view returns (uint256) {
        return greetingCount;
    }
    
    /**
     * @notice Get frequency of a specific greeting
     * @param _greeting The greeting to check
     * @return Number of times this greeting was used
     */
    function getGreetingFrequency(string memory _greeting) 
        public 
        view 
        returns (uint256) 
    {
        return greetingFrequency[_greeting];
    }
    
    /**
     * @notice Transfer ownership of the contract
     * @param _newOwner Address of the new owner
     */
    function transferOwnership(address _newOwner) public onlyOwner {
        if (_newOwner == address(0)) revert InvalidGreeting();
        address oldOwner = owner;
        owner = _newOwner;
        emit OwnershipTransferred(oldOwner, _newOwner);
    }
    
    /**
     * @notice Get contract statistics
     * @return count Total greeting count
     * @return historyLength Length of greeting history
     * @return currentOwner Current owner address
     */
    function getStats() 
        public 
        view 
        returns (
            uint256 count,
            uint256 historyLength,
            address currentOwner
        ) 
    {
        return (greetingCount, greetingHistory.length, owner);
    }
}
