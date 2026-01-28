class STREAMLITTEXT:
    #Intro text in markdown
    PRICES_INTRO = """
    Op deze website presenteer ik de resultaten van mijn end-to-end datapipeline. 
    Deze datapipeline scraped elke dag de brandstofprijzen van een landelijke operator in brandstoffen.
    De data pipeline kun je hier vinden [Github](https://github.com/MaximiliaanO/Data-Pipeline---Fuel-Prices).
    """

    FUEL_COMMENT = '''
    In beide grafieken zien we per 1 januari 2026 een forse stijging in de brandstofprijzen.
    Dit komt doordat de overheid de accijns op brandstoffen vanaf die datum heeft [verhoogd](https://nos.nl/artikel/2596842-accijns-op-benzine-omhoog-en-er-volgt-meer-wennen-aan-2-50-per-liter).
    '''

    INTRODUCTIEPAGE_INTRO = """
    Op deze website presenteer ik een analyse van Nederlandse brandstofprijzen op basis van dagelijks verzamelde prijsdata van tankstations door het hele land.
    De data pipeline kun je hier vinden [Github](https://github.com/MaximiliaanO/Data-Pipeline---Fuel-Prices).

    De focus ligt op het inzichtelijk maken van **prijsontwikkelingen door de tijd** en de **verschillen tussen premium- en budgettankstations**.
    Voor zowel **benzine** als **diesel** worden de dagelijkse **minimum-, gemiddelde- en maximumprijzen** weergegeven.

    Hiermee is in één oogopslag te zien hoe groot de prijsbandbreedte is en hoe deze zich ontwikkelt. Daarnaast wordt onderscheid gemaakt tussen **premium** en **budget** pompen. Dit maakt het mogelijk om prijsverschillen tussen beide categorieën te analyseren en te beoordelen in hoeverre het type pomp structureel invloed heeft op het prijsniveau.

    Om dit verder te verdiepen worden aanvullende visualisaties toegevoegd, waaronder:

    - een overzicht van het aantal premium- en budgetpompen in de dataset
    - grafieken waarin per brandstof zowel het gemiddelde als de mediaan wordt getoond, uitgesplitst naar premium en budget pompen, zodat prijsverdelingen beter met elkaar kunnen worden vergeleken.

    Deze combinatie van tijdreeksen en verdelingsstatistieken biedt een genuanceerd beeld van de Nederlandse brandstofmarkt en laat zien waar, wanneer en bij welk type pomp prijsverschillen ontstaan.
    """

    PRIJZEN_SAMENVATTING_COMMENT = """
    Een opvallend verschil tussen premium- en budgettankstations is de relatie tussen het gemiddelde en de mediaan.
    Bij budgetpompen liggen deze twee waarden dicht bij elkaar, wat wijst op een relatief smalle prijsverdeling en een consistente prijszetting.

    Bij premiumtankstations ligt het gemiddelde structureel hoger dan de mediaan. Dit suggereert een grotere spreiding in prijzen, waarbij hogere prijzen of uitschieters het gemiddelde sterker beïnvloeden.

    Door zowel het gemiddelde als de mediaan te tonen, wordt zichtbaar dat prijsverschillen tussen pomptypes niet alleen in het niveau zitten, maar ook in de verdeling en stabiliteit van prijzen.
    """