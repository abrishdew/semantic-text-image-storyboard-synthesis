import PIL


class GenerateImage:

    def __init__(self) -> None:
        pass

    def make_grid(images, rows, cols, resize_to=128):
        images = [image.resize((resize_to, resize_to)) for image in images]
        w, h = images[0].size
        grid = PIL.Image.new("RGB", size=(cols*w, rows*h))
        for i, image in enumerate(images):
            grid.paste(image, box=(i%cols*w, i//cols*h))
        return grid



if __name__ == '__main__':
    # Load sample images
    sample_images = [Image.open('path_to_image1.jpg'), Image.open('path_to_image2.jpg')]

    # Instantiate the GenerateImage class
    generator = GenerateImage()

    # Call the make_grid method with sample data
    grid_image = generator.make_grid(sample_images,  2,  2)

    # Save the resulting grid image to disk
    grid_image.save('output_grid.jpg')