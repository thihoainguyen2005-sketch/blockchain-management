import hashlib
import time

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        return hashlib.sha256(
            (str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash) + str(self.nonce)).encode()
        ).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, time.time(), "Genesis Block", "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        # Tự gán previous_hash từ block cuối cùng
        new_block.previous_hash = self.get_latest_block().hash
        # Tính lại hash mới sau khi gán previous_hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)

# Tạo blockchain và thêm dữ liệu
my_blockchain = Blockchain()
my_blockchain.add_block(Block(1, time.time(), "Hồ sơ sinh viên: Nguyễn Văn A", ""))
my_blockchain.add_block(Block(2, time.time(), "Hợp đồng kinh doanh: ABC", ""))
my_blockchain.add_block(Block(3, time.time(), "Hồ sơ sinh viên: Trần Thị B", ""))
my_blockchain.add_block(Block(4, time.time(), "Hợp đồng kinh doanh: XYZ", ""))

# Hiển thị blockchain
for block in my_blockchain.chain:
    print(f"Index: {block.index}, Data: {block.data}, Hash: {block.hash}")