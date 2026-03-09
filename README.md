# Training-LLMs-on-PCFGs
The intent of this project is to test whether Large Language Models (LLMs) (or augmented versions of them utilizing stack-based mechanisms) can learn synthetic data generated from a Context-Free Grammar (CFG).

The training data for this project is generated from Probabilistic Context-Free Grammars (PCFGs), where every production rule is assigned a specific probability of generation. Standard LLMs have historically had difficulty recognizing certain Context-Free Languages, especially nested recursive languages (like Dyck languages). 

We explore classical and novel LLM architectures for learning such synthetic data.
