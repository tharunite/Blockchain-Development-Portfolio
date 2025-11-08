// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

interface IERC173 {
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);
    function owner() external view returns (address);
    function transferOwnership(address newOwner) external;
}

interface IERC20 {
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    function name() external view returns (string memory);
    function symbol() external view returns (string memory);
    function decimals() external view returns (uint8);
    function totalSupply() external view returns (uint256);
    function balanceOf(address account) external view returns (uint256);
    function transfer(address to, uint256 value) external returns (bool);
    function approve(address spender, uint256 value) external returns (bool);
    function allowance(address owner, address spender) external view returns (uint256);
    function transferFrom(address from, address to, uint256 value) external returns (bool);
}

contract Token is IERC20, IERC173 {
    string public name;
    string public symbol;
    uint8 public immutable decimals;
    uint256 private _totalSupply;

    mapping(address => uint256) private _balances;
    mapping(address => mapping(address => uint256)) private _allowances;

    address private _owner;

    constructor(
        string memory _name,
        string memory _symbol,
        uint8 _decimals,
        uint256 initialSupply
    ) {
        name = _name;
        symbol = _symbol;
        decimals = _decimals;
        _totalSupply = initialSupply;
        _balances[msg.sender] = initialSupply;

        _owner = msg.sender;
        emit Transfer(address(0), msg.sender, initialSupply);
        emit OwnershipTransferred(address(0), msg.sender);
    }

    modifier onlyOwner() {
        require(msg.sender == _owner, "Not owner");
        _;
    }

    // --- IERC173 ---
    function owner() external view override returns (address) {
        return _owner;
    }

    function transferOwnership(address newOwner) external override onlyOwner {
        require(newOwner != address(0), "Invalid address");
        emit OwnershipTransferred(_owner, newOwner);
        _owner = newOwner;
    }

    function totalSupply() external view override returns (uint256) {
        return _totalSupply;
    }

    function balanceOf(address account) external view override returns (uint256) {
        return _balances[account];
    }

    function transfer(address to, uint256 value) external override returns (bool) {
        _transfer(msg.sender, to, value);
        return true;
    }

    function approve(address spender, uint256 value) external override returns (bool) {
        _approve(msg.sender, spender, value);
        return true;
    }

    function allowance(address ownerAddr, address spender) external view override returns (uint256) {
        return _allowances[ownerAddr][spender];
    }

    function transferFrom(address from, address to, uint256 value) external override returns (bool) {
        uint256 allowed = _allowances[from][msg.sender];
        require(allowed >= value, "Allowance too low");
        _allowances[from][msg.sender] = allowed - value;

        _transfer(from, to, value);
        return true;
    }

    function _transfer(address from, address to, uint256 value) internal {
        require(to != address(0), "Zero address");
        require(_balances[from] >= value, "Insufficient balance");

        _balances[from] -= value;
        _balances[to] += value;

        emit Transfer(from, to, value);
    }

    function _approve(address ownerAddr, address spender, uint256 value) internal {
        require(spender != address(0), "Zero address");
        _allowances[ownerAddr][spender] = value;
        emit Approval(ownerAddr, spender, value);
    }

    function mint(address to, uint256 amount) external onlyOwner {
        require(to != address(0), "Zero address");
        _totalSupply += amount;
        _balances[to] += amount;
        emit Transfer(address(0), to, amount);
    }

    function burn(uint256 amount) external {
        require(_balances[msg.sender] >= amount, "Not enough balance");
        _balances[msg.sender] -= amount;
        _totalSupply -= amount;
        emit Transfer(msg.sender, address(0), amount);
    }
}
