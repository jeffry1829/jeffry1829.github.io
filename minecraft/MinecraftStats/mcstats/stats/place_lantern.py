from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'place_lantern',
        {
            'title': '懼黑',
            'desc': '放置的燈籠數量',
            'unit': 'int',
        },
        mcstats.StatDiffReader(
            mcstats.StatReader(['minecraft:used','minecraft:lantern']),
            mcstats.StatReader(['minecraft:mined','minecraft:lantern']),
        ),
        1910 # lanterns added in 18w46a
    ))
