# ECS198-Cryptocurrency-Technologies
The class materials for ECS 198 - Cryptocurrency Technologies, Spring 2016 taught by Rylan Schaeffer and Vincent Yang.

##### Important Materials
* [Syllabus](https://cdn.rawgit.com/RylanSchaeffer/ECS198-Cryptocurrency-Technologies/master/Syllabus/Course-Syllabus.pdf)
* [Term Project](https://cdn.rawgit.com/RylanSchaeffer/ECS198-Cryptocurrency-Technologies/master/Programs/Term-Project/Term-Project.pdf)

##### Assignments
1. Digital Signatures

  Generate a public/private key pair. Submit your public key and a digital signature of the sentence, "I, [insert your name here], signed this sentence!"  

2. Cryptographic Hash Functions/Merkle Trees

  Submit a program that accepts a string of transactions, and outputs a hash tree of transactions.

3. Proof of Work

  Submit a program that accepts a list of transactions and an integer n, and outputs the value of a nonce such that

  ```hash(root of hash tree | nonce)``` has n leading zeroes


To be updated...

3. Centralized Cryptocurrency

  Submit a program that accepts a list of transactions over a number of "epochs", and outputs a list of valid transactions per epoch

5. Proof of Work (Cont.)
  
  Submit a program that accepts a list of transactions, a nonce and integer n, and verifies that

  ```hash(root of hash tree | nonce)``` has n leading zeroes

6. Decentralized Cryptocurrency

  Submit a program that accepts a block chain or a list of transactions, or hash tree, nonce. 
  For each epoch: 

  If given (hash tree, nonce), verify the proposed block and append to block chain if legitimate

  If given list of transactions, verify the transactions, mine the correct nonce, append the block to block chain

##### Structure
```
.
├── Lectures
│   ├── 0-History
│   ├── 1-DigitalSignatures
│   ├── 2-CryptoHash
│   ├── 3-Decentralization
│   ├── 4-Mining
│   ├── 5-EngineeringDetails
│   ├── 6-Flaws
│   ├── 6.5-Blockchain
│   ├── 7-Anonymity
│   ├── 8-Ethereum
│   └── 9-DAO
├── Programs
│   ├── HW1-Digital-Signatures
│   │   ├── Program\ 1
│   │   └── Submissions
│   ├── HW2-Crypto-Hash
│   │   └── Program\ 2
│   ├── HW3-Mining
│   │   └── Program\ 3
│   └── Term-Project
├── Projects
├── Syllabus
└── Worksheets
    ├── backup
    ├── exam
    ├── hw1
    ├── hw2
    ├── hw3
    ├── hw4
    ├── hw5
    ├── hw6
    ├── hw7
    ├── hw8
    └── hw9
```
