# arb-files-translator

Automatically translate `.arb` files into multiple target locales using the `googletrans` Python library.

## Features

* Parses an input `.arb` file
* Uses Google Translate to generate translations for specified target locales
* Outputs new `.arb` files for each locale

## Prerequisites

* Python 3.6+
* `googletrans==3.1.0a0` (Ensure this exact version for stability)

## Installation

```bash
pip install googletrans==3.1.0a0
```

## Usage

1. Fill the `input.arb` file with key-value pairs you want translated.
2. In `main.py`, configure the following variables:

   * `inputLocale`: the language code of the original file (e.g. `en`)
   * `outputLocales`: a list of target language codes (e.g. `["fr", "es", "de"]`)
3. Run the script:

```bash
python main.py
```

## Example

```json
// input.arb
{
  "hello": "Hello",
  "goodbye": "Goodbye"
}
```

Output files generated:

* `app_fr.arb`
* `app_es.arb`
* `app_de.arb`

Each containing the translated strings.

## Notes

* Translations are machine-generated; manual review is recommended.
* Be cautious of rate limits when translating many entries or using many locales.

## License

MIT
