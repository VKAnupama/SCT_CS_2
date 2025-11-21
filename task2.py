from PIL import Image
import numpy as np
import random

def load_image(path):
    return np.array(Image.open(path).convert("RGB"), dtype=np.uint8)

def save_image(arr, path):
    Image.fromarray(arr.astype(np.uint8)).save(path)

# --------------------------
# XOR encryption/decryption
# --------------------------
def xor_operation(arr, key):
    return np.bitwise_xor(arr, key)

# --------------------------
# ADD encryption/decryption
# --------------------------
def add_operation(arr, value):
    return (arr + value) % 256

def subtract_operation(arr, value):
    return (arr - value) % 256

# --------------------------
# Shuffle + Unshuffle
# --------------------------
def shuffle_pixels(arr, seed):
    h, w, c = arr.shape
    flat = arr.reshape(-1, c)
    random.seed(seed)
    
    indices = list(range(len(flat)))
    random.shuffle(indices)

    shuffled = flat[indices]
    return shuffled.reshape(h, w, c), indices

def unshuffle_pixels(arr, indices):
    h, w, c = arr.shape
    flat = arr.reshape(-1, c)

    unshuffled = np.zeros_like(flat)
    for i, idx in enumerate(indices):
        unshuffled[idx] = flat[i]

    return unshuffled.reshape(h, w, c)

# ======================================================
#                   MAIN PROGRAM
# ======================================================

print("===== Image Encryption / Decryption Tool =====")

mode = input("Choose mode (encrypt/decrypt): ").strip().lower()

image_path = input("Enter image path: ").strip()
img = load_image(image_path)

print("\nChoose Method:")
print("1. XOR")
print("2. ADD")
print("3. PIXEL SHUFFLE")

choice = int(input("Enter choice (1/2/3): "))

# --------------------------
# ENCRYPTION
# --------------------------
if mode == "encrypt":

    if choice == 1:
        key = int(input("Enter XOR key (0-255): "))
        output = xor_operation(img, key)
        save_image(output, "encrypted_xor.png")
        print("Saved as encrypted_xor.png")

    elif choice == 2:
        value = int(input("Enter ADD value (0-255): "))
        output = add_operation(img, value)
        save_image(output, "encrypted_add.png")
        print("Saved as encrypted_add.png")

    elif choice == 3:
        seed = int(input("Enter shuffle seed (any number): "))
        output, perm = shuffle_pixels(img, seed)
        save_image(output, "encrypted_shuffle.png")

        # Save permutation for decrypt
        np.save("shuffle_key.npy", np.array(perm))

        print("Saved as encrypted_shuffle.png")
        print("Key saved as shuffle_key.npy — DO NOT DELETE IT!")

    else:
        print("Invalid choice!")


# --------------------------
# DECRYPTION
# --------------------------
elif mode == "decrypt":

    if choice == 1:
        key = int(input("Enter SAME XOR key used in encryption: "))
        output = xor_operation(img, key)
        save_image(output, "decrypted_xor.png")
        print("Saved as decrypted_xor.png")

    elif choice == 2:
        value = int(input("Enter SAME ADD value used in encryption: "))
        output = subtract_operation(img, value)
        save_image(output, "decrypted_add.png")
        print("Saved as decrypted_add.png")

    elif choice == 3:
        print("Loading shuffle_key.npy...")
        perm = np.load("shuffle_key.npy")
        output = unshuffle_pixels(img, perm)
        save_image(output, "decrypted_shuffle.png")
        print("Saved as decrypted_shuffle.png")

    else:
        print("Invalid choice!")

else:
    print("Invalid mode! Type encrypt or decrypt.")
