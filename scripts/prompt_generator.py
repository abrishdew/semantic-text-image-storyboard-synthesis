import main
from main import APIKeys  

# Create an instance of the APIKeys class
api_keys = APIKeys()

api_keys.set_openai_api_key()
#define a template
template = "You are a prompt generator given a descrption. The prompt will be used to generate descriptive quality image. What is a concise prompt for the description {description}?"



prompt = main.PromptTemplate.from_template(template)
print(prompt.format(description="In the center of a vibrant scene, a high-resolution 3D Coca-Cola bottle surrounded by effervescent bubbles captures the viewer's attention. As the bubbles rise, the bottle seamlessly transforms into a sleek DJ turntable, complete with illuminated controls and a spinning vinyl record bearing the Coke Studio logo. This imagery symbolizes a fusion of refreshing beverage and rhythmic beats. Directly below this dynamic transformation, the call-to-action 'Mix Your Beat' shines in a bold, dynamic font with a playful energy. The text, surrounded by a subtle glow, invites interaction, set against a backdrop designed to evoke creativity and musical exploration."))

llm = main.OpenAI(temperature = 0.9)

chain = main.LLMChain(llm=llm, prompt=prompt)
print(chain.run({'description' : "In the center of a vibrant scene, a high-resolution 3D Coca-Cola bottle surrounded by effervescent bubbles captures the viewer's attention. As the bubbles rise, the bottle seamlessly transforms into a sleek DJ turntable, complete with illuminated controls and a spinning vinyl record bearing the Coke Studio logo. This imagery symbolizes a fusion of refreshing beverage and rhythmic beats. Directly below this dynamic transformation, the call-to-action 'Mix Your Beat' shines in a bold, dynamic font with a playful energy. The text, surrounded by a subtle glow, invites interaction, set against a backdrop designed to evoke creativity and musical exploration."}))