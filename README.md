# Translation Looper
This is a script that translates a phrase through a bunch of languages and then back to the source language to see how it changes.

It uses the Microsoft Azure translation service and requires an API key to use.

## Usage
1. Clone the repo: ```git clone https://github.com/MaxAnderson95/Translation-Looper.git```
2. Install the requirements ```pip install -r requirements.txt```
3. Export an environment variable named `SUBSCRIPTION_KEY` with your API key from azure
4. Export an environment variable named `LOCATION` with the Azure Region where your translation service is hosted. Ex. `eastus`
5. Run the script:
```commandline
python .\main.py --phrase "Good morning!" --rounds 10
Original phrase: Good morning

Translating to Pashto => سهار مو پخیر
Translating to Malay => Selamat pagi
Translating to Icelandic => Góðan dag
Translating to Divehi => ބާއްޖަވެރި މެންދުރެއް
Translating to Tigrinya => ጽቡቕ እዋን
Translating to Samoan => Taimi lelei
Translating to Tigrinya => ፅቡቕ እዋን
Translating to Inuinnaqtun => Algaaluarninga
Translating to German => Handschuhe
Translating to English => Gloves

Final translation after 10 rounds => Gloves
```

If you don't specify a number of rounds, it will run 20 by default.

You can also use a different source language other than English:
```commandline
python .\main.py --phrase "Bom dia" --source-language pt --rounds 10
Original phrase: Bom dia

Translating to Myanmar (Burmese) => မင်္ဂလာ နံနက်ခင်းပါ
Translating to Marathi => शुभ प्रभात
Translating to German => Guten Morgen
Translating to Urdu => صبح بخير
Translating to Khmer => អរុណសួស្តី
Translating to Swedish => God morgon
Translating to Haitian Creole => Bonjou
Translating to Somali => Haye
Translating to Hindi => सुनो
Translating to Portuguese (Brazil) => Ei, ouça.

Final translation after 10 rounds => Ei, ouça.
```

Each run will choose languages at random from the list of available from Microsoft.