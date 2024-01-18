Mans (Ginta Jankovska 221RMB019) projekta darbs Lietojumprogrammatūras automatizēšanas rīkos.
Es izveidoju programmatūru, kas dod iespēju ātri piekļūt pie konkrētām sadaļām mācību vidē ORTUS, jo ORTUS nav viena no ērtākajām vietām, lai pārskatītu vajadzīgo informāciju studentiem.

Tika izmantota tādas bibliotēkas, kā:
Selenium - kas dod iespēju izmantot vajadzīgo informāciju no tīmekļa vietnēm.
Time - kas dod iespēju apstādināt programmas procesu noteiktajā laika intervālā
Sys - kas dod iespēju apstādināt programmu noteiktajā brīdī

Programma lielākoties ir paredzēta DITF 1. kursa studentiem, jo citiem kursiem var atsķirties studiju kursi un pasniedzējiem paša ORTUS vide.

Pasniedzēji visticamāk nevarēs izmantot visas iespējas, ko piedāvā programma, piemēram Atzīmes par studiju programmām vai konkrētu studijas kursu.

Sākumā programma piedāvā ievadīt savu Lietotājvārdu un paroli, lai varētu ienākt ORTUS vidē.(Lai būtu ērtāka ienākšana ORTUS vidē ir ieteicams izmainīt 16 rindu no Login=input() uz Login="Vārds.Uzvārds" un 18 rindu no Parole=input() uz Parole="Sava parole")

Pēc tam tiek atvērta sākuma lapa ORTUSĀ ar kuru var jau darboties, bet programma piedāvā izvēlēties, ko vēlaties atvērt - Grafiku, Atzīmes par studiju programmām, Uzdoto uzdevumu grafiku, Konkrētu studijas kursu vai E-pastu.

SVARĪGI! Ja jums atverot E-pastu parāda kļūdu, tad ir jānomaina 80 un 85 rindā vērtība time.sleep(2) uz piemēram time.sleep(jūsu vērtība, kas ir lielāka par doto)

Kad jūs izvēlējāties, ko vēlaties atvērt, jūs varat turpināt darboties dotajā lapā un programma piedāvā "Vai jūs vēlaties turpināt", ja jūs izvēlēsieties "1", jeb "Jā" tad jums dos iespēju izvēlēties, ko jūs vēlaties atvērt, ja jūs izvēlēsieties "2", jeb "Nē" tad jūsu programma beigs darbību un tīmekļa vietne aizvērsies.
