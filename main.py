#TASK 2
from PIL import Image
def encrypt_image(input_path, output_path, key):
    image = Image.open(input_path)
    encrypted_image = Image.new(image.mode, image.size)
    pixels = image.load()
    encrypted_pixels = encrypted_image.load()

    for i in range(image.size[0]):
        for j in range(image.size[1]):
            pixel = pixels[i, j]
            if len(pixel) == 4:  # RGBA
                r, g, b, a = pixel
                encrypted_pixels[i, j] = ((r + key) % 256, (g + key) % 256, (b + key) % 256, a)
            else:  # RGB
                r, g, b = pixel
                encrypted_pixels[i, j] = ((r + key) % 256, (g + key) % 256, (b + key) % 256)

    encrypted_image.save(output_path)
    print(f"Image encrypted and saved as {output_path}")

def decrypt_image(input_path, output_path, key):
    image = Image.open(input_path)
    decrypted_image = Image.new(image.mode, image.size)
    pixels = image.load()
    decrypted_pixels = decrypted_image.load()

    for i in range(image.size[0]):
        for j in range(image.size[1]):
            pixel = pixels[i, j]
            if len(pixel) == 4:  # RGBA
                r, g, b, a = pixel
                decrypted_pixels[i, j] = ((r - key) % 256, (g - key) % 256, (b - key) % 256, a)
            else:  # RGB
                r, g, b = pixel
                decrypted_pixels[i, j] = ((r - key) % 256, (g - key) % 256, (b - key) % 256)

    decrypted_image.save(output_path)
    print(f"Image decrypted and saved as {output_path}")

def main():
    while True:
        choice = input("Do you want to (E)ncrypt or (D)ecrypt an image? Enter 'E' or 'D': ").upper()
        if choice not in ['E', 'D']:
            print("Invalid choice. Please enter 'E' for encrypt or 'D' for decrypt.")
            continue

        input_path = input("Enter the input image path: ")
        output_path = input("Enter the output image path: ")
        try:
            key = int(input("Enter the encryption key (0-255): "))
            if not (0 <= key <= 255):
                raise ValueError
        except ValueError:
            print("Invalid key. Please enter a number between 0 and 255.")
            continue

        if choice == 'E':
            encrypt_image(input_path, output_path, key)
        else:
            decrypt_image(input_path, output_path, key)

        another = input("Do you want to perform another operation? (Y/N): ").upper()
        if another != 'Y':
            break

if __name__ == "__main__":
    main()
