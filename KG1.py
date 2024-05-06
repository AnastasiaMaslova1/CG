from PIL import Image

def box_blur(image_path, output_path):
    kernel_size = int(input("Введите размер ядра[3, 5, 7]: "))
    img = Image.open(image_path)
    pixels = img.load()
    width, height = img.size

    # Создание нового изображения
    new_img = Image.new("RGB", (width, height))
    new_pixels = new_img.load()

    offset = kernel_size // 2

    for y in range(height):
        for x in range(width):
            total = [0, 0, 0]
            count = 0

            for ky in range(-offset, offset + 1):
                for kx in range(-offset, offset + 1):
                    nx, ny = x + kx, y + ky
                    if 0 <= nx < width and 0 <= ny < height:
                        pixel = pixels[nx, ny]
                        for i in range(3):
                            total[i] += pixel[i]
                        count += 1

            new_pixels[x, y] = tuple(t // count for t in total)

    new_img.save(output_path)
    new_img.show()

box_blur("104.jpg", "blurred_image.jpg")
