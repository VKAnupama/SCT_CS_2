                                                                            readme.md                                                                                      
This is a simple Python-based image encryption and decryption tool built using pixel manipulation techniques.

 Features:

*Encrypt and decrypt any image.

*Multiple pixel-manipulation encryption methods:

   -Swap Mode: Scrambles the image by rearranging pixels based on a random sequence generated from a user key.

   -Add Mode: Applies a mathematical shift to every pixel value (mod 256). Reversible using the same value.

   -XOR Mode: Encrypts pixels using bitwise XOR — applying the same value again decrypts it.

*Supports reversible transformations.


 How It Works:

The tool loads an image and converts it into a numerical pixel matrix using NumPy.
Depending on the chosen encryption mode:

Pixels may be reordered,

Their color values may be mathematically shifted, or

They may be bitwise XOR-masked.

Since the encryption operations are mathematically reversible, running the tool again in decrypt mode restores the original image — as long as the same mode, key, and values are used.




