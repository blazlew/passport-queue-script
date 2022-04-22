# Passport Queue Script 🛂

Super simple, yet not the best quality and fragile script to alert the user about available reservation slots in the passport registration queue. It's not perfect, feel free to open pr's.
The key assumption of this script is that if it can't find a `Brak dostępnych` substring, it means that there are some slots available.

## User guide

```sh
brew install chromedriver
pip3 install -r requirements.txt
python3 script.py
```

## Caveats

For some reason `Ctrl+C` doesn't kill the script properly, and it keeps screaming that it found something, so I do `Ctrl+Z` and then `kill` the process.

## License

© 2022 BlazeIT Błażej Lewandowski
