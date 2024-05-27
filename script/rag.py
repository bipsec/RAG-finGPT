import argparse
from langchain_community.llms import Ollama
from langchain_community.vectorstores.chroma import Chroma
from langchain.prompts import ChatPromptTemplate
from langchain_community.embeddings.fastembed import FastEmbedEmbeddings

CHROMA_PATH = "chroma"

PROMPT_TEMPLATE = """ 
    <s>[INST] You are a seasoned stock market analyst. Your task is to list the positive investments and the negative investements based on the basic financials from the open price, high price, low price as well as the closing price and provide an analysis and prediction for the companies' stock price movement for the upcoming week. " \
    "Your answer format should be as follows:\n\n[Pretty Good Investment]:\n1. ...\n\n[Not a good investment]:\n1. ...\n\n[]:\n...\n [/INST] </s>
    [INST] {input}
           Context: {context}
           Answer:
    [/INST]
"""


def main():
    # Create CLI.
    parser = argparse.ArgumentParser()
    parser.add_argument("query_text", type=str, help="The query text.")
    args = parser.parse_args()
    query_text = args.query_text

    # Prepare the DB.
    embedding_function = FastEmbedEmbeddings()
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)


    # Search the DB.

    results = db.similarity_search_with_relevance_scores(query_text, k=3)
    if len(results) == 0 or results[0][1] < 0.7:
        print(f"Unable to find matching results.")
        return

    context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=context_text, question=query_text)
    print(prompt)

    model = Ollama(model="llama3")
    response_text = model.predict(prompt)

    sources = [doc.metadata.get("source", None) for doc, _score in results]
    formatted_response = f"Response: {response_text}\nSources: {sources}"
    print(formatted_response)


if __name__ == "__main__":
    main()
