import hmac
import hashlib
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt



from typing import Any

def load(path: str) -> np.ndarray:
    img = Image.open(path).convert("L")
    return np.array(img)


def resize(image: np.ndarray, block_size: int) -> np.ndarray:
    return image[:image.shape[0] // block_size * block_size, :image.shape[1] // block_size * block_size]


def combine(blocks: np.ndarray, image_shape: tuple) -> np.ndarray:
    height, width = image_shape
    block_size = blocks.shape[1]
    return blocks.reshape(height // block_size, width // block_size, block_size, block_size).swapaxes(1, 2).reshape(height, width)

def split(image: np.ndarray, block_size: int) -> np.ndarray:
    height, width = image.shape
    return image.reshape(height // block_size, block_size, width // block_size, block_size).swapaxes(1, 2).reshape(-1, block_size, block_size)

def encode_one(block: np.ndarray, key: str = "") -> np.ndarray:
    block_shape = block.shape
    byte_string = hmac.new(key.encode(), block.tobytes(), hashlib.md5).hexdigest()
    decoded_array = np.frombuffer(bytes.fromhex(byte_string), dtype=np.uint8)

    if len(decoded_array) < block.size:
        decoded_array = np.pad(decoded_array, (0, block.size - len(decoded_array)))
    decoded_array = decoded_array.reshape(block_shape)
    return decoded_array



def encode_ECB(image: np.ndarray, key: str, blocks: np.ndarray) -> None:
    result = np.zeros(blocks.shape, dtype=np.uint8)
    for i, block in enumerate(blocks):
        result[i] = encode_one(block, key)
    image_encoded = result
    image_reconstructed = combine(image_encoded, image.shape)
    plt.imsave(f"ecb_crypto.bmp", image_reconstructed, cmap="gray")


def encode_CBC(image: np.ndarray, key: str, blocks: np.ndarray) -> None:
    result = np.zeros(blocks.shape, dtype=np.uint8)
    prev_block = np.random.randint(0, 2, blocks[0].shape, dtype=np.uint8)

    for i, block in enumerate(blocks):
        new_block = np.array([pixel ^ prev_pixel for pixel, prev_pixel in zip(block.flatten(), prev_block.flatten())])
        new_block = new_block.reshape(blocks[0].shape)
        new_block = encode_one(new_block, key)
        prev_block = new_block
        result[i] = new_block

    image_encoded = result
    image_reconstructed = combine(image_encoded, image.shape)
    plt.imsave(f"cbc_crypto.bmp", image_reconstructed, cmap="gray")


def main() -> None:
    image_path = "plain.bmp"
    block_size = 4
    key = "nie wiem"

    image = load(image_path)
    image = image[:image.shape[0] // block_size * block_size, :image.shape[1] // block_size * block_size]
    blocks = split(image, block_size)

    encode_ECB(image, key, blocks)
    encode_CBC(image, key, blocks)


if __name__ == "__main__":
    main()
