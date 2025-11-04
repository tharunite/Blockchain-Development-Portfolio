<h1 align="center">⛓️ Tharie v1.0 — A Minimal Blockchain in Python</h1>

<p align="center">
  <b>Educational blockchain prototype</b><br>
  Built from scratch in Python to understand the core mechanics behind Bitcoin and Ethereum-style systems.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/language-Python%203.8+-blue" />
  <img src="https://img.shields.io/badge/license-MIT-green" />
  <img src="https://img.shields.io/badge/status-educational-yellow" />
</p>

---

## 🧩 Overview

**Tharie v1.0** is a self-contained blockchain implementation written purely in Python.  
It demonstrates the **core architecture of a cryptocurrency ledger** — block creation, hashing, proof-of-work, digital signatures, and persistence — all without external dependencies or networking.

This project was built for **learning and experimentation**, not production or public deployment.

---

## 🚀 Features

| Core Feature | Description |
|:--------------|:------------|
| 🧱 **Genesis Block** | Automatically generates a valid starting block. |
| 💸 **Transactions** | Signed using ECDSA (SECP256k1) for authenticity. |
| 🧾 **Pending Transaction Pool** | Collects transactions before inclusion in a block. |
| ⚙️ **Proof-of-Work Mining** | Finds a valid nonce meeting the difficulty target. |
| 🔗 **Block Hashing** | Each block’s hash depends on its data and previous hash. |
| 💾 **File-Based Persistence** | Stores blocks in `blockchain.txt`. |
| 🔐 **Signature Verification** | Ensures no tampering between sender and recipient. |

---

## 🧠 Architecture

Blockchain
├── Blocks
│ ├── Header
│ │ ├── Timestamp
│ │ ├── Previous Hash
│ │ └── Nonce
│ └── Transactions[]
│ ├── Sender
│ ├── Receiver
│ ├── Amount
│ ├── Signature
│ └── Public Key
└── Chain (linked via hashes)