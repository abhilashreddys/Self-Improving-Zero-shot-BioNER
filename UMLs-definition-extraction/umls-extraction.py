import re
import pandas as pd
from groq import Groq
from umlsparser import UMLSParser

dataset_path = "define dataset path"
data = pd.read_csv(dataset_path)

def join_words(word_list):
    result = []
    word_list_new = word_list[1:-1]
    wordlistnew = word_list_new.replace("'","").split(",")
    wordlistnewnew = [x.strip() for x in wordlistnew]
    for word in wordlistnewnew:
        if result and not word.isalnum():
            result[-1] += word
        else:
            result.append(word)
    return ' '.join(result)


client = Groq(api_key="define groq_api_key")

def umls_list(inp):
    prompt = (
        "Extract medical entities from the passage. Medical entities include diseases, genes, mutations, and medically relevant terms. "
        "Do not include stop words and special characters in the output. Only return Python list of medical entities and do not include stopwords and special characters in it and return nothing else. Do not generate any type of code in the output\n\n"
        f"Passage: {inp}"
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="llama3-8b-8192", 
    )
    response_text = chat_completion.choices[0].message.content

    return response_text.lower()


data['sentences'] = data['tokens'].apply(join_words)
data['potential_tokens'] = data['sentences'].apply(umls_list)

data[['tokens','potential_tokens']].to_csv('define output path', index=False)

umls = UMLSParser('define umls data path')

concepts = umls.get_concepts()

def find_concept_definitions1(entity):
    entity = entity.strip('[]').replace("'", "").split(', ')
    matching_definitions = {}

    for key, concept in concepts.items():
        all_names = set()
        for lang_names in [concept._Concept__all_names, concept._Concept__preferred_names]:
            for lang_set in lang_names.values():
                all_names.update(lang_set)

        for e in entity:
            if e in all_names:
                if concept._Concept__definitions:
                    text = concept._Concept__definitions
                    text = re.sub('<.*?>', '', next(iter(text))[0])
                    matching_definitions[e] = text

    return matching_definitions

def cached_find_definitions(tokens):
    return [find_concept_definitions1(token) for token in tokens]

data['uml_definitions'] = cached_find_definitions(data['potential_tokens'])

data.to_csv('define output path', index=False)
