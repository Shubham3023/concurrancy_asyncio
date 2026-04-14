# without Multiprocessing

# import time
# from PIL import Image, ImageFilter
# import os

# image_names = os.listdir("Images")

# OUTPUT_FOLDER = "Processed_images"
# os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# if __name__ == "__main__":
#     start = time.perf_counter()
#     size = (1000, 1000)
#     for image_name in image_names:
#         try: 
#             file_name = os.path.join("Images", image_name)
#             img = Image.open(file_name)
#             img = img.filter(ImageFilter.GaussianBlur(15))
#             img.thumbnail(size)
#             image_path = os.path.join(OUTPUT_FOLDER, image_name)
#             img.save(image_path)
#             print(f'processed and saved {image_path}')
#         except Exception as e:
#             print(f"Error processing {image_name}: {e}")

#     finish = time.perf_counter()
#     print(f"Finished in {round(finish-start, 2)} seconds")

# With multiprocessing

import time
import concurrent.futures
from PIL import Image, ImageFilter
import os

images_names = os.listdir("Images") 

OUTPUT_FOLDER = "Processed_images"
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def process_image(image_name):
    try:
        file_name = os.path.join("Images", image_name)
        img = Image.open(file_name)
        img = img.filter(ImageFilter.GaussianBlur(10))
        img.thumbnail(size=(1200, 1200))
        image_path = os.path.join(OUTPUT_FOLDER, image_name)
        img.save(image_path)
        print(f'processed and saved {image_path}')
    except Exception as e:
        print(f"Error processing {image_name}: {e}")

if __name__ == "__main__":
    start = time.perf_counter()

    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(process_image, images_names)

    finish = time.perf_counter()
    print(f"Finished in {round(finish-start, 2)} seconds")