# Dataset and preprocessing

## Dataset
De datasets die gebruikt worden bevatten allebei informatie over alle landen ter wereld. De datasets zijn echter niet volledig bruikbaar omdat meerdere kolommen niet de beste waardes bevatten. Dit kan worden opgelost door ze te preprocessen.

### Dataset 1
Link: https://www.kaggle.com/datasets/tirant/country-by-country-data-collection-since-1960 
In de eerste dataset wordt er sinds 1960 jaarlijks bijgehouden hoeveel CO2 elk land heeft uitgestoten. Ook wordt vermeld hoeveel energie het land heeft opgewekt en het percentage daarvan dat duurzaam en niet-duurzaam is. Per land worden ook de GDP en de bevolking vermeld. Dit geeft een goed beeld van hoe duurzaam een land is.

### Dataset 2
Link: https://www.kaggle.com/datasets/mmattson/who-national-life-expectancy 
De tweede dataset bevat data die is verzameld van 2000 tot 2016 en richt zich op zaken zoals levensverwachting, sterfte onder volwassenen, sterfte onder baby's en de vaccinatiegraad van verschillende ziekten. Dit geeft ons een gedetailleerd beeld van de gezondheidssituatie in alle landen.

Voordat de datasets kunnen worden samengevoegd voor het eindproduct, worden ze eerst schoongemaakt. Om de data in de datasets consistent te maken, is ervoor gekozen om te filteren op het jaar 2016 aangezien dit het recentste jaar is dat aanwezig is in beide datasets. Vervolgens worden kolommen zonder data verwijderd en krijgen lege cellen een waarde van -1. Dit is nodig om deze waarden te herkennen en te filteren bij de dataverwerking. Ook hebben we extra variabelen berekend zoals CO2 per capita en GDP per capita, omdat deze meer betekenisvol zijn in het vergelijken van landen. Hierbij hebben we rekening gehouden met missende waarden, zodat er niet doorgerekend wordt met waarden van -1. Tenslotte worden de datasets samengevoegd met behulp van de inner join methode op de variabele country_code (Figuur 1), omdat deze consistent is over beide datsets. 

![Head van de database](head.png)
