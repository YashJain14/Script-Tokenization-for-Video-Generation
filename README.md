# Script-to-Video Generation with Diffusion Models

## Overview

This project utilizes diffusion models to generate video clips based on a provided script. The sentences serves as the primary prompt, guiding the generation process, while phrases extracted from each sentence act as secondary or positive prompts for ensuring consistency in the generated video content.

By combining natural language processing (NLP) techniques to parse the script into sentences and phrases, along with diffusion models for video generation, this system automates the creation of video content that aligns closely with the narrative and thematic elements of the provided script.

## Requirements

- Python 3.x
- SpaCy

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/YashJain14/Script-Tokenization-for-Video-Generation
    ```

2. Install dependencies:

    ```bash
    pip install spacy
    ```

3. Download SpaCy English model:

    ```bash
    python -m spacy download en_core_web_sm
    ```

## Example

```
The sun was setting behind the tall trees, casting long shadows across the forest floor. 
Birds chirped merrily as they returned to their nests, preparing for the night ahead. 
A gentle breeze rustled the leaves, carrying with it the scent of pine and earth. 
In the distance, a river meandered through the landscape, its waters shimmering in the fading light. 
The tranquility of the forest was broken by the occasional rustle of small animals moving through the underbrush. 
As dusk descended, the sky turned into a canvas of vibrant colors, painting the clouds with shades of pink, orange, and purple. 
Fireflies began to emerge, their soft glow adding to the enchanting atmosphere. 
It was a scene straight out of a fairy tale, where magic lingered in every corner and time seemed to stand still.
```

Running the script will produce prompts like:

```
Sentence: The sun was setting behind the tall trees, casting long shadows across the forest floor. 
Phrases: ['The sun', 'the tall trees', 'long shadows', 'the forest floor']

Sentence: Birds chirped merrily as they returned to their nests, preparing for the night ahead. 
Phrases: ['Birds', 'the night']

Sentence: A gentle breeze rustled the leaves, carrying with it the scent of pine and earth. 
Phrases: ['A gentle breeze', 'the leaves', 'the scent', 'pine', 'earth']

Sentence: In the distance, a river meandered through the landscape, its waters shimmering in the fading light. 
Phrases: ['the distance', 'the landscape', 'the fading light']

Sentence: The tranquility of the forest was broken by the occasional rustle of small animals moving through the underbrush. 
Phrases: ['The tranquility', 'the forest', 'the occasional rustle', 'small animals', 'the underbrush']

Sentence: As dusk descended, the sky turned into a canvas of vibrant colors, painting the clouds with shades of pink, orange, and purple. 
Phrases: ['dusk', 'the sky', 'a canvas', 'vibrant colors', 'the clouds', 'shades', 'purple']

Sentence: Fireflies began to emerge, their soft glow adding to the enchanting atmosphere. 
Phrases: ['Fireflies', 'the enchanting atmosphere']

Sentence: It was a scene straight out of a fairy tale, where magic lingered in every corner and time seemed to stand still.
Phrases: ['a scene', 'a fairy tale', 'magic', 'every corner', 'time']
```

You can use these prompts to generate video clips consistent with the script.

