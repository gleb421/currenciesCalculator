from currencies import Constants

print('Все коды валют:'
      'USD - Доллар\n'
      'EUR - Евро\n'
      'CNY - Юань\n'
      'INR - Индийская рупия\n'
      'KRW - Вона Республики Корея\n'
      'UAH - Украинская гривна\n'
      'GBP - Фунт стерлингов Соединенного королевства\n'
      'SEK - Шведская крона\n'
      'CHF - Швейцарский франк\n'
      'JPY - Японская иена\n'
      'CAD - Канадский доллар\n'
      'AED - Дирхам (оаэ)\n'
      'KZT - Казахстанский тенге\n'
      'BYN - Белорусский рубль\n'
      'BRL - Бразильский реал\n'
      'AMD - Армянский драм\n'
      'AZN - Азербайджанский манат\n'

      )


def currenciesCalc(chislo, val):
    if type(val) != str:
        raise TypeError("val should be a word")
    if type(chislo) not in [int, float]:
        raise TypeError("chislo should be a number")
    return chislo * Constants.currenc[val]
