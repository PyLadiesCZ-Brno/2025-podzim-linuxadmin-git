# GitHub a pull requesty

Práce s tímto repozitářem bude simulovat **skutečný způsob práce na GitHubu**, kdy budete chtít dosáhnout umístění svého kódu v branchi _main_ v hlavním repu.

Zatím jsou zde úkoly na Python, ale možná přibudou i skriptovací úkoly pro Bash. ChatGPT mi vytvořilo podle zadání bashový skript, který vygeneroval všechny tasky i unit testy. Musel jsem to trochu upravit, protože to nefungovalo hned out-of-the-box. Příkaz `pytest` spustí všechny testy.

Funkce s tasky používají _typing annotation_ - je to moderní způsob psaní funkcí v Pythonu, kdy určujeme datové typy parametrů funkce a datový typ návratové hodnoty.

Úkoly 01 až 25 jsou jednoduché. Výzvou jsou až úkoly 25 až 40.

### Postup samostatné práce

1. Nahlásíš svůj GitHub username, abychom ti dali právo zápisu do tohoto repa
1. Vybereš si na jakém tasku budeš dělat. V tomto repozitáři na GitHubu založíš **Issue** s title číslo úkolu (např. **01**) - tím si úkol _zarezervuješ_, aby nikdo jiný neposlal pull request se svým řešením dřív než ty.
1. Vyřešíš a otestuješ task
    * Spustíš na své řešení `autopep8` - přečti si o [Coding style](https://kodim.cz/czechitas/uvod-do-progr-2/bonusy/coding-style/coding-style)
    * Spustíš na své řešení `pytest`
        * Jednotlivý test spustíš:
            ```
            pytest test_01_sum_two_numbers.py -vv
            ```

            Parametr `-v` a `-vv` zvyšuje vypisování detailů chyb.

1. Commitneš řešení do nové branche
    * Název branche **musí obsahovat tvoje jméno nebo iniciály, číslo tasku** a krátký popisek:
        * `mz-01-sum-two-numbers`
    * **Commit message musí začínat číslem tasku** a pokračovat vhodným popiskem:
        * `01 Soucet dvou cisel`
    * Pushneš tuto branch do tohoto repa.
1. Vytvoříš PR, které bude chtít zamergovat branch s řešením tasku do branche main.
    * **PR musí obsahovat přesně jeden tvůj commit**
        * Nech si od koučů poradit s `git commit --amend` popř. `git rebase -i`.
    * Aby byla hra na práci co nejvěrnější, je v repozitáři nastaveno CI (Continuous integration)
        * GitHub Action automaticky spustí `autopep8` a `pytest` pro tvůj task
        * Toto GitHub Action [workflow](.github/workflows/pr-checks.yml) bylo také vygenerováno pomocí ChatGPT, ale bylo opět nutné ho rozfungovat a zlepšit.
