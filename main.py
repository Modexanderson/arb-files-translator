from googletrans import Translator


def rreplace(s, old, new, occurrence):

    li = s.rsplit(old, occurrence)

    return new.join(li)


if __name__ == "__main__":
    inputLocale = 'en'
    outputLocales = ['ar', 'bn', 'cs', 'de', 'es', 'fr', 'he', 'hi',
                     'id', 'it', 'ja', 'pt', 'ru', 'ta', 'tr', 'uk', 'ur', 'zh-cn']

    translator = Translator()
    file = open("input.arb", "r", encoding="ISO-8859-1")

    translations = {}

    for line in file:
        # Ignore empty lines and brackets
        if (line == '{\n' or line == '}' or line == ''):
            continue

         # Skip lines that don't have a colon and a space
        if ': ' not in line:
            continue

        # Ignore lines starting with "@"
        # if line.strip().startswith('@'):
        #     continue

        toTranslate = line.split('": ')[1][1:]
        toTranslate = toTranslate.split('"')[0]

        print(toTranslate)

        for supportedLocale in outputLocales:
            translation = translator.translate(
                toTranslate, src=inputLocale, dest=supportedLocale)
            newLine = rreplace(line, toTranslate, translation.text, 1)

            if (supportedLocale in translations.keys()):
                translations[supportedLocale].append(newLine)
            else:
                translations[supportedLocale] = [newLine]

    for key in translations.keys():
        with open("result/app_" + key + ".arb", "w", encoding='utf-8') as f:
            f.write('{\n')
            for line in translations[key]:
                f.write(line)
            f.write('}')
            f.close()
