from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever
model = OllamaLLM(model="llama3.2")

template = """
You are an expert in answering questions about a pizza restaurant

here are some reviews that are relevant to the context ignore the numbering:{reviews}
here is a question to answer: {question}"""

prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

while True:
    print("\n\n ----------------------------------------------------------------------")
    question = input("Enter a question (Press q to quit): ")
    if question.lower() == "q":
        break
    reviews = retriever.invoke(question)
    res = chain.invoke(
        {
            "reviews": reviews,
            "question": question,
        }
    )
    print(res)
    print("\n\n ----------------------------------------------------------------------")
    print("Reviews Picked Up\n\n",reviews)
    print("\n\n ----------------------------------------------------------------------")
    # The code above uses the OllamaLLM model to answer a question about pizza restaurant reviews.
print 
# The code above uses the OllamaLLM model to answer a question about pizza restaurant reviews.
