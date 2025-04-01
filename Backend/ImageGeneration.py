import asyncio
from random import randint
from PIL import Image
import requests
from dotenv import get_key
import os
from time import sleep
from io import BytesIO  

def open_images(prompt):
    folder_path = r"Data"
    prompt = prompt.replace(" ", "_")

    Files = [f"{prompt}{i}.jpg" for i in range(1, 5)]

    for jpg_file in Files:
        image_path = os.path.join(folder_path, jpg_file)

        if os.path.exists(image_path) and os.path.getsize(image_path) > 0:  
            try:
                img = Image.open(image_path)
                print(f"Opening image: {image_path}")
                img.show()
                sleep(1)
            except IOError:
                print(f"Unable to open {image_path} (corrupt file).")
        else:
            print(f"Image {image_path} not found or is empty.")

API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
headers = {"Authorization": f"Bearer {get_key('.env', 'HuggingFaceAPIKey')}"}

async def query(payload):
    response = await asyncio.to_thread(requests.post, API_URL, headers=headers, json=payload)

    if response.status_code == 200:  
        return response.content
    else:
        print(f" API Error: {response.status_code} - {response.text}")  
        return None

async def generate_images(prompt: str):
    tasks = []
    os.makedirs("Data", exist_ok=True)  

    for _ in range(4):
        payload = {
            "inputs": f"{prompt}, quality=4k, sharpness=maximum, Ultra High details, high resolution, seed={randint(0, 1000000)}",
        }
        task = asyncio.create_task(query(payload))
        tasks.append(task)

    image_bytes_list = await asyncio.gather(*tasks)

    for i, image_bytes in enumerate(image_bytes_list):
        image_path = fr"Data\{prompt.replace(' ', '_')}{i + 1}.jpg"

        if image_bytes:  
            try:
                img = Image.open(BytesIO(image_bytes))  
                img.save(image_path, "JPEG")
                print(f" Saved {image_path}")
            except Exception as e:
                print(f" Failed to save image {image_path}: {e}")
        else:
            print(f" No valid image received for {image_path}")

def GenerateImages(prompt: str):
    try:
        asyncio.run(generate_images(prompt))
    except RuntimeError:  
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(generate_images(prompt))

    open_images(prompt)

while True:
    try:
        with open(r"Frontend\Files\ImageGeneration.data", "r") as f:
            Data: str = f.read().strip()

        if not Data:
            print("Error: File is empty.")
            break  

        Prompt, Status = Data.split(",")

        if Status.strip().lower() == "true":
            print("Generating Images...")
            GenerateImages(prompt=Prompt.strip())

            with open(r"Frontend\Files\ImageGeneration.data", "w") as f:
                f.write("False,False")

            break  

        else:
            sleep(1)

    except Exception as e:
        print(f"Error: {e}")  
        sleep(1)
