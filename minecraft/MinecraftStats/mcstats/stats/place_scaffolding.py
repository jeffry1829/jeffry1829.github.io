from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'place_scaffolding',
        {
            'title': '建築工',
            'desc': '放置的鷹架數量',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:used','minecraft:scaffolding']),
        1908 # scaffolding added in 18w45a
    ))
