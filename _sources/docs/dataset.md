# Dataset and preprocessing

Om de dataset te kunnen gebruiken moeten we ze eerst preprocessen. Beide datasets bevat informatie over alle landen ter wereld. De eerste dataset bevat informatie over alle landen ter wereld. Sinds 1960 is jaarlijks bijgehouden hoeveel CO2-uitstoot er heeft plaatsgevonden in elk land. Ook wordt vermeld hoeveel energie het land heeft opgewekt en het percentage daarvan dat duurzaam en niet-duurzaam is. Per land worden ook de GDP en de bevolking vermeld. Dit geeft een goed beeld van hoe duurzaam een land is.

De tweede dataset bevat data die is verzameld in 2016 en richt zich op zaken zoals levensverwachting, sterfte onder volwassenen, sterfte onder zuigelingen en verschillende ziekten. Dit geeft ons een gedetailleerd beeld van de gezondheidssituatie in verschillende landen over de hele wereld.
Alle missende waardes hebben we als waarde -1 gegeven en bij de dataverwerking skippen we deze waardes.

Deze datasets willen we samenvoegen, om dit te doen gaan we alle waarden uit de eerste dataset pakken die in 2016 waren. Dit zorgt ervoor dat beide datasets uit hetzelfde jaar komen. We mergen beide datasets op een inner join op country_code. Country_code is een drieletterige code die uniek is voor elk land, en is perfect om hierop te mergen omdat ze hetzelfde zijn in beide datasets. Bij het mergen pakken we ook alleen de variabelen die wij willen gebruiken in het onderzoek.
Bij het preprocessen hebben we ook wat extra variabelen toegevoegd die niet in de datasets zitten, zoals total_renewable_energy_per_capita waarbij we alle opgewekte schone energie per persoon berekend hebben. In figuur 1 kan je zien hoe de head van de uiteindelijke dataset eruitziet.

