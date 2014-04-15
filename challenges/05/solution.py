def ceaser_shift(shift, words):
    shift %= 26
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    words = words.lower()
    shifted_words = words.maketrans(alphabet, shifted_alphabet)

    return words.translate(shifted_words).upper()


def ceaser_output(shift):
    def decoration(function):
        def ceaser():
            words = function()

            return ceaser_shift(shift, words)
        return ceaser
    return decoration


def ceaser_input(shift, filter_function):
    def decoration(function):
        def ceaser(*args, **kwargs):
            function_args = []
            function_kwargs = {}
            for index, arg in enumerate(args):
                if filter_function(index):
                    function_args.append(ceaser_shift(shift, arg))
                else:
                    function_args.append(arg)

            for key, value in kwargs.items():
                if filter_function(key):
                    function_kwargs[key] = ceaser_shift(shift, value)
                else:
                    function_kwargs[key] = value

            return function(*function_args, **function_kwargs)
        return ceaser
    return decoration
