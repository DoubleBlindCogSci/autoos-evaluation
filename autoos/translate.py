from gpt3 import gpt3


def translate(to_translate: str,
              train_prompt: str,
              preamble: str = '',
              start_word: str = '_gpt3:',
              stop_word: str = '_hum:',
              response_length: int = 1548) -> str:
    """
    Args:
        to_translate: the text to translate
        train_prompt: the training prompts
        preamble: a preamble to append set before the text (e.g. variables needed from code)
        start_word: the start word
        stop_word: the stop word
        response_length:

    Returns:
        Translated text (defined by the prompts)
    """
    if not to_translate:
        return ''
    prompt = f'{train_prompt}\n{preamble}\n{to_translate}\n{start_word}\n'
    answer, _ = gpt3(prompt, response_length=response_length, stop_seq=[stop_word])
    return answer
