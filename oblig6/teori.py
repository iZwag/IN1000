# 1. Hva er innkapsling? Hvorfor er det nyttig?
# Kort sagt vil innkapsling vil si at relaterte variabler og metodene som jobber på dem samles sammen. I tillegg medfører dette  også kontroll på hvilken logikk som er tilgjengelig utenfor scopet til objektet/metoden. 
# Det er nyttig for det medfører bedre forutsigbarhet, logisk resonnering og lesbarhet for programmereren.
# Det er også nyttig for sikkerhet, så ikke viktige, interne variabler kan endres fra utside.

# 2. Hva er grensesnittet til en klasse? Hvordan skiller det seg fra implementasjonen av en klasse?
# Grensesnittet til en klasse er attributter ved klassen som tilgjengelig fra utsiden, spesielt metodene som kan anses som "public".
# Interfacet skiller seg fra implementasjonen ved at det avgrenser logikken som skjer på innsiden, dvs. interne variabler og logikk som ikke behøver, eller burde, være synlig fra utsiden.

# 3. Hva er en instansmetode, og hvordan skiller dette seg fra prosedyrene/funksjonene vi har møtt hittil?
# En instansmeteode er metoder som tar (self) som parameter når den blir kalt. Dette betyr at den har tilgang og kan jobbe på logikk som tilhører instansen av klassen sin.
# De andre funksjonene vi har sett har mer statiske oppgaver gitt av parametererene eller logikken på innsiden, og gjør kun det.
# Mulighetene er ofte større for instansemetodene - de har tilgang på mer informasjon.
