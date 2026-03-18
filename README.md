# Mô phỏng Blockchain cho phần mềm quản lý

## 1. Tổng quan Blockchain
- Blockchain là sổ cái phân tán, ghi nhận dữ liệu liên kết với nhau.
- Mỗi khối chứa:
  - Index
  - Timestamp
  - Data (ví dụ: hồ sơ sinh viên, hợp đồng)
  - Previous Hash
  - Hash
  - Nonce

## 2. Các cơ chế trong Blockchain
- **Proof-of-Work (PoW)**: giải toán để tạo khối
- **Proof-of-Stake (PoS)**: tạo khối dựa trên số token
- **Consensus**: đồng thuận giữa các node
- **Hashing**: đảm bảo dữ liệu không thay đổi

## 3. Phiên bản Blockchain
- Public Blockchain: Bitcoin, Ethereum
- Private Blockchain: Hyperledger
- Consortium / Hybrid Blockchain: ngân hàng, chuỗi cung ứng

## 4. Sơ đồ Blockchain (ASCII)
+--------+     +--------+     +---------+
| Block0 | --> | Block1 | --> | Block2  |
| Genesis|     | Student|     | Contract|
| Hash0  |     | Hash1  |     | Hash2   |
+--------+     +--------+     +---------+

## 5. Hướng dẫn chạy code Python
1. Mở VS Code, mở folder `blockchain_project`.
2. Chạy file `blockchain.py`.
3. Output sẽ hiển thị các block đã tạo, bao gồm Genesis, Student, Contract.