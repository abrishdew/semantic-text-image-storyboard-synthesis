from typing import Literal, Optional, Tuple
import logging
import base64
from io import BytesIO
import io
import os
import torch
from diffusers import DiffusionPipeline
from torchvision import transforms
from PIL import Image
import requests
from pydantic import HttpUrl
from IPython.display import display



class ImageGenerater:
    def __init__(self, asset_suggestions: dict) -> None:
        self.asset_suggestions = asset_suggestions
        # Load the pretrained diffusion model
        self.pipeline = DiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5").to("cuda")

    def generate_images(self, store_location: str ='./images') -> dict:
        # Ensure the store_location directory exists
        os.makedirs(store_location, exist_ok=True)

        generated_images = {}
        for frame, elements in self.asset_suggestions.items():
            if frame.startswith('frame'):
                generated_images[frame] = []
                for type, description in elements.items():
                    images = self.pipeline(prompt=description).images
                    for idx, image in enumerate(images):
                        # Save the image to the specified location with .png extension
                        save_path = os.path.join(store_location, f"{frame}_{type}_{idx}.png")
                        image.save(save_path)
                        logging.info(f"Image saved to {save_path}")
                        # Add the save path to the generated_images dictionary
                        generated_images[frame].append((type, save_path))

        return generated_images

    @staticmethod
    def download_image(url: HttpUrl, save_path: str) -> Tuple[str, str]:
        """
        Downloads provided url data to given location.

        :param url: HTTP Url of the file.
        :param save_path: Folder location to save the data.
        :return: Tuple of the url and save location.
        """
        try:
            response = requests.get(url)
            
            if response.status_code ==  200:
                save_path = os.path.join(save_path, os.path.basename(url))
                image = Image.open(BytesIO(response.content))
                image.save(save_path)
                logging.info(f"Image saved to {save_path}")
                return (url, save_path)
            else:
                raise RuntimeError(f"Failed to download image. Status code: {response.status_code}") from None
        except Exception as e:
            raise RuntimeError(f"An error occurred: {e}") from e

if __name__ == "__main__":
    # Example usage
    concept = {
        "frame_1": {
            "Animated Element": "A high-resolution  3D Coca-Cola bottle center-screen, bubbles rising to the top, transitioning into a sleek DJ turntable with a vinyl record that has the Coke Studio logo.",
        },
        "frame_2": {
            "CTA Text": "'Mix Your Beat' in bold, playful font pulsating to the rhythm of a subtle background beat, positioned at the bottom of the screen."
        },
        "explanation": "This variation emphasizes the joy and interactivity of music mixing, with each frame building on the last to create a crescendo of engagement. The  3D bottle-to-turntable animation captures attention, the interactive beat mixer sustains engagement, and the vibrant animations encourage sharing, aligning with the campaign's objectives of engagement and message recall."
    }
    ig = ImageGenerater(concept)
    generated_images = ig.generate_images()
    # Now you can use the generated images as needed
