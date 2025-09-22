import re


def to_ipa(word):
    try:
        word = word.strip()
        word = re.sub(r'\d', '', word)
        word = re.sub(r'-', '', word)
        if '//' in word:
            words = word.split('//')
            words = [to_ipa(word) for word in words]
            return ' '.join(words)
        word = re.sub(r'/', '', word)
        word = re.sub(r'[\(\)]', '', word)
        word = re.sub(r'аᵸ|Аᵸ', '-ã', word)
        word = re.sub(r'Ā|ā', '-aː', word)
        word = re.sub(r'Āᵸ|āᵸ', '-ãː', word)
        word = re.sub(r'ГЪ|гъ', '-ʁ', word)
        word = re.sub(r'ГЬ|гь', '-h', word)
        word = re.sub(r'ГI|гӀ', '-ʕ', word)
        word = re.sub(r'Еᵸ|еᵸ', '-ẽ', word)
        word = re.sub(r'Ē|ē', '-eː', word)
        word = re.sub(r'Ēᵸ|ēᵸ', '-ẽː', word)
        word = re.sub(r'Иᵸ|иᵸ', '-ĩ', word)
        word = re.sub(r'Ӣ|ӣ', '-iː', word)
        word = re.sub(r'КЪ|къ', '-qχ’', word)
        word = re.sub(r'КЬ|кь', '-tɬ’', word)
        word = re.sub(r'КI|кӀ', '-k’', word)
        word = re.sub(r"Л'|л'", '-lʲ', word)
        word = re.sub(r'ЛЪ|лъ', '-ɬ', word)
        word = re.sub(r'ЛI|лӀ', '-tɬ', word)
        word = re.sub(r'Оᵸ|оᵸ', '-õ', word)
        word = re.sub(r'Ō|ō', '-oː', word)
        word = re.sub(r'Ōᵸ|ōᵸ', '-õː', word)
        word = re.sub(r'ПI|пӀ', '-p’', word)
        word = re.sub(r'ТI|тӀ', '-t’', word)
        word = re.sub(r'Уᵸ|уᵸ', '-ũ', word)
        word = re.sub(r'Ӯ|ӯ', '-uː', word)
        word = re.sub(r'Ӯᵸ|ӯᵸ', '-ũː', word)
        word = re.sub(r'ХЪ|хъ', '-qχ', word)
        word = re.sub(r'ХЬ|хь', '-x', word)
        word = re.sub(r'ХI|хӀ', '-ħ', word)
        word = re.sub(r'ЦI|цӀ', '-tsʼ', word)
        word = re.sub(r'ЧI|чӀ', '-tʃʼ', word)
        word = re.sub(r'Ыᵸ|ыᵸ', '-ɨ̃ ', word)
        word = re.sub(r'Ы̄|ы̄', '-ɨː', word)
        word = re.sub(r'Эᵸ|эᵸ', '-ʔẽ', word)
        word = re.sub(r'Э̄|э̄', '-ʔeː', word)
        word = re.sub(r'Э̄ᵸ|э̄ᵸ', '-ʔẽː', word)
        word = re.sub(r'I', '-ˁ', word)
        if re.search(r'А́|а́', word):
            word = re.sub(r'А́|а́', "-'a", word)
        word = re.sub(r'[Аа]', '-a', word)
        word = re.sub(r'[Бб]', '-b', word)
        word = re.sub(r'[Вв]', '-w', word)
        word = re.sub(r'[Гг]', '-g', word)
        word = re.sub(r'[Дд]', '-d', word)
        if re.search(r'Е́|е́', word):
            word = re.sub(r'Е́|е́', "-'e",word)
        word = re.sub(r'[Ее]', '-e', word)
        word = re.sub(r'[Жж]', '-ʒ', word)
        word = re.sub(r'[Зз]', '-z', word)
        if re.search(r'И́|и́', word):
            word = re.sub(r'И́|и́', "-'i", word)
        word = re.sub(r'И|и', '-i', word)
        word = re.sub(r'[Йй]', '-j', word)
        word = re.sub(r'[Кк]', '-kʰ', word)
        word = re.sub(r'[Лл]', '-l', word)
        word = re.sub(r'[Мм]', '-m', word)
        word = re.sub(r'[Нн]', '-n', word)
        if re.search(r'О́|о́', word):
            word = re.sub(r'О́|о́', "-'o", word)
        word = re.sub(r'О|о', '-o', word)
        word = re.sub(r'[Пп]', '-pʰ', word)
        word = re.sub(r'[Рр]', '-r', word)
        word = re.sub(r'[Сс]', '-s', word)
        word = re.sub(r'[Тт]', '-tʰ', word)
        if re.search(r'У́|у́', word):
            word = re.sub(r'У́|у́', "-'u", word)
        word = re.sub(r'У|у', '-u', word)
        word = re.sub(r'[Хх]', '-χ', word)
        word = re.sub(r'[Цц]', '-tsʰ', word)
        word = re.sub(r'[Чч]', '-tʃʰ', word)
        word = re.sub(r'[Шш]', '-ʃ', word)
        word = re.sub(r'[Ъъ]', '-ʔ', word)
        if re.search(r'Ы́|ы́', word):
            word = re.sub(r'Ы́|ы́', "-'ɨ", word)
        word = re.sub(r'[Ыы]', '-ɨ', word)
        if re.search(r'Э́|э́', word):
            word = re.sub(r'Э́|э́', "-'ʔe", word)
        word = re.sub(r'Э|э', '-ʔe', word)
        word = word[1::]
        VOWELS = 'aeiouɨ'
        segments = word.split('-')
        new_segments = []
        for previous, current in zip(segments, segments[1:]):
            if previous[0] in VOWELS and current[0] in VOWELS:
                new_segments.append('ʔ')
                new_segments.append(current)
            else:
                new_segments.append(current)
        segments_final = []
        segments_final.append(segments[0])
        segments_final.extend(new_segments)
        word_new = '-'.join(segments_final)
        word_no_spec_symbols = re.sub('[̃̃\- ̃:ʰ\'’]', '', word_new)
        if word_no_spec_symbols[0] in VOWELS:
            word_new = 'ʔ-' + word_new
        return word_new
    except IndexError:
        return word


def fix_m_accent(text):
    clusters = re.findall(r'[аеюяэыиоёу]м', text)
    vowel_accent = {'а': 'а́', 'е': 'е́', 'и': 'и́', 'о': 'о́', 'у': 'у́', 'ы': 'ы́', 'э': 'э́', 'ю': 'ю́', 'я': 'я́', 'ё': 'ё́'}
    for cluster in clusters:
        vowel_accented = vowel_accent[cluster[0]]
        text = re.sub(cluster, vowel_accented, text)
    return text


