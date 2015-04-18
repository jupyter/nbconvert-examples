def prepend_prompt(text):
    prompt = '>>> '
    result = []
    index = 0
    while index != -1:
        old_index = index
        index = text.find('\n', index)
        if index != -1:
            index += 1
            result.append(prompt + text[old_index:index])
            prompt = '... '
    if old_index == 0 or text[old_index:]:
        result.append(prompt + text[old_index:])
    return ''.join(result)
assert prepend_prompt('') == '>>> '
assert prepend_prompt('abc') == '>>> abc'
assert prepend_prompt('abc\n') == '>>> abc\n'
assert prepend_prompt('abc\ndef') == '>>> abc\n... def'
assert prepend_prompt('abc\ndef\n') == '>>> abc\n... def\n'
assert prepend_prompt('a\nb\nc\n') == '>>> a\n... b\n... c\n'
