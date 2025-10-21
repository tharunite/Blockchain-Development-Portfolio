# Blockchain Project To-Do List

## Phase 1: Core Blockchain
- [x] Genesis Block Initialization
  - [x] Create block with Id=0
  - [x] Set timestamp
  - [x] Initialize empty transactions list
  - [x] Set prev_hash = '0'*16
  - [x] Compute and store hash
- [x] Block Hashing
  - [x] Implement SHA-256 hashing of block content
  - [x] Ensure hash is consistent and deterministic
- [x] Proof-of-Work (Mining)
  - [x] Add nonce field to block
  - [x] Implement difficulty parameter
  - [x] Create mining loop to find valid hash
  - [x] Break loop when hash meets difficulty
- [x] Adding Transactions
  - [x] Implement `add_transaction()` method
  - [x] Store transactions in `pending_transaction` list

## Phase 2: Transaction Security
- [ ] Transaction Verification
  - [ ] Ensure sender and recipient are valid
  - [ ] Amount must be positive
  - [ ] Reject malformed transactions
- [ ] Account Balance Checks
  - [ ] Implement `get_balance(address)`
  - [ ] Reject transaction if sender has insufficient balance
- [ ] Mining Reward
  - [ ] Add `"NETWORK"` → miner reward transaction
  - [ ] Include reward in `pending_transaction` before mining
- [ ] Chain Validation
  - [ ] Validate `prev_hash` for each block
  - [ ] Recompute hash with nonce to ensure PoW
  - [ ] Ensure entire chain is tamper-proof

## Phase 3: Advanced Security
- [ ] Transaction Signing & Digital Signatures
  - [ ] Generate private/public key pairs for users
  - [ ] Sign transactions using sender private key
  - [ ] Verify signatures before adding transaction
  - [ ] Allow mining rewards without signature

## Phase 4: Utilities & Queries
- [ ] Implement `get_last_block()`
- [ ] Implement `get_block_by_index(index)`
- [ ] Implement `get_balance(address)`
- [ ] Pretty-print blocks or chain summary

## Phase 5: Persistence
- [ ] Save blockchain to JSON file
- [ ] Load blockchain from file at startup
- [ ] Append blocks incrementally to file
- [ ] Ensure memory chain and file are synchronized

## Phase 6: Optional Networking / P2P
- [ ] Maintain a list of peer nodes
- [ ] Broadcast newly mined blocks to peers
- [ ] Receive blocks from peers
- [ ] Resolve forks using longest valid chain
- [ ] Validate incoming blocks before adding to chain

## Phase 7: Testing & Debugging
- [ ] Generate multiple user accounts
- [ ] Create and sign test transactions
- [ ] Mine multiple blocks and verify PoW
- [ ] Test transaction rejection (invalid signature, insufficient funds)
- [ ] Test chain validation after tampering attempts
- [ ] Verify persistence and file integrity

## Phase 8: Difficulty & Performance
- [ ] Test different difficulty values
- [ ] Adjust difficulty for reasonable mining speed
- [ ] Benchmark mining performance
- [ ] Optimize hashing loop if necessary
