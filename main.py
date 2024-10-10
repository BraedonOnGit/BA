# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pocketsphinx as ps


def print_hi(name):
    # Simulate speech input
    speech_text = "Hello, World!"

    # Initialize the recognizer
    config = ps.Decoder.default_config()
    config.set_string('-hmm', '/path/to/pocketsphinx/model/en-us/en-us')
    config.set_string('-lm', '/path/to/pocketsphinx/lm/en-us/en-us.lm.bin')
    config.set_string('-dict', '/path/to/pocketsphinx/dict/cmudict-en-us.dict')

    decoder = ps.Decoder(config)

    # Process the simulated speech
    result = decoder.decode(speech_text.encode(), True)

    print("Recognized:", result[0][1])


if __name__ == "__main__":
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
