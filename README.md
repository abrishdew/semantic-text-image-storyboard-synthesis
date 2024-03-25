# Semantic Text to Image Storyboard Synthesis
***

### Project Overview
In this transformative era of advertising and recognizing the potential for technology to
streamline and enhance the ad creation process, Adludio is embarking on an
ambitious initiative to automate the end-to-end process of advertising production.
Adludio is a well renowned company in the business of advertisement creation for
different customers across the globe.
One aspect involves automation of this process so that the generation of potential
creative concepts based on the client's brief.
This transformation process aims to visually depict the narrative flow and user
interaction within advertisements, making the conceptualization of digital campaigns
both more intuitive and impactful.
Our task for this week, as part of this transformative process, is to architect and
develop a cutting-edge machine learning solution that automates the conversion of
textual advertisement concepts, assets descriptions into visually compelling
storyboards.

### Project Guide
Bring the concept to life, we will be using the perks of machine learning and diffusion
models broadly.
As a general scheme for the workflow, we have divided the project into three tasks for
ease of approach.
1) Image Generation and EDA analysis on the given Assets

- This task involves the generation of images using a model by adding the
concepts or ideas given as data. These concepts need some adjustment before
they are handed out to the LLMs for image generation.
- As for the EDA, that is a crucial step to help us identify the positions and
dimensions of images we find on a certain image on a Storyboard(either the
landing page or the Ending page). We can use the image search on image to
check and examine the segmented images.
2) Image Composition
3) Storyboard Creation

## Usage

This project aims to automate the end-to-end process of advertising production by converting textual advertisement concepts and assets descriptions into visually compelling storyboards.

## Prerequisites

- Python  3.x
- A virtual environment (optional but recommended)

## Setup

1. Clone the repository:

git clone https://github.com/yourusername/semantic-text-image-storyboard-synthesis.git

2. Change directory

cd semantic-text-image-storyboard-synthesis

3. Create and Activate a virtual environment (optional but recommended):

python3 -m venv venv

TO Activate
*On Win:* 

.\venv\Scripts\activate

*On Linux or Macos:*

source venv/bin/activate

4. Install the required dependencies:

pip install -r requirements.txt

5. Set up the environment variables:
   - Create a `.env` file in the project root directory.
   - Add the following lines to the `.env` file, replacing the placeholders with your actual API keys:
     ```
OPENAI_API_KEY=your_openai_api_key 
HUGGINGFACEHUB_API_KEY=your_huggingfacehub_api_key 
SERPAPI_API_KEY=your_serpapi_api_key

6. Run the main script:

python scripts/main.py


## Usage

To use the `APIKeys` class in your scripts, import it and create an instance:

python from scripts.api_keys import APIKeys

api_keys = APIKeys() api_keys.set_openai_api_key()

## Contributing

If you're open to contributions, please follow the standard fork, branch, and pull request workflow.

## License

This project is licensed under the MIT License.

