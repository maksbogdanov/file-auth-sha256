import hashlib
import os.path


class FileAuth:
    def __init__(self, filename, block_size):
        self.__file = open(filename, "rb")
        self.__block_size = block_size
        self.__file_size = os.path.getsize(filename)

    def auth(self):
        hashed_block = bytes()
        for block in reversed(self.__get_blocks()):
            hashed_block = hashlib.sha256(block + hashed_block).digest()
        return hashed_block

    def __get_blocks(self):
        blocks = []
        block = self.__file.read(self.__block_size)
        while block:
            blocks.append(block)
            block = self.__file.read(self.__block_size)
        return blocks

    def __del__(self):
        self.__file.close()
