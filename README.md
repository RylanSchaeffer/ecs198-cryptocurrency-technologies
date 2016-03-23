# ECS198-Cryptocurrency-Technologies

##### Structure
.
├── Lectures
│   ├── 0-History
│   │   ├── 0-History.aux
│   │   ├── 0-History.log
│   │   ├── 0-History.pdf
│   │   ├── 0-History.synctex.gz
│   │   └── 0-History.tex
│   ├── 1-DigitalSignatures
│   │   ├── 1-DigitalSignatures.aux
│   │   ├── 1-DigitalSignatures.log
│   │   ├── 1-DigitalSignatures.out
│   │   ├── 1-DigitalSignatures.pdf
│   │   └── 1-DigitalSignatures.tex
│   ├── 2-CryptoHash
│   │   ├── 2-CryptoHash.aux
│   │   ├── 2-CryptoHash.log
│   │   ├── 2-CryptoHash.pdf
│   │   ├── 2-CryptoHash.synctex.gz
│   │   └── 2-CryptoHash.tex
│   ├── 3-CentralCrypto
│   │   ├── 3-CentralCrypto.log
│   │   └── 3-CentralCrypto.out
│   └── 3-Centralization
│       ├── 3-CentralCrypto.aux
│       ├── 3-CentralCrypto.pdf
│       └── 3-CentralCrypto.tex
├── Programs
│   ├── HW1-Digital-Signatures
│   │   ├── SchaefferRylanHW1Submission.py
│   │   ├── SchaefferRylanHW1Submission.pyc
│   │   └── grader.py
│   └── HW2-Crypto-Hash
│       ├── SchaefferRylanHW2Submission.py
│       ├── transactionGenerator.py
│       └── transactions.txt
├── README.md
├── Syllabus
│   ├── Course-Syllabus.pdf
│   └── Course-Syllabus.tex
├── Worksheets
│   ├── backup
│   │   ├── hw1.aux
│   │   ├── hw1.log
│   │   ├── hw1.pdf
│   │   ├── hw1.tex
│   │   └── hw1.toc
│   ├── exam
│   │   ├── README
│   │   ├── exam.cls
│   │   ├── exam.md5
│   │   ├── examdoc.pdf
│   │   └── examdoc.tex
│   ├── hw1
│   │   ├── hw1.aux
│   │   ├── hw1.log
│   │   ├── hw1.pdf
│   │   ├── hw1.tex
│   │   ├── oldhw1.pdf
│   │   └── oldhw1.tex
│   ├── hw2
│   ├── hw3
│   │   └── hw3.tex
│   ├── hw4
│   ├── hw5
│   ├── hw6
│   ├── hw7
│   ├── hw8
│   └── hw9
└── temp

22 directories, 47 files

##### Assignments
1. Digital Signatures

  Generate a public/private key pair. Submit your public key and a digital signature of the sentence, "I, [insert your name here], signed this sentence!"  

2. Cryptographic Hash Functions/Merkle Trees

  Submit a program that accepts a string of transactions, and outputs a hash tree of transactions.

3. Centralized Cryptocurrency

  Submit a program that accepts a list of transactions over a number of "epochs", and outputs a list of valid transactions per epoch

4. Proof of Work

  Submit a program that accepts a list of transactions and an integer n, and outputs the value of a nonce such that

  ```hash(root of hash tree | nonce)``` has n leading zeroes

5. Proof of Work (Cont.)
  
  Submit a program that accepts a list of transactions, a nonce and integer n, and verifies that

  ```hash(root of hash tree | nonce)``` has n leading zeroes

6. Decentralized Cryptocurrency

  Submit a program that accepts a block chain or a list of transactions, or hash tree, nonce. 
  For each epoch: 

  If given (hash tree, nonce), verify the proposed block and append to block chain if legitimate

  If given list of transactions, verify the transactions, mine the correct nonce, append the block to block chain

7.
  
8

9.

