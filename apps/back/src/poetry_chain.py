import threading
from src.thread_generator import ThreadedGenerator
from src.chain_thread import chain_thread


def poetry_chain(prompt: str) -> ThreadedGenerator:
    template = """
        You are an excellent poet who generates creative poetry.
        A user will pass information on how he wants the poem to be and you must generate a poem with this information and separate it into stanzas of a maximum of 4 stanzas.
        try to generate the poem with rhymes.
        Return ONLY one to poetry and nothing else.
    """.strip()
    generator = ThreadedGenerator()
    threading.Thread(target=chain_thread, args=(generator, template, prompt)).start()
    return generator
