Web alkalmazás: 3-féle eltérő megvalósítás lehetséges
* Flask + HTML, semmi JS "server-side rendering" megoldással
* Csak JS nincs új lap betöltés
* Flask + HTML  + JS "client-render" megoldással (tehát async fetch-ek) EZ még nem szkóp nektek, de lehet rajta agyalni aki akar

A funkció annyi, hogy:
* Főoldalon lát a user egy "exchange rate" táblát, lehet váltani HUF-ról USD, EUR-ra, meg EUR-ról USD-ra, meg ilyesmi, pár ilyen árfolyamot kell behardkódolni
* Van egy gomb a főoldalon ami a Váltás oldalra/nézetbe vezet, ahol "Amount", "From Currency" és "To Currency" inputokat tud megadni a user, és ha kattint a vált gombra, akkor látja mennyit USD-t kap a HUF-jáért pl.
* A váltás oldalról vissza lehet menni a főoldalra
* Az árfolyam "backend"-en van tárolva (kivéve csak a JS-es 2. esetben), onnan kell ezt előcsalni

A váltás a backenden (1. eset, flask) vagy frontenden (2. eset, JS) történik. A 3. esetben a backenden, csak JS-ből kell "fetch"-el meghívni a váltás funkciótt